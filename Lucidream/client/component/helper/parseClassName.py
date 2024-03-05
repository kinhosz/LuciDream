from typing import List

def parseClassName(className: str) -> List[List[str]]:
    raw_options = className.split(" ")
    
    options = []
    for raw in raw_options:
        options.append(raw.split("-"))
    
    return options
