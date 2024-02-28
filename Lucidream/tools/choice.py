class Choice:
    def __init__(self, description, nextScene):
        self._desciption = description
        self._nextScene = nextScene
    
    def getDescription(self):
        return self._desciption
    
    def getNextScene(self):
        return self._nextScene
