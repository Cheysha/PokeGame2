from main import *
from Classes import *
from unittest import TestCase


class Test(TestCase):
    def test_get_pokemon(self):
        # create list with 4 random numbers
        random_numbers = [random.randint(1, 340) for i in range(4)]

        # create a list of 4 pokemon to test
        test_pokemon = [get_pokemon(random_numbers[0]), get_pokemon(random_numbers[1]),
                        get_pokemon(random_numbers[2]), get_pokemon(random_numbers[3])]

        # create a list of the expected values from the global lists
        expected = [poke_list['identifier'].values[random_numbers[0] - 1],
                    poke_list['identifier'].values[random_numbers[1] - 1],
                    poke_list['identifier'].values[random_numbers[2] - 1],
                    poke_list['identifier'].values[random_numbers[3] - 1]]

        # create a list of the actual values
        actual = [pokemon.name for pokemon in test_pokemon]

        # assert that the expected and actual values are the same, ignore if theres a - where a space should be
        for i in range(len(expected)):
            assert expected[i].replace('-', ' ') == actual[i].replace('-', ' ')
    def test_get_move(self):
        # create a list of 5 moves to test
        test_moves = [get_move('tackle'), get_move('ember'), get_move('water gun'),
                      get_move('thunder shock'), get_move('tackle')]
        # create a list of the expected values
        expected = ['tackle', 'ember', 'water gun', 'thunder shock', 'tackle']
        # create a list of the actual values
        actual = [move.name for move in test_moves]
        # assert that the expected and actual values are the same, ignore if theres a - where a space should be
        for i in range(len(expected)):
            assert expected[i].replace('-', ' ') == actual[i].replace('-', ' ')


class TestGame(TestCase):
    player1 = new_player('random')
    player2 = new_player('random')

    game = Game(player1, player2)

    def test_player1_turn(self):
        self.game.player1_turn()

class TestPlayer(TestCase):
    player = new_player('random')

    def test_select_pokemon(self):
        self.player.pokemon_list[0].current_hp = 0
        self.player.pokemon_select()

        assert self.player.current_pokemon in self.player.pokemon_list and not self.player.current_pokemon.is_fainted()

    def test_move_select(self):
        self.player.current_pokemon.moves[0].pp = 0
        test = self.player.move_select()

        assert test in self.player.current_pokemon.moves and test.can_use()



