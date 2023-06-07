import pygame

# initializes pygame video
pygame.init()

from config import Config
from render import fill_tile_map, draw_clouds

config = Config()

running = True


def main():
    global running

    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        config.screen.fill("blue")

        # draws the tile map
        fill_tile_map()

        # draws the cloud textures
        draw_clouds()

        # updates display
        pygame.display.update()
        config.clock.tick(config.FPS)

    pygame.quit()


main()
