# engine is for drawing map and entities to screen and handling events
from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self, events: Iterable[Any]):
        for event in events:
            action = self.event_handler.dispatch(event)  # gets whatever action is currently being preformed, dispatch sends the event to its proper action

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.player.move(dx=action.dx, dy=action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:  # draws each entity form the entity set onto the console
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)  # updates the screen

        console.clear()
