import pygame
from typing import Tuple
from .helper import parseClassName, applyOptions

class Button:
    def __init__(self, className: str, *childs):
        self._options = parseClassName(className)
        self._childs = childs
        self._clickableArea: pygame.Rect = None

    def render(self, screen: pygame.Surface, resolution: str, start: Tuple[int, int], span: Tuple[int, int]) -> None:
        validOptions = applyOptions(resolution, self._options)
        
        left = start[0] + span[0] * validOptions['parentCol']
        top = start[1] + span[1] * validOptions['parentRow']
        width = span[0] * validOptions['parentColSpan']
        height = span[1] * validOptions['parentRowSpan']
        rect = pygame.Rect(left, top, width, height)
        
        self._clickableArea = pygame.draw.rect(screen, validOptions['bgColor'], rect, 0)

        for child in self._childs:
            child.render(
                screen,
                resolution,
                (left, top),
                (width/validOptions['cols'], height/validOptions['rows'])                
            )
