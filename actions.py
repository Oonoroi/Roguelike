from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:  # whenever we have an "action" the user can perform, we'll create a class for it here
    def perform(self, engine: Engine, entity: Entity) -> None:  # This will be overwritten in every subsequent action subclass
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):  # checks if the entity is trying to go out of bounds
            return  # destination is out of bounds
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:  # check if the entity is trying to walk into a wall
            return  # destination is blocked

        entity.move(self.dx, self.dy)