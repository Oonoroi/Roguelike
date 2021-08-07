# main is for setting up initial variables and instantiating objects
import tcod
from input_handlers import EventHandler
from entity import Entity
from engine import Engine
from game_map import GameMap


def main() -> None:
    screen_width = 80  # same grid system as pygame, quadrant IV on a graph
    screen_height = 50

    map_width = 80
    map_height = 50

    tileset = tcod.tileset.load_tilesheet("assets\\tileset.png", 32, 8, tcod.tileset.CHARMAP_TCOD)  # sets font to use

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2) - 5, int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2) + 5, int(screen_height / 2), "@", (255, 135, 0))
    entities = {npc, player}  # set (unordered list) of entities to pass to the engine to draw. I cannot add the same Entity instance to the set more than once, which enforces uniqueness

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(  # creates the screen
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # THIS IS THE BEGINNING OF THE GAME LOOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)  # sends events to the engine to be dispacted to the correct class in "actions.py"


if __name__ == "__main__":
    main()
