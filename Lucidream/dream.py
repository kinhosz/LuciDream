from .tools import Scene

class Dream:
    def __init__(self):
        self._scenes = []
        self._nameToId = {}
        self._mockeds = {}
    
    def _isMocked(self, name):
        return name in self._mockeds.keys()
    
    def _wasSceneAdded(self, name):
        return not self._isMocked(name) and name in self._nameToId.keys()
    
    def _validateUniqueName(self, name):
        if self._wasSceneAdded(name):
            raise ValueError("Duplicated scenes with the same name: {}".format(name))

    def _checkIfNameExist(self, name):
        if not self._wasSceneAdded(name):
            raise ValueError("Unknown scene name: {}".format(name))

    def _addMockedScene(self, name):
        sceneId = len(self._scenes)
        self._scenes.append(None)
        
        self._nameToId[name] = sceneId
        self._mockeds[name] = sceneId
        
        return sceneId
    
    def _clearMockedScene(self, name):
        if name in self._mockeds.keys():
            del self._mockeds[name]
    
    def _getSceneId(self, name):
        if not name in self._nameToId.keys():
            self._addMockedScene(name)
        
        return self._nameToId[name]

    def addScene(self, name, description, image):
        self._validateUniqueName(name)
    
        scene = Scene(name, description, image)    
        sceneId = self._getSceneId(name)
        
        self._clearMockedScene(name)

        self._scenes[sceneId] = scene
    
    def getScene(self, name):
        self._checkIfNameExist(name)
        sceneId = self._nameToId[name]
        return self._scenes[sceneId]

    def addChoice(self, parent, description, child):
        self._checkIfNameExist(parent)
        
        scene = self.getScene(parent)
        
        childId = self._getSceneId(child)
        scene.addChoice(description, childId)
