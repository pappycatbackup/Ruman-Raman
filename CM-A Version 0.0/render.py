import pygame
from config import Config
import csv
import ast

config = Config()

# load and transform cloud texture
main_cloud_texture1 = pygame.image.load('Assets/Textures/Clouds/Cloud_3_A.png')
main_cloud_texture2 = pygame.image.load('Assets/Textures/Clouds/Cloud_1_H.png')
# main_cloud_texture = pygame.transform.scale(main_cloud_texture, (config.tile_size, config.tile_size))

# load and transform main sky texture 
main_sky_texture = pygame.image.load('Assets/Textures/Surfaces/Sky_1_B.png')
main_sky_texture = pygame.transform.scale(main_sky_texture, (config.tile_size, config.tile_size))

# load and transform dirt floor texture 
dirt_floor_texture = pygame.image.load('Assets/Textures/Surfaces/Dirt_B.png')
dirt_floor_texture = pygame.transform.scale(dirt_floor_texture, (config.tile_size, config.tile_size))

# load and transform grass floor texture 
grass_floor_texture = pygame.image.load('Assets/Textures/Surfaces/Grass_B.png')
grass_floor_texture = pygame.transform.scale(grass_floor_texture, (config.tile_size, config.tile_size))


# draws the cloud textures
def draw_clouds():
    x = 10 * config.tile_size
    y = 3 * config.tile_size

    width = 525
    height = 271

    # blit clouds to screen
    config.screen.blit(main_cloud_texture1, (x, y, width, height))
    config.screen.blit(main_cloud_texture2, (x - 600, y - 100, width, height))


def fill_tile_map():
    # writes to csv file tile location and value
    with open("tile_map.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in range(config.row):
            for col in range(config.col):
                tile_x = col * config.tile_size
                tile_y = row * config.tile_size

                tile_position = (tile_x // config.tile_size, tile_y // config.tile_size)

                grass_layers = 2
                dirt_layers = 1

                if (config.row - grass_layers) == row:
                    tile_value = 2
                elif (config.row - dirt_layers) == row:
                    tile_value = 1
                else:
                    tile_value = 0

                writer.writerow([str(tile_position), tile_value])  # Convert tile_position to a string

    # reads csv file and draws tiles
    with open("tile_map.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tile_position = ast.literal_eval(row[0])  # Convert the string back to a tuple
            x = tile_position[0] * config.tile_size
            y = tile_position[1] * config.tile_size
            tile_value = int(row[1])

            width = config.tile_size
            height = config.tile_size

            if tile_value == 0:
                config.screen.blit(main_sky_texture, (x, y, width, height))
            elif tile_value == 1:
                config.screen.blit(dirt_floor_texture, (x, y, width, height))
            elif tile_value == 2:
                config.screen.blit(grass_floor_texture, (x, y, width, height))

            # draw_map_grid(tile_position)


def draw_map_grid(tile_position):
    x = tile_position[0] * config.tile_size
    y = tile_position[1] * config.tile_size

    width = config.tile_size
    height = config.tile_size
    offset = 1

    pygame.draw.rect(config.screen, "white",
                     (x - offset, y - offset, width + 2, height + 2), 1)


# THIS CODE WORKS:
# tile_map = []
#
# def fill_tile_map():
#     for row in range(config.row):
#         for col in range(config.col):
#             tile_x = col * config.tile_size
#             tile_y = row * config.tile_size
#
#             tile_position = (tile_x // config.tile_size, tile_y // config.tile_size)
#
#             grass_layers = 2
#
#             if (config.row - grass_layers) > row:
#                 tile_value = 0
#
#             else:
#                 tile_value = 1
#
#             tile_map.append((tile_position, tile_value))
#
#         # Print only the tile_position
#         for tile in tile_map:
#             tile_position, _ = tile  # Extracting only the tile_position from the tuple
#             _, tile_value = tile     # Extracting only the tile_value from the tuple
#
#             print(tile_position, tile_value)
#
#             x, y = tile_position
#
#             x *= config.tile_size
#             y *= config.tile_size
#
#             width = config.tile_size
#             height = config.tile_size
#
#             offset = 2
#
#             # based on tile value draw texture
#             if tile_value == 0:
#                 pygame.draw.rect(config.screen, "blue", (x, y, width, height))
#
#             if tile_value == 1:
#                 pygame.draw.rect(config.screen, "brown", (x, y, width, height))
#
#             # Draw black empty rectangle offset
#             pygame.draw.rect(config.screen, "black",
#                              (x - offset, y - offset, width + 2 * offset, height + 2 * offset), 1)
#
# CODE DOES NOT WORK:
# def fill_tile_map():
#     half_row = config.row / 2  # Calculate half of the rows
#
#     # identify tile position and value
#     for row in range(config.row):
#         for col in range(config.col):
#             tile_x = col * config.tile_size
#             tile_y = row * config.tile_size
#
#             if row < half_row:
#                 tile_value = 0
#
#             else:
#                 tile_value = 1
#
#             tile_position_np = np.array([tile_x // config.tile_size, tile_y // config.tile_size]).flatten()
#             tile_value_np = np.array([tile_value]).flatten()
#
#             tile_map_np = np.array([
#
#                 *tile_position_np,
#                 *tile_value_np
#
#             ])
#
#             print(f"TILE POSITION: {tile_position_np}, TILE VALUE: {tile_value_np}")
#
#         # draw tiles
#         for tile in tile_map_np:
#             tile_position_np, _ = tile  # Extracting only the tile_position from the tuple
#             _, tile_value_np = tile     # Extracting only the tile_value from the tuple
#
#             x, y = tile_position_np
#
#             x *= config.tile_size
#             y *= config.tile_size
#
#             if tile_value == 0:
#                 width = config.tile_size
#                 height = config.tile_size
#                 pygame.draw.rect(config.screen, "blue", (x, y, width, height))
#
#             if tile_value == 1:
#                 width = config.tile_size
#                 height = config.tile_size
#                 pygame.draw.rect(config.screen, "brown", (x, y, width, height))
#
# CODE DOES NOT WORK:
# # append sky and grass tiles to texture lists
# for row in range(config.row):
#     for col in range(config.col):
#         if (config.row - 4) > row:
#             sky_tiles.append('sky_tile')
#             sky_tile_locations.append((col, row))
#         else:
#             grass_tiles.append('grass_floor_tile')
#             grass_tile_locations.append((col, row))
#
#
# CODE DOES NOT WORK:
# def draw_textures(screen):
#     for i in range(len(grass_tiles)):
#         if grass_tiles[i] == 'grass_floor_tile':
#             x = grass_tile_locations[i][0] * config.tile_size
#             y = grass_tile_locations[i][1] * config.tile_size
#             width = config.tile_size
#             height = config.tile_size
#             pygame.draw.rect(screen, "brown", (x, y, width, height))
#
#     for i in range(len(sky_tiles)):
#         if sky_tiles[i] == 'sky_tile':
#             x = sky_tile_locations[i][0] * config.tile_size
#             y = sky_tile_locations[i][1] * config.tile_size
#             width = config.tile_size
#             height = config.tile_size
#             pygame.draw.rect(screen, "blue", (x, y, width, height))
#
# CODE DOES NOT WORK:
# def draw_textures(screen):
#     for i in range(len(grass_tiles)):
#
#         if grass_tiles[i] == 'grass_floor':
#             screen.blit(grass_floor_texture, (grass_tile_locations[i][0] * tile.tile_size,
#                                               grass_tile_locations[i][1] * tile.tile_size))
