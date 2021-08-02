import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80  # same grid system as pygame, quadrant IV on a graph
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet("assets\\tileset.png", 32, 8, tcod.tileset.CHARMAP_TCOD)  # sets font to use

    event_handler = EventHandler()

    with tcod.context.new_terminal(  # creates the screen
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:  # game loop
            root_console.print(x=player_x, y=player_y, string="@")  # prints the character to the screen

            context.present(root_console)  # updates the screen

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)  # gets whatever action is currently being preformed, dispatch sends the event to its proper action

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
