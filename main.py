import pygame


class Pathfinder:
    def __init__(self):
        pygame.init()
        self.scr_height = 600
        self.scr_width = 1000
        self.screen = pygame.display.set_mode((self.scr_width, self.scr_height))

    def run(self):
        while True:
            self._check_events()
            pygame.display.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break


if __name__ == '__main__':
    p = Pathfinder()
    p.run()
