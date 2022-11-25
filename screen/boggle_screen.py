import pygame

from .screen import Screen


class Boggle_Screen(Screen):
    def __init__(self, board):
        super().__init__("Nathan's Boggler", (800, 600))
        self.board = board

    def tick(self):
        self.clear_screen()
        self.draw_dice()
        self.update()

    def draw_dice(self):
        die_width = 75
        die_gap = 10
        dice_positions = []
        increment = die_gap + die_width
        for i in range(self.board.dimension):
            x = 25 + i * increment
            for j in range(self.board.dimension):
                y = 25 + j * increment
                dice_positions.append(self.translateXY((x, y)))

        for die in dice_positions:
            pygame.draw.rect(
                self.surface,
                (255, 255, 255),
                pygame.Rect(
                    die[0],
                    die[1],
                    self.normalize_measurement(die_width),
                    self.normalize_measurement(die_width)
                ),
                0,
                5
            )

        # font = pygame.font.SysFont('arialunicode', 100)
        # for die in dice_positions:
        #     img = font.render('A', True, (255, 0, 0))
        #     self.surface.blit(img, (20, 20))
