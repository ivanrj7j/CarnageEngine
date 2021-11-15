import pygame
from pygame import color
from .Entity import Entity
from .Vector import Vector2
from .Vector import Vector3
from pygame.color import Color

class Camera():
    def __init__(self, position:Vector3 ,screen:pygame.display,  defaultBG = Color(255,255,255), active = True, fov=60):
        self.positon = position
        self.backGround = defaultBG
        self.active = active
        self.screen = screen
        self.fov = fov
    
    def toggleActive(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def update(self, Entities, dt):
        if self.active:
            self.screen.fill(self.backGround)
            cameraOffset = (self.positon.convertToVector2() - Vector2.zero()) * -1
            for entity in Entities:
                if type(entity) == Entity:
                    entity.update(dt, cameraOffset, self.positon.z, self.screen.get_width(), self.fov)
                if type(entity) == pygame.Rect:
                    entity.x += cameraOffset.x
                    entity.y += cameraOffset.y
            # updating the Entities 

    

