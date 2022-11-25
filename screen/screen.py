import pygame


class Screen:
    def __init__(self, caption):
        pygame.init()
        self.surface = pygame.display.set_mode()
        self.width, self.height = self.surface.get_size()
        self.surface = pygame.display.set_mode(
            (self.width, self.height),
            pygame.RESIZABLE
        )
        pygame.display.set_caption(caption)

    @staticmethod
    def check_user_quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

