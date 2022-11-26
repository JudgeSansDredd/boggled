from .board.board import Board
from .dice.dice import rollDice
from .screen.boggle_screen import Boggle_Screen


class Game:
    def __init__(self, board_dimensions):
        self.board = Board(rollDice(board_dimensions))
        self.screen = Boggle_Screen()
    def tick(self):
        self.screen.do_events()
        self.screen.tick(self.board)
