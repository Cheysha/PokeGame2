from main import *
from Classes import *
from Util import *
from Game import *
from unittest import TestCase




class Test(TestCase):

    #   tests the pokemon generator, makes sure it returns a legal pokemon
    def test_pokemon(self):


        index = 3
        pokemon = get_pokemon(index)

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
        p = poke_list.loc[poke_list['id'] == index]
        s = stat_list.loc[stat_list['pokemon_id'] == index]
        #m = moveset_list.loc[moveset_list['pokemon_id'] == index]
        #m = move_list.loc[move_list['id'].isin(m['move_id'])]

        assert name == p['identifier'].values[0]
        assert _type == TYPES(type_list.loc[type_list['pokemon_id'] == index]['type_id'].values[0]).name.lower()
        assert hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
        assert attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
        assert defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
        assert sp_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
        assert sp_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
        assert speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])
    def test_pokemon(self, pokemon):
        pokemon = pokemon

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
        p = poke_list.loc[poke_list['id'] == index]
        s = stat_list.loc[stat_list['pokemon_id'] == index]
        # m = moveset_list.loc[moveset_list['pokemon_id'] == index]
        # m = move_list.loc[move_list['id'].isin(m['move_id'])]

        assert name == p['identifier'].values[0]
        assert _type == TYPES(type_list.loc[type_list['pokemon_id'] == index]['type_id'].values[0]).name.lower()
        assert hp == int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
        assert attack == int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
        assert defense == int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
        assert sp_attack == int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
        assert sp_defense == int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
        assert speed == int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])

    #   tests the move generator, makes sure it returns a legal move
    def test_move(self):
        # Test valid index
        index = 1
        move = get_move(index)
        assert isinstance(move, Move)
        assert move.index == index
        assert move.name == move_list.loc[move_list['id'] == index, 'identifier'].iloc[0]
        assert move.type == TYPES(move_list.loc[move_list['id'] == index, 'type_id'].iloc[0])
        assert move.power == move_list.loc[move_list['id'] == index, 'power'].iloc[0]
        assert move.accuracy == move_list.loc[move_list['id'] == index, 'accuracy'].iloc[0]
        assert move.pp == move_list.loc[move_list['id'] == index, 'pp'].iloc[0]
        assert move.category == CATEGORY(move_list.loc[move_list['id'] == index, 'damage_class_id'].iloc[0])

    def test_new_player(self):
        name = 'chey'
        player = new_player(name)
        assert player.name == name
        # assert that each pokemon in party is legal
        for pokemon in player.pokemon_list:
            self.test_pokemon(pokemon)


class TestGame(TestCase):
    player1 = new_player('test')
    player2 = new_player('test')





    game = Game(player1, player2)

    def test_player1_turn(self):
        self.game.player1_turn()

    def test_do_move(self):
        player_2_hp = self.game.player2.current_pokemon.current_hp
        self.game.do_move(self.player1.current_pokemon.moves[0],self.game.player1, self.game.player2)
        #assert self.game.player2.current_pokemon.current_hp < player_2_hp







