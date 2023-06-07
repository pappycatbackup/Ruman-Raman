import pygame


class Config:
    def __init__(self):
        self.SCREENWIDTH = 1500
        self.SCREENHEIGHT = 900

        self.tile_size = 60
        self.row = self.SCREENHEIGHT // self.tile_size
        self.col = self.SCREENWIDTH // self.tile_size

        self.screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('CMGO-Version 0.0')

        # setup window
        self.clock = pygame.time.Clock()
        self.FPS = 60
