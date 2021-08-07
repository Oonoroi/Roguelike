import numpy as np
from tcod.console import Console
import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")  # makes an array full of floor tiles

        self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x: int, y: int) -> bool:  # returns true if both x and y are within the bounds of the map
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console):
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]