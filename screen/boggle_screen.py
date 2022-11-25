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
        desired_box_size = (800, 500)
        box_gutter = 25
        max_box_size = min(desired_box_size) - 2 * box_gutter
        die_gap = 10
        num_gaps = self.board.dimension - 1
        gap_usage = die_gap * num_gaps
        die_usage = max_box_size - gap_usage
        die_size = die_usage / self.board.dimension
        normalized_die_size = self.normalize_measurement(die_size)
        dice_positions = []
        for i in range(self.board.dimension):
            x = box_gutter + i * (die_size + die_gap)
            for j in range(self.board.dimension):
                y = box_gutter + j * (die_size + die_gap)
                position = (x, y)
                die_position = self.translateXY(position)
                letter = self.board.get_letter((i, j))
                dice_positions.append({
                    'x': die_position[0],
                    'y': die_position[1],
                    'letter': letter
                })

        font = pygame.font.SysFont('arialunicode', round(die_size))
        for die in dice_positions:
            pygame.draw.rect(
                self.surface,
                (255, 255, 255),
                pygame.Rect(
                    die['x'],
                    die['y'],
                    normalized_die_size,
                    normalized_die_size
                ),
                0,
                5
            )
            text_width, text_height = font.size(die['letter'])
            gutter_x = (normalized_die_size - text_width) / 2
            gutter_y = (normalized_die_size - text_height) / 2
            img = font.render(die['letter'], True, (255, 0, 0))
            self.surface.blit(img, (die['x'] + gutter_x, die['y'] + gutter_y))
