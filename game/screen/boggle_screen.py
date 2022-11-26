import pygame

from .screen import Screen


class Boggle_Screen(Screen):
    def __init__(self):
        super().__init__("Nathan's Boggler", (800, 600))
        self.check_word = ''

    def draw_screen(self, board, highlight_path):
        self._clear_screen()
        self._draw_dice(board, highlight_path)
        self._draw_check_word()
        self._update()

    def _draw_check_word(self):
        font = pygame.font.SysFont('arialunicode', round(18))
        img = font.render(self.check_word, True, (255, 0, 0))
        _, surface_height = self.surface.get_size()
        check_word_pos = (25, surface_height - 100)
        self.surface.blit(img, check_word_pos)

    def _draw_dice(self, board, highlight_path):
        desired_box_size = (800, 500)
        box_gutter = 25
        max_box_size = min(desired_box_size) - 2 * box_gutter
        die_gap = 10
        num_gaps = board.dimension - 1
        gap_usage = die_gap * num_gaps
        die_usage = max_box_size - gap_usage
        die_size = die_usage / board.dimension
        normalized_die_size = self.normalize_measurement(die_size)
        dice_positions = []
        for i in range(board.dimension):
            x = box_gutter + i * (die_size + die_gap)
            for j in range(board.dimension):
                y = box_gutter + j * (die_size + die_gap)
                position = (x, y)
                die_position = self.translateXY(position)
                letter = board.get_letter((i, j))
                dice_positions.append({
                    'x': die_position[0],
                    'y': die_position[1],
                    'letter': letter,
                    'highlighted': highlight_path and (i, j) in highlight_path
                })

        font = pygame.font.SysFont('arialunicode', round(die_size))
        for die in dice_positions:
            pygame.draw.rect(
                self.surface,
                (255, 255, 255) if not die['highlighted'] else (0, 255, 0),
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

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.check_word = ''
            elif event.key == pygame.K_BACKSPACE:
                self.check_word = self.check_word[:-1]
            else:
                self.check_word += event.unicode.upper()
