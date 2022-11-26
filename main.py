from game.game import Game

BOARD_DIMENSIONS = 5

def main():
    game = Game(BOARD_DIMENSIONS)
    while True:
        cont = game.tick()
        if not cont:
            print("Game exited by player")
            return


if __name__ == '__main__':
    main()
