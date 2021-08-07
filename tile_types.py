from typing import Tuple
import numpy as np

graphic_dt = np.dtype(  # creates a new datatype made up of the character, the foreground color, and the background color
    [
        ("ch", np.int32),
        ("fg", "3B"),  # 3B = 3 bytes for rgb values
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # determines if entities can walk over the tile (yes for floor, no for walls)
        ("transparent", np.bool),  # determines if tile blocks FOV (no for floor, yes for solid walls)
        ("dark", graphic_dt),  # makes tile dark when out of view
    ]
)


def new_tile(  # creates an array containing a single tile, and returns it
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (100, 100, 100)))  # the first parameter is the character used to show that it's out of view, the third parameter is the actual color of the tile (practically speaking)

wall = new_tile(walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (255, 255, 255)))
