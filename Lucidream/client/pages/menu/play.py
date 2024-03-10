from typing import Tuple
from pygame.surface import Surface
from ...component import Text, Div, Image, Button
from ....constants import RESOLUTIONS, Action, t
from ....tools import Scene

class Play:
    def __init__(self, screen: Surface, resolution: str):
        self._screen = screen
        self._res = resolution
        
        self._root = Div(
            "",
            Text("", "Continue")
        )

    def render(self, scene: Scene, **_):
        self._reload(scene)
        self._root.render(
            self._screen,
            self._res,
            (0, 0),
            RESOLUTIONS[self._res]
        )

    def onClick(self, mousePos: Tuple[int, int]) -> dict:
        return self._root.click(mousePos)

    def _reload(self, scene: Scene):
        rows = scene.getChoiceSizes() * 3 + 2
        offset = 1 + 2 * scene.getChoiceSizes()
        
        choices = []
        for i in range(scene.getChoiceSizes()):
            choices.append(
                Button(
                    "row-{} col-2".format(offset + i),
                    Text(
                        "text-size-16",
                        t(scene.getChoice(i).getDescription())
                    ),
                    {'action': Action.UPDATE_SCENE, 'resource': scene.getChoice(i).getNextScene()}
                )
            )
        
        self._root = Div(
            "grid-{}-5".format(rows),
            Image(
                "col-0-span-5 row-0-span-{}".format(rows),
                scene.getImg()
            ),
            Text(
                "col-2",
                t(scene.getDescription())
            ),
            *choices
        )
