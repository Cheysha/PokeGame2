from Util import *
from Classes import *
from main import *

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1


    def player1_turn(self):

        while not self.player1.current_pokemon.is_fainted():
            self.player1_select_move()
        # self.player1_select_pokemon() # should i make this a propertry of the trainer

    def player2_turn(self):
        pass

    def get_player2_input(self):
        pass

    def run(self):
        while True:
            pass