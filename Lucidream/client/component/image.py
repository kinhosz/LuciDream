import pygame
from typing import Tuple
from .helper import parseClassName, applyOptions
from ..constants import DEFAULT_OPTIONS

class Image:
    def __init__(self, className: str, path: str):
        self._options = parseClassName(className)
        self._path = path

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
        
        img = pygame.image.load(self._path)
        transf_img = pygame.transform.scale(img, (width, height))
        position = (left, top)
        
        screen.blit(transf_img, position)
