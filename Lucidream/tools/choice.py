class Choice:
    def __init__(self, description: int, nextScene: int):
        self._description: int = description
        self._nextScene: int = nextScene
    
    def getDescription(self) -> int:
        return self._description
    
    def getNextScene(self) -> int:
        return self._nextScene
