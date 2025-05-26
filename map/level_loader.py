import json
import os
import pygame

from utils.constants import TILE_SIZE


class Level:
    def __init__(self, data):
        self.tile_data = data["tiles"]
        self.start_pos = tuple(data["start"])
        self.ball_spawn = tuple(data["ball_spawn"])

        path_grass = os.path.join("assets", "images", "tiles", "grass.webp")
        self.grass_tile = pygame.image.load(path_grass).convert_alpha()
        self.grass_tile = pygame.transform.scale(
            self.grass_tile, (TILE_SIZE, TILE_SIZE)
        )

        path_wall = os.path.join("assets", "images", "tiles", "wall.png")
        self.wall_tile = pygame.image.load(path_wall).convert_alpha()
        self.wall_tile = pygame.transform.scale(self.wall_tile, (TILE_SIZE, TILE_SIZE))

        path_wall_top = os.path.join("assets", "images", "tiles", "wall_top.png")
        self.wall_top_tile = pygame.image.load(path_wall_top).convert_alpha()
        self.wall_top_tile = pygame.transform.scale(
            self.wall_top_tile, (TILE_SIZE, TILE_SIZE)
        )

        path_wall_flat = os.path.join("assets", "images", "tiles", "wall_flat.png")
        self.wall_flat_tile = pygame.image.load(path_wall_flat).convert_alpha()
        self.wall_flat_tile = pygame.transform.scale(
            self.wall_flat_tile, (TILE_SIZE, TILE_SIZE)
        )

        path_grass_wall = os.path.join(
            "assets", "images", "tiles", "grass_with_wall.webp"
        )
        self.grass_with_wall_tile = pygame.image.load(path_grass_wall).convert_alpha()
        self.grass_with_wall_tile = pygame.transform.scale(
            self.grass_with_wall_tile, (TILE_SIZE, TILE_SIZE)
        )

        path_ring = os.path.join("assets", "images", "tiles", "ring.png")
        self.ring_tile = pygame.image.load(path_ring).convert_alpha()
        self.ring_tile = pygame.transform.scale(self.ring_tile, (TILE_SIZE, TILE_SIZE))

    def draw(self, surface):
        for row_index, row in enumerate(self.tile_data):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.grass_tile, (x, y))
                elif tile == 2:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.wall_tile, (x, y))
                elif tile == 3:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.wall_top_tile, (x, y))
                elif tile == 4:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.wall_flat_tile, (x, y))
                elif tile == 5:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.grass_with_wall_tile, (x, y))
                elif tile == 6:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.ring_tile, (x, y))


class LevelLoader:
    @staticmethod
    def load(filename: str) -> Level:
        with open(f"map/{filename}") as f:
            data = json.load(f)
        return Level(data)
