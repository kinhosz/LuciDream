from pygame.surface import Surface
from ...component import Text, Div, Button
from ....constants import RESOLUTIONS, Action
from typing import Tuple

import math

class Languages:
    def __init__(self, screen: Surface, resolution: str):
        self._screen = screen
        self._res = resolution
        
        self._root = Div(
            "",
            Text("", "Languages")
        )
    
    def render(self, languages,**_):
        self._reload(languages)
        self._root.render(
            self._screen,
            self._res,
            (0, 0),
            RESOLUTIONS[self._res]
        )

    def onClick(self, mousePos: Tuple[int, int]) -> dict:
        return self._root.click(mousePos) 

    def _reload(self, languages):
        rows_c = int(math.ceil(math.sqrt(len(languages))))
        cols_c = int((len(languages) + rows_c - 1) // rows_c)
        
        buttons = []
        
        i = 0
        for r in range(rows_c):
            for c in range(cols_c):
                if i >= len(languages):
                    continue
                buttons.append(
                    Button(
                        "row-{} col-{}".format(r, c),
                        Text(
                            "",
                            languages[i]
                        ),
                        {'action': Action.SET_LANGUAGE, 'resource': languages[i]}
                    )
                )
                i += 1

        self._root = Div(
            "grid-" + str(int(rows_c)) + "-" + str(int(cols_c)),
            *buttons
        )
