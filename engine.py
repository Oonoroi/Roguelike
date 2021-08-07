# engine is for drawing map and entities to screen and handling events
from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]):
        for event in events:
            action = self.event_handler.dispatch(event)  # gets whatever action is currently being preformed, dispatch sends the event to its proper action

            if action is None:
                continue

            action.perform(self, self.player)  # preforms the correct action from actions.py

    def render(self, console: Console, context: Context) -> None:  # draws each entity form the entity set onto the console
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)  # updates the screen

        console.clear()
