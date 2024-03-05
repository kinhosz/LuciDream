from pygame.surface import Surface
from ..constants import RESOLUTIONS, Action
from typing import Tuple

from ..component import Div, Button, Text
from .menu import Languages, Play, NewGame

class Menu:
    def __init__(self, screen: Surface, resolution: str):
        self._screen = screen
        self._res = resolution

        self._root = Div(
            "bg-204-0-204 grid-8-8",
            Div(
                "bg-0-0-255 row-2-span-4 col-2-span-4 grid-5-1",
                Text(
                    "row-0 text-bg-0-0-255",
                    "Menu"
                ),
                Button(
                    "bg-0-0-255 row-1",
                    Text(
                        "bg-0-0-255",
                        "Continue"
                    ),
                    {'action': Action.RENDER, 'resource': Play(self._screen, self._res)}
                ),
                Button(
                    "bg-0-0-255 row-2",
                    Text(
                        "bg-0-0-255",
                        "New Game"
                    ),
                    {'action': Action.RENDER, 'resource': NewGame(self._screen, self._res)}
                ),
                Button(
                    "bg-0-0-255 row-3",
                    Text(
                        "bg-0-0-255",
                        "Languages"
                    ),
                    {'action': Action.RENDER, 'resource': Languages(self._screen, self._res)}
                ),
                Button(
                    "bg-0-0-255 row-4",
                    Text(
                        "bg-0-0-255",
                        "Quit"
                    ),
                    {'action': Action.QUIT, 'resource': None}
                )
            )
        )

    def render(self):
        self._root.render(
            self._screen,
            self._res,
            (0, 0),
            RESOLUTIONS[self._res],
        )
    
    def onClick(self, mousePos: Tuple[int, int]) -> dict:
        return self._root.click(mousePos)   
