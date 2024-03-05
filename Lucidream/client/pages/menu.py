from pygame.surface import Surface
from ..constants import RESOLUTIONS

from ..component import Div, Button, Text

class Menu:
    def __init__(self, screen: Surface, resolution: str):
        self._screen = screen
        self._res = resolution

    def render(self):
        Div(
            "bg-204-0-204 grid-8-8",
            Div(
                "bg-0-0-255 row-2-span-4 col-2-span-4 grid-5-1",
                Text(
                    "bg-0-0-255 row-0",
                    "Título do jogo"
                ),
                Button(
                    "bg-0-0-255 row-1",
                    Text(
                        "bg-0-0-255",
                        "Continue"
                    )
                ),
                Button(
                    "bg-0-0-255 row-2",
                    Text(
                        "bg-0-0-255",
                        "New Game"
                    )
                ),
                Button(
                    "bg-0-0-255 row-3",
                    Text(
                        "bg-0-0-255",
                        "Languages"
                    )
                ),
                Button(
                    "bg-0-0-255 row-4",
                    Text(
                        "bg-0-0-255",
                        "Quit"
                    )
                )
            )
        ).render(
            self._screen,
            self._res,
            (0, 0),
            RESOLUTIONS[self._res],
        )
