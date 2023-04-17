from Util import *
from Classes import *
from main import *

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1


    '''
        Player 1 turn
    '''
    def player1_turn(self):
        p = self.player1.current_pokemon

        while self.player1.current_pokemon.is_fainted():
            p = self.pokemon_select()
            self.player1.current_pokemon = p
        m = self.move_select()

        return p, m
    def pokemon_select(self):
        for i, pokemon in enumerate(self.player1.pokemon_list):
            print(i, pokemon)

        try:
            option = int(input('player1 input: '))
            if option not in range(len(self.player1.pokemon_list)):
                raise ValueError
        except ValueError:
            print('invalid input')
            return self.pokemon_select()

        if self.player1.pokemon_list[option].is_fainted():
            print('pokemon is fainted')
            return self.pokemon_select()

        return self.player1.pokemon_list[option]
    def move_select(self):
        for i, move in enumerate(self.player1.current_pokemon.moves):
            print(i, move)

        try:
            option = int(input('player1 input: '))
            if option not in range(len(self.player1.current_pokemon.moves)):
                raise ValueError
        except ValueError:
            print('invalid input')
            return self.move_select()

        if not self.player1.current_pokemon.moves[option].can_use():
            print('move is out of pp')
            return self.move_select()

        return self.player1.current_pokemon.moves[option]


    '''
        Player 2 turn
    '''
    def player2_turn(self):
        pass
    def get_player2_input(self):
        pass


    '''
        Game logic
    '''
    def check_game(self):
        # check if either player has no pokemon left
        if self.player1.pokemon_left() == 0:
            print('Player 2 wins!')
            exit()
        elif self.player2.pokemon_left() == 0:
            print('Player 1 wins!')
            exit()
    def do_move(self, *move, defender):
        attacker = move[0]
        move = move[1]

        if move.category == CATEGORY.PHYSICAL:
            L = attacker.level
            A = attacker.attack# moves will change bd ultimately
            D = defender.defense
            P = move.power
            S = 1.5 if attacker.type == move.type else 1 # STAB
            T = 1 # type effectiveness
            Z = 1 # random number between 0.85 and 1.00

            damage = ((((2 * L) / 5)+2) * P * (A / D)) / 50 + 2 * S * T * Z

            defender.current_hp -= damage
            print(f'{attacker.name} used {move.name} on {defender.name} for {damage} damage')
        else: return

    def Run(self):
        while True:
            # fastest current pokemon goes first
            if self.player1.current_pokemon.speed > self.player2.current_pokemon.speed:
                player1_move = self.player1_turn()
                player2_move = self.player2_turn()

                self.do_move(player1_move,self.player2.current_pokemon)
                self.do_move(player2_move,self.player1.current_pokemon)
            else:
                player2_move = self.player2_turn()
                player1_move = self.player1_turn()

                self.do_move(player2_move,self.player1.current_pokemon)
                self.do_move(player1_move,self.player2.current_pokemon)

            self.check_game()
            self.turn += 1