import pygame

"""
Yet to implement
"""

def hasInput(keys:dict, keysPressed):
    # keys format = key : [desired keys]
    everyKeysPressed = [] 
    for key in keys:
        if keysPressed == key:
            everyKeysPressed.append(True)
        else:
            return False
    
    for i in everyKeysPressed:
        if not i:
            return False
        else:
            pass
    return True

