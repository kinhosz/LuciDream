from .tools import Scene
from .graph import dfs
from .client import Game
from typing import List, Dict

class Dream:
    def __init__(self):
        self._scenes: List[Scene] = []
        self._nameToId: Dict[str, int] = {}
        self._mockeds: Dict[str, int] = {}
    
    def _isMocked(self, name: str) -> bool:
        return name in self._mockeds.keys()
    
    def _wasSceneAdded(self, name: str) -> bool:
        return not self._isMocked(name) and name in self._nameToId.keys()
    
    def _validateUniqueName(self, name: str) -> None:
        if self._wasSceneAdded(name):
            raise ValueError("Duplicated scenes with the same name: {}".format(name))

    def _checkIfNameExist(self, name: str) -> None:
        if not self._wasSceneAdded(name):
            raise ValueError("Unknown scene name: {}".format(name))

    def _addMockedScene(self, name: str) -> int:
        sceneId = len(self._scenes)
        self._scenes.append(None)
        
        self._nameToId[name] = sceneId
        self._mockeds[name] = sceneId
        
        return sceneId
    
    def _clearMockedScene(self, name: str) -> None:
        if name in self._mockeds.keys():
            del self._mockeds[name]
    
    def _getSceneId(self, name: str) -> int:
        if not name in self._nameToId.keys():
            self._addMockedScene(name)
        
        return self._nameToId[name]
    
    def _checkSpectedScene(self, sceneName: str) -> None:
        scene_counter = 0
        for scene in self._scenes:
            if scene.getName() == sceneName:
                scene_counter += 1
        
        if scene_counter != 1:
            raise ValueError("Expected 1 scene {}. Founded {}".format(sceneName, scene_counter))
    
    def _hasDraftScenes(self) -> None:
        if len(self._mockeds.keys()) != 0:
            raise ValueError("You have {} draft scenes".format(self._mockeds.keys()))
    
    def _createAdjacentList(self) -> tuple[List[List[int]], List[int]]:
        graph = []
        mark = []
        for scene in self._scenes:
            adjacent = []
            mark.append(False)
            for i in range(scene.getChoiceSizes()):
                adjacent.append(
                    scene.getChoice(i).getNextScene()
                )
            graph.append(adjacent)
        
        return graph, mark
    
    def _hasDisconnectedScenes(self) -> None:
        graph, mark = self._createAdjacentList()
        dfs(graph, mark, 0)
        
        untouchedScenes: List[str] = []
        for i in range(len(mark)):
            if not mark[i]:
                untouchedScenes.append(
                    self._scenes[i].getName()
                )
        
        if len(untouchedScenes) != 0:
            raise ValueError("You have {} untouched scenes. They're: {}".format(
                len(untouchedScenes), untouchedScenes
            ))        
    
    def _checkValidHistory(self) -> None:
        self._checkSpectedScene('start')
        self._checkSpectedScene('end')
        self._hasDraftScenes()
        self._hasDisconnectedScenes()

    def addScene(self, name: str, description: str, image: str) -> None:
        self._validateUniqueName(name)
    
        scene = Scene(name, description, image)    
        sceneId = self._getSceneId(name)
        
        self._clearMockedScene(name)

        self._scenes[sceneId] = scene
    
    def getScene(self, name: str) -> Scene:
        self._checkIfNameExist(name)
        sceneId = self._nameToId[name]
        return self._scenes[sceneId]

    def addChoice(self, parent: str, description: str, child: str) -> None:
        self._checkIfNameExist(parent)
        
        scene = self.getScene(parent)
        
        childId = self._getSceneId(child)
        scene.addChoice(description, childId)
    
    def run(self) -> None:
        self._checkValidHistory()
        
        game = Game()
        game.run()
