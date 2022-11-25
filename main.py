from board.board import Board
from dice.dice import rollDice
from screen.screen import Screen


def main():
    board = Board(rollDice(5))
    board.print()
    screen = Screen("Nathan's Boggler")
    while True:
        if screen.check_user_quit():
            return


if __name__ == '__main__':
    main()
