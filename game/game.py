from .board.board import Board
from .dice.dice import rollDice
from .screen.boggle_screen import Boggle_Screen


class Game:
    def __init__(self, board_dimensions):
        self.board = Board(rollDice(board_dimensions))
        self.screen = Boggle_Screen()
        self.check_word = ''

    def tick(self):
        if not self.screen.do_events():
            return False # Game quit
        self.check_word = self.screen.check_word
        path = self.board.find_word(self.check_word)
        self.screen.draw_screen(self.board, path)

        return True
