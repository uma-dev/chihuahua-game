import json
import os
import pygame

from utils.constants import TILE_SIZE


class Level:
    TILE_MAPPING = {
        1: "grass.webp",
        2: "wall.png",
        3: "wall_top.png",
        4: "wall_flat.png",
        5: "grass_with_wall.webp",
        6: "ring.png",
    }

    def __init__(self, data):
        self.tile_data = data["tiles"]
        self.start_pos = tuple(data["start"])
        self.target = tuple(data["target"])
        self.ball_spawn = tuple(data["ball_spawn"])
        self.tiles = self._load_tiles()

    def _load_tiles(self):
        tiles = {}
        base_path = os.path.join("assets", "images", "tiles")
        for tile_id, filename in self.TILE_MAPPING.items():
            path = os.path.join(base_path, filename)
            image = pygame.image.load(path)
            if pygame.display.get_init():
                image = image.convert_alpha()
            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            tiles[tile_id] = image
        return tiles

    def draw(self, surface):
        for row_index, row in enumerate(self.tile_data):
            for col_index, tile_id in enumerate(row):
                if tile_id in self.tiles:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    surface.blit(self.tiles[tile_id], (x, y))


class LevelLoader:
    @staticmethod
    def load(filename: str) -> Level:
        with open(f"map/{filename}") as f:
            data = json.load(f)
        return Level(data)
