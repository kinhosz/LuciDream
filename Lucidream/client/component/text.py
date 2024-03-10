import pygame
from typing import Tuple
from .helper import parseClassName, applyOptions
from ...constants import DEFAULT_OPTIONS

class Text:
    def __init__(self, className: str, text: str):
        self._options = parseClassName(className)
        self._text = text

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
    
        font = pygame.font.Font(validOptions['textFont'], validOptions['textSize'])        
        text = font.render(self._text, True, validOptions['textColor'], validOptions['textBackground'])
        
        textRect = text.get_rect()
        textRect.center = (left + width//2, top + height//2)
        
        screen.blit(text, textRect)
