from board.board import Board
from dice.dice import rollDice
from screen.boggle_screen import Boggle_Screen


def main():
    board = Board(rollDice(5))
    board.print()
    screen = Boggle_Screen(board)
    while True:
        if screen.check_user_quit():
            return
        screen.tick()


if __name__ == '__main__':
    main()
