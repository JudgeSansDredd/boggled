from game.game import Game

BOARD_DIMENSIONS = 5

def main():
    game = Game(BOARD_DIMENSIONS)
    while True:
        tick_response = game.tick()
        if 'quit' in tick_response and tick_response['quit']:
            print("Game exited by player")
            return


if __name__ == '__main__':
    main()
