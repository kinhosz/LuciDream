from ...constants import RESOLUTIONS
from typing import List, Dict, Union, Tuple

def applyOptions(resolution: str, options: List[List[str]]) -> Dict[str, Union[Tuple[int, int, int], int]]:
    validOptions = {}
    
    for option in options:
        if len(option) == 0:
            continue
        
        index = 0
        
        if option[index] in RESOLUTIONS.keys() and option[index] == resolution:
            index += 1
        
        if index + 2 < len(option) and option[index] == "grid":
                validOptions['rows'] = int(option[index + 1])
                validOptions['cols'] = int(option[index + 2])
                continue
        
        if index + 3 < len(option) and option[index] == "bg":
            validOptions['bgColor'] = (
                int(option[index + 1]), 
                int(option[index + 2]), 
                int(option[index + 3])
            )
            continue
        
        if index + 1 < len(option) and option[index] == "row":
            validOptions['parentRow'] = int(option[index + 1])
            
            if index + 3 < len(option) and option[index + 2] == "span":
                validOptions['parentRowSpan'] = int(option[index + 3])
            continue
        
        if index + 1 < len(option) and option[index] == "col":
            validOptions['parentCol'] = int(option[index + 1])
            
            if index + 3 < len(option) and option[index + 2] == "span":
                validOptions['parentColSpan'] = int(option[index + 3])
            continue
    
    return validOptions
