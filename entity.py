from typing import Tuple


class Entity:  # a generic object to hold the player, enemies, items, etc.
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):  # x position, y position, the character used to represent the entity, and color
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
