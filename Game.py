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
            self.player1.pokemon_select()

        self.player1.move_select()

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
                t1= self.player1_turn()

                t2 =self.player2_turn()
            else:
                t2= self.player2_turn()
                t1= self.player1_turn()

            self.check_game()
            self.turn += 1