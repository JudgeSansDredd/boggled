from game.game import Game

BOARD_DIMENSIONS = 5

def main():
    game = Game(BOARD_DIMENSIONS)
    while True:
        game.tick()


if __name__ == '__main__':
    main()
