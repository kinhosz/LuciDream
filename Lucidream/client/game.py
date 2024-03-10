import pygame
import json
from .pages import Menu
from ..constants import RESOLUTIONS, Action, getAsset
from ..tools import Scene

class Game:
    def __init__(self):
        pygame.init()
        
        self._info = self._getInfo()
        self._resolution = self._info['resolution']
        self._screen = pygame.display.set_mode(RESOLUTIONS[self._resolution])
        self._clock = pygame.time.Clock()
        self._running = False
        self._page = Menu(self._screen, self._resolution)
     
    def run(self, **args) -> None:
        self._running = True
        
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._save(args['scene'])
                    self._running = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    response = self._page.onClick(pygame.mouse.get_pos())
                    
                    if response['action'] == Action.QUIT:
                        self._save(args['scene'])
                        self._running = False
                    
                    elif response['action'] == Action.RENDER:
                        self._page = response['resource']
                    
                    elif response['action'] == Action.UPDATE_SCENE:
                        args['scene'] = args['scenes'][response['resource']]
                    
                    elif response['action'] == Action.RESTART_SCENE:
                        self._save(args['start'])
                        args['scene'] = args['start']
                        self._page = response['resource']

            self._page.render(**args)
            
            pygame.display.flip()
            self._clock.tick(60)
        
        pygame.quit()

    def _save(self, scene: Scene) -> None:
        data = {
            'scene': scene.getName()
        }
        
        f = open("data.bin".format(getAsset()), "w")
        f.write(json.dumps(data))
        f.close()
    
    def _getInfo(self):
        path = getAsset() + "/logs.json"
        f = open(path, "r")
        info = json.loads(f.read())
        f.close()
        return info
