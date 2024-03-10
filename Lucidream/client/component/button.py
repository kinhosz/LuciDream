import pygame
from typing import Tuple
from .text import Text
from .helper import parseClassName, applyOptions, optionsPermitted
from ...constants import DEFAULT_OPTIONS, Action

class Button:
    def __init__(self, className: str, text: Text, handle: dict):
        self._options = parseClassName(className)
        self._text = text
        self._handle = handle
        self._clickableArea: pygame.Rect = None

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
        self._clickableArea = pygame.Rect(left, top, width, height)
        
        pygame.draw.rect(screen, validOptions['bgColor'], self._clickableArea, 0)

        self._text.render(
            screen,
            resolution,
            (left, top),
            (width/validOptions['cols'], height/validOptions['rows']),
            optionsPermitted(validOptions)
        )
    
    def click(self, mousePos: Tuple[int, int]) -> dict:
        if mousePos[0] >= self._clickableArea.left and mousePos[0] <= self._clickableArea.right and \
            mousePos[1] >= self._clickableArea.top and mousePos[1] <= self._clickableArea.bottom:
            
            return self._handle
        
        return {'action': Action.NONE, 'resource': None}
