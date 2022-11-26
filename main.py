from board.board import Board
from dice.dice import rollDice
from screen.boggle_screen import Boggle_Screen

BOARD_DIMENSIONS = 5

class Game:
    def __init__(self):
        self.board = Board(rollDice(BOARD_DIMENSIONS))
        self.screen = Boggle_Screen()
    def tick(self):
        self.screen.do_events()
        self.screen.tick(self.board)

def main():
    game = Game()
    while True:
        game.tick()


if __name__ == '__main__':
    main()
