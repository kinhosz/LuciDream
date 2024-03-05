from pygame.surface import Surface
from ...component import Text, Div
from ...constants import RESOLUTIONS
from typing import Tuple

class Play:
    def __init__(self, screen: Surface, resolution: str):
        self._screen = screen
        self._res = resolution
        
        self._root = Div(
            "",
            Text("", "Continue")
        )

    def render(self):
        self._root.render(
            self._screen,
            self._res,
            (0, 0),
            RESOLUTIONS[self._res]
        )

    def onClick(self, mousePos: Tuple[int, int]) -> dict:
        return self._root.click(mousePos)
