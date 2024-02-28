from .choice import Choice

class Scene():
    def __init__(self, name, description, img):
        self._name = name
        self._description = description
        self._img = img
        self._choices = []
    
    def getName(self):
        return self._name
    
    def getDescription(self):
        return self._description
    
    def getImg(self):
        return self._img

    def addChoice(self, description, nextScene):
        choice = Choice(description, nextScene)
        self._choices.append(choice)
    
    def getChoice(self, choiceId):
        return self._choices[choiceId]
