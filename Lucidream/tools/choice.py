class Choice:
    def __init__(self, description: str, nextScene: int):
        self._description: str = description
        self._nextScene: int = nextScene
    
    def getDescription(self) -> str:
        return self._description
    
    def getNextScene(self) -> int:
        return self._nextScene
