import pygame
from .pages import Menu
from .constants import RESOLUTIONS, Action

class Game:
    def __init__(self):
        pygame.init()
        
        self._resolution = 'hd'
        self._screen = pygame.display.set_mode(RESOLUTIONS[self._resolution])
        self._clock = pygame.time.Clock()
        self._running = False
        self._page = Menu(self._screen, self._resolution)
        
    def run(self) -> None:
        self._running = True
        
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    response = self._page.onClick(pygame.mouse.get_pos())
                    
                    if response['action'] == Action.QUIT:
                        self._running = False
                    
                    elif response['action'] == Action.RENDER:
                        self._page = response['resource']

            self._page.render()
            
            pygame.display.flip()
            self._clock.tick(60)
        
        pygame.quit()
