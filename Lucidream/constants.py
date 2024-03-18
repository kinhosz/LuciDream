from enum import Enum
import os, sys
import json

RESOLUTIONS = {
    'hd': (1280, 720),
    'fullhd': (1920, 1080),
    '4k': (3840, 2160),
}

DEFAULT_OPTIONS = {
    'rows': 1,
    'cols': 1,
    'parentRow': 0,
    'parentCol': 0,
    'parentRowSpan': 1,
    'parentColSpan': 1,
    'bgColor': (255, 255, 255),
    'textFont': 'freesansbold.ttf',
    'textSize': 32,
    'textColor': (0, 255, 0),
    'textBackground': (0, 0, 128)
}

class Action(Enum):
    NONE = 1
    RENDER = 2
    QUIT = 3
    UPDATE_SCENE = 4
    RESTART_SCENE = 5
    SET_LANGUAGE = 6

def isApp():
    if not getattr(sys, 'frozen', False):
        return False
    return True

def getAsset():
    if not isApp():
        return 'assets'
    return os.path.join(sys._MEIPASS, 'assets')

TEXTS = None
LANG = 'en'

def t(id: int) -> str:
    global TEXTS
    
    if TEXTS == None:
        f = open(getAsset() + "/texts.json")
        TEXTS = json.loads(f.read())
        f.close()
    
    return TEXTS[LANG][id]

def setLang(lang):
    global LANG
    LANG = lang
