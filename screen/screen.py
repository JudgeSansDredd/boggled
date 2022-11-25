import pygame


class Screen:
    def __init__(self, caption, dimensions):
        self.width, self.height = dimensions
        pygame.init()
        self.surface = pygame.display.set_mode()
        self.surface = pygame.display.set_mode(
            self.surface.get_size(),
            pygame.RESIZABLE
        )
        pygame.display.set_caption(caption)

    @staticmethod
    def check_user_quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def translateXY(self, pos):
        x, y = pos
        actual_width, actual_height = self.surface.get_size()
        return x / self.width * actual_width, y / self.height * actual_height

    def normalize_measurement(self, measurement):
        return min(self.translateXY((measurement, measurement)))

    def clear_screen(self):
        self.surface.fill((0, 0, 0))

    @staticmethod
    def update():
        pygame.display.update()
