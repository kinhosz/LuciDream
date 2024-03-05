import pygame
from typing import Tuple
from .helper import parseClassName, applyOptions

class Text:
    def __init__(self, className: str, text: str):
        self._options = parseClassName(className)
        self._text = text

    def render(self, screen: pygame.Surface, resolution: str, start: Tuple[int, int], span: Tuple[int, int]) -> None:
        validOptions = applyOptions(resolution, self._options)

        green = (0, 255, 0)
        blue = (0, 0, 128)
        
        left = start[0] + span[0] * validOptions['parentCol']
        top = start[1] + span[1] * validOptions['parentRow']
        width = span[0] * validOptions['parentColSpan']
        height = span[1] * validOptions['parentRowSpan']

        font = pygame.font.Font('freesansbold.ttf', 32)        
        text = font.render(self._text, True, green, blue)
        
        textRect = text.get_rect()
        textRect.center = (left + width//2, top + height//2)
        
        screen.blit(text, textRect)
