from Util import *
from Classes import *
from main import *

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1


    def player1_turn(self):

        while self.player1.current_pokemon.is_fainted():
            self.pokemon_select()

        self.move_select()
    def pokemon_select(self):

        for pokemon in self.player1.pokemon_list:
            print(self.player1.pokemon_list.index(pokemon), end=' ')
            print(pokemon)

        option = input('player1 input: ')

        while option not in [str(i) for i in range(len(self.player1.pokemon_list))]:
            print('invalid input')
            option = input('player1 input: ')

        while self.player1.pokemon_list[int(option)].is_fainted():
            print('pokemon is fainted')
            option = input('player1 input: ')

        self.player1.set_current_pokemon(self.player1.pokemon_list[int(option)])

    def move_select(self):
        for move in self.player1.current_pokemon.moves:
            print(self.player1.current_pokemon.moves.index(move), end=' ')
            print(move)

        option = input('player1 input: ')

        while option not in [str(i) for i in range(len(self.player1.current_pokemon.moves))]:
            print('invalid input')
            option = input('player1 input: ')

        while not self.player1.current_pokemon.moves[int(option)].can_use():
            print('move is out of pp')
            option = input('player1 input: ')

        return self.player1.current_pokemon.moves[int(option)] # returns the move object


    def player2_turn(self):
        pass
    def get_player2_input(self):
        pass

    def check_game(self):
        # check if either player has no pokemon left
        if self.player1.pokemon_left() == 0:
            print('Player 2 wins!')
            exit()
        elif self.player2.pokemon_left() == 0:
            print('Player 1 wins!')
            exit()

    def do_move(self, move, attacker, defender):
        # if move is physical
        if move.category == 'physical':
            # calculate damage
            damage = int((((2 * attacker.level) / 5 + 2) * move.power * (attacker.attack / defender.defense)) / 50 + 2)
            # apply damage
            defender.current_hp -= damage
            # print damage
            print(f'{attacker.name} used {move.name} on {defender.name} for {damage} damage!')
        # if move is special
        elif move.category == 'special':
            # calculate damage
            damage = int((((2 * attacker.level) / 5 + 2) * move.power * (attacker.special_attack / defender.special_defense)) / 50 + 2)
            # apply damage
            defender.current_hp -= damage
            # print damage
            print(f'{attacker.name} used {move.name} on {defender.name} for {damage} damage!')
        # if move is status
        elif move.category == 'status':
            # apply status
            pass


        pass



    def Run(self):
        while True:
            # fastest current pokemon goes first
            if self.player1.current_pokemon.speed > self.player2.current_pokemon.speed:
                self.player1_turn()

                self.player2_turn()
            else:
                self.player2_turn()

                self.player1_turn()

            self.check_game()
            self.turn += 1