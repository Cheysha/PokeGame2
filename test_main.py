from main import *
from Classes import *
from Util import *
from Generators import *
from Game import *
from unittest import TestCase


class GeneratorTest(TestCase):

    '''
        Generator Tests
    '''
    def test_pokemon(self):
        index = random.randint(1, 807)
        pokemon = generate_pokemon_from_index(index)

        index = pokemon.index
        name = pokemon.name
        _type = pokemon.type.name.lower()
        hp = pokemon.base_hp
        attack = pokemon.base_attack
        defense = pokemon.base_defense
        sp_attack = pokemon.base_special_attack
        sp_defense = pokemon.base_special_defense
        speed = pokemon.base_speed

        # Check values against data frames
        p = global_pokemon_frame.loc[global_pokemon_frame['id'] == index]
        s = global_stat_frame.loc[global_stat_frame['pokemon_id'] == index]
        #m = moveset_list.loc[moveset_list['pokemon_id'] == index]
        #m = move_list.loc[move_list['id'].isin(m['move_id'])]



        assert name == p['identifier'].values[0]
        assert _type == TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower()
        assert hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
        assert attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
        assert defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
        assert sp_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
        assert sp_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
        assert speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])

    def test_move(self):
        # Test valid index
        index = random.randint(1, 100)
        move = generate_move_from_index(index)
        assert isinstance(move, Move), f"Move is {move} but should be a Move object"
        assert move.index == index, f"Move index is {move.index} but should be {index}"
        assert move.name == global_move_frame.loc[global_move_frame['id'] == index, 'identifier'].iloc[0] , \
            f"Move name is {move.name} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'identifier'].iloc[0]}"
        assert move.type == TYPES(global_move_frame.loc[global_move_frame['id'] == index, 'type_id'].iloc[0]) , \
            f"Move type is {move.type} but should be {TYPES(global_move_frame.loc[global_move_frame['id'] == index, 'type_id'].iloc[0])}"
        assert move.power == global_move_frame.loc[global_move_frame['id'] == index, 'power'].iloc[0] , \
            f"Move power is {move.power} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'power'].iloc[0]}"
        assert move.accuracy == global_move_frame.loc[global_move_frame['id'] == index, 'accuracy'].iloc[0] , \
            f"Move accuracy is {move.accuracy} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'accuracy'].iloc[0]}"
        assert move.pp == global_move_frame.loc[global_move_frame['id'] == index, 'pp'].iloc[0] , \
            f"Move pp is {move.pp} but should be {global_move_frame.loc[global_move_frame['id'] == index, 'pp'].iloc[0]}"
        assert move.category == CATEGORY(global_move_frame.loc[global_move_frame['id'] == index, 'damage_class_id'].iloc[0]) , \
            f"Move category is {move.category} but should be {CATEGORY(global_move_frame.loc[global_move_frame['id'] == index, 'damage_class_id'].iloc[0])}"
        pass
    def test_new_player(self):
        name = 'chey'
        player = new_player(name)
        assert player.name == name, f"Player name is {player.name} but should be {name}"

        assert player.current_pokemon == player.pokemon_list[0], \
        f"Player current pokemon is {player.current_pokemon} but should be {player.pokemon_list[0]}"

        assert len(player.pokemon_list) <= BAG_SIZE, \
            f"Player pokemon list size is {len(player.pokemon_list)} but should be less than or equal to {BAG_SIZE}"

        for pokemon in player.pokemon_list:

            index = pokemon.index
            p = global_pokemon_frame.loc[global_pokemon_frame['id'] == index]
            s = global_stat_frame.loc[global_stat_frame['pokemon_id'] == index]

            assert pokemon.name == p['identifier'].values[0], \
                f"Pokemon name is {pokemon.name} but should be {p['identifier'].values[0]}"
            assert pokemon.type.name.lower() == TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower(), \
                f"Pokemon type is {pokemon.type} but should be {TYPES(global_type_frame.loc[global_type_frame['pokemon_id'] == index]['type_id'].values[0]).name.lower()}"
            assert pokemon.base_hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0]), \
                f"Pokemon hp is {pokemon.hp} but should be {int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])}"
            assert pokemon.base_attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0]), \
                f"Pokemon attack is {pokemon.attack} but should be {int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])}"
            assert pokemon.base_defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0]), \
                f"Pokemon defense is {pokemon.defense} but should be {int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])}"
            assert pokemon.base_special_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0]), \
                f"Pokemon sp_attack is {pokemon.sp_attack} but should be {int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])}"
            assert pokemon.base_special_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0]), \
                f"Pokemon sp_defense is {pokemon.sp_defense} but should be {int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])}"
            assert pokemon.base_speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0]), \
                f"Pokemon speed is {pokemon.speed} but should be {int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])}"

class GameTests(TestCase):

    trainer1 = Trainer('chey')
    # add 3 pokemon to trainer1
    trainer1.add_pokemon(generate_pokemon_from_index(1))
    trainer1.add_pokemon(generate_pokemon_from_index(2))
    trainer1.add_pokemon(generate_pokemon_from_index(3))
    trainer1.current_pokemon = trainer1.pokemon_list[0]

    trainer2 = Trainer('rival')
    # add 3 pokemon to trainer2
    trainer2.add_pokemon(generate_pokemon_from_index(4))
    trainer2.add_pokemon(generate_pokemon_from_index(5))
    trainer2.add_pokemon(generate_pokemon_from_index(6))
    trainer2.current_pokemon = trainer2.pokemon_list[0]



    game = Game(trainer1, trainer2)

    '''
          Game tests
    '''

    def test_game_entry(self):
        # assert both players current pokemon have full hp
        assert self.game.player1.current_pokemon.current_hp == self.game.player1.current_pokemon.max_hp, \
            f"Player 1 current pokemon hp is {self.game.player1.current_pokemon.current_hp} but should be {self.game.player1.current_pokemon.max_hp}"
        assert self.game.player2.current_pokemon.current_hp == self.game.player2.current_pokemon.max_hp, \
            f"Player 2 current pokemon hp is {self.game.player2.current_pokemon.current_hp} but should be {self.game.player2.current_pokemon.max_hp}"

        pass


    '''
        Player 1 tests
    '''
    def test_player1_pokemon_select(self):
        temp = self.game.pokemon_select()

        assert temp in self.game.player1.pokemon_list, \
            f"Pokemon {temp} is not in player 1 pokemon list"
        assert temp.current_hp > 0, \
            f"Pokemon {temp} is faint"

        pass

    def test_player1_pokemon_select_faint(self):
        self.game.player1.current_pokemon.current_hp = 0
        temp = self.game.pokemon_select()

        assert temp in self.game.player1.pokemon_list, \
            f"Pokemon {temp} is not in player 1 pokemon list"
        assert temp.current_hp > 0, \
            f"Pokemon {temp} is faint"


    def test_player1_move_select(self):
        temp = self.game.move_select()

        assert temp in self.game.player1.current_pokemon.moves, \
            f"Move {temp} is not in player 1 current pokemon moves"
        assert temp.pp > 0, \
            f"Move {temp} is out of pp"

    def test_player1_move_select_no_pp(self):
        self.game.player1.current_pokemon.moves[0].pp = 0
        temp = self.game.move_select()

        assert temp in self.game.player1.current_pokemon.moves, \
            f"Move {temp} is not in player 1 current pokemon moves"
        assert temp.pp > 0, \
            f"Move {temp} is out of pp"


    def test_pleyer1_turn(self):
        t = self.game.player1_turn()

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    def test_pleyer1_turn_no_health(self):
        self.game.player1.pokemon_list[0].current_hp = 0
        t = self.game.player1_turn()

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    def test_pleyer1_turn_no_pp(self):
        #set the pp of all player1 current pokemon moves to 0
        for move in self.game.player1.current_pokemon.moves:
            move.pp = 0
        # a way out of hte test
        self.game.player1.current_pokemon.moves[0].pp = 1

        t = self.game.player1_turn()

        assert isinstance(t, tuple), \
            f"Player 1 turn is {t} but should be a tuple"

        assert isinstance(t[0], Pokemon), \
            f"Player 1 turn pokemon is {t[0]} but should be a pokemon"
        assert t[0].current_hp > 0, \
            f"Player 1 turn pokemon {t[0]} is faint"

        assert isinstance(t[1], Move), \
            f"Player 1 turn move is {t[1]} but should be a move"
        assert t[1].pp > 0, \
            f"Player 1 turn move {t[1]} is out of pp"

    '''
        Battle tests
    '''

    def test_do_move(self):
        test_attacker = self.game.player1.current_pokemon
        test_defender = self.game.player2.current_pokemon
        test_move = test_attacker.moves[0]

        # get the damage before the move
        initial_health = test_defender.current_hp
        # do the move
        self.game.do_move(test_attacker, test_move, defender=test_defender)

        # assert attack did damage
        assert initial_health > test_defender.current_hp, \
            f"Pokemon {test_defender} did not take damag{test_defender.current_hp}"






