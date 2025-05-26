import json
import os
import pygame

from utils.constants import TILE_SIZE


class Level:
    def __init__(self, data):
        self.tile_data = data["tiles"]
        self.start_pos = tuple(data["start"])
        self.ball_spawn = tuple(data["ball_spawn"])

        path = os.path.join("assets", "images", "tiles", "grass.webp")
        self.grass_tile = pygame.image.load(path).convert_alpha()
        self.grass_tile = pygame.transform.scale(
            self.grass_tile, (TILE_SIZE, TILE_SIZE)
        )

    def draw(self, surface):
        for row_index, row in enumerate(self.tile_data):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.grass_tile, (x, y))


class LevelLoader:
    @staticmethod
    def load(filename: str) -> Level:
        with open(f"map/{filename}") as f:
            data = json.load(f)
        return Level(data)
