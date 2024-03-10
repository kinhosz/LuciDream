import pygame
from typing import Tuple
from .helper import parseClassName, applyOptions, optionsPermitted
from ...constants import DEFAULT_OPTIONS, Action
from .button import Button

class Div:
    def __init__(self, className: str, *childs):
        self._options = parseClassName(className)
        self._childs = childs

    def render(
        self, 
        screen: pygame.Surface, 
        resolution: str, 
        start: Tuple[int, int], 
        span: Tuple[int, int],
        parentOptions: dict = DEFAULT_OPTIONS.copy()
    ) -> None:
        
        validOptions = parentOptions.copy()
        validOptions.update(applyOptions(resolution, self._options))
        
        left = start[0] + span[0] * validOptions['parentCol']
        top = start[1] + span[1] * validOptions['parentRow']
        width = span[0] * validOptions['parentColSpan']
        height = span[1] * validOptions['parentRowSpan']
        rect = pygame.Rect(left, top, width, height)
        
        pygame.draw.rect(screen, validOptions['bgColor'], rect, 0)

        for child in self._childs:
            child.render(
                screen,
                resolution,
                (left, top),
                (width/validOptions['cols'], height/validOptions['rows']),
                optionsPermitted(validOptions)
            )

    def click(self, mousePos: Tuple[int, int]) -> dict:
        for child in self._childs:
            if isinstance(child, Button) or isinstance(child, Div):
                buttonAction = child.click(mousePos)
                
                if buttonAction['action'] != Action.NONE:
                    return buttonAction
        
        return {'action': Action.NONE, 'resource': None}
