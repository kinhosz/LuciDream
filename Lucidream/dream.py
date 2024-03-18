from .constants import getAsset, isApp
from .tools import Scene
from .graph import dfs
from .client import Game
from typing import List, Dict
import json
from googletrans import Translator

class Dream:
    def __init__(self):
        self._scenes: List[Scene] = []
        self._nameToId: Dict[str, int] = {}
        self._mockeds: Dict[str, int] = {}
        self._texts: List[str] = []
        
        self._addDefaultTexts()
    
    def _addDefaultTexts(self):
        self._texts.append('Continue')
        self._texts.append('New Game')
        self._texts.append('Languages')
        self._texts.append('Exit')
    
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
    
    def _checkAssets(self) -> None:
        for scene in self._scenes:
            try:
                f = open(scene.getImg(), "r")
                f.close()
            except:
                raise ValueError("image \"{}\" Not Found".format(scene.getImg()))
    
    def _getCheckpoint(self) -> str:
        try:
            f = open("data.bin", "r")
            sceneName = json.loads(f.read())['scene']
            f.close()
            return sceneName
        except:
            return 'start'
    
    def _translate(self) -> None:
        f = open(getAsset() + "/logs.json", "r")
        langs = json.loads(f.read())['languages']
        f.close()
        
        translated = {}
        for lang in langs:
            translated[lang] = []
        
        translator = Translator()
        
        for text in self._texts:
            for lang in langs:
                src = translator.detect(text).lang
                try:
                    translation = translator.translate(text, src=src, dest=lang).text
                except:
                    print("Failed on translate \"{}\" for {}".format(text, lang))
                    translation = text
                translated[lang].append(
                    translation
                )
                print("base: {}, src: {}, dest: {}, trans: {}".format(text, src, lang, translation))
        
        f = open(getAsset() + "/texts.json", "w")
        f.write(json.dumps(translated))
        f.close()

    def addScene(self, name: str, description: str, image: str) -> None:
        self._validateUniqueName(name)
    
        image = getAsset() + "/" + image
    
        scene = Scene(name, len(self._texts), image)
        self._texts.append(description)    
        sceneId = self._getSceneId(name)
        
        self._clearMockedScene(name)

        self._scenes[sceneId] = scene
    
    def _getScene(self, name: str) -> Scene:
        self._checkIfNameExist(name)
        sceneId = self._nameToId[name]
        return self._scenes[sceneId]

    def addChoice(self, parent: str, description: str, child: str) -> None:
        self._checkIfNameExist(parent)
        
        scene = self._getScene(parent)
        
        childId = self._getSceneId(child)
        scene.addChoice(len(self._texts), childId)
        self._texts.append(description)
    
    def run(self) -> None:
        if not isApp():
            self._checkValidHistory()
            self._checkAssets()
            self._translate()
            return
        
        savedScene = self._getCheckpoint()
        
        game = Game()
        game.run(scenes=self._scenes, 
                 scene=self._getScene(savedScene),
                 start=self._getScene('start'))
