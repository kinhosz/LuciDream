from .choice import Choice
from typing import List

class Scene():
    def __init__(self, name: str, description: int, img: str):
        self._name: str = name
        self._description: int = description
        self._img: str = img
        self._choices: List[Choice] = []
    
    def getName(self) -> str:
        return self._name
    
    def getDescription(self) -> int:
        return self._description
    
    def getImg(self) -> str:
        return self._img
    
    def getChoiceSizes(self) -> int:
        return len(self._choices)

    def addChoice(self, description: str, nextScene: int) -> None:
        choice = Choice(description, nextScene)
        self._choices.append(choice)
    
    def getChoice(self, choiceId: int) -> Choice:
        return self._choices[choiceId]
