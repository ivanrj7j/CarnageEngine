import pygame
from Physics import Physics

class Entity(Physics):
    def __init__(self,superParent:pygame,parent, object:pygame.Rect,color:tuple,collisionObjects:list, gravityScale=1, defaultGravityAccelaration=9.81, mass = 1, doesapplyGravity = True, airDrag = 0.2) -> None:
        self.object = object
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.mass = mass
        self.doesapplyGravity = doesapplyGravity
        self.color = color
        self.parent = parent
        self.superParent = superParent
        self.velocity = {"x":0, "y":0}
        self.collisionObjects = collisionObjects
        self.airDrag = airDrag
        self.acceleration = {"x":0, "y":0}
        self.force = {"x" : self.mass*self.acceleration["x"], "y" : self.mass*self.acceleration["y"]}

    def update(self, deltaTime):
        self.calculateForce()
        self.collision(deltaTime=deltaTime)
        if self.doesapplyGravity:
            self.applyGravity(deltaTime=deltaTime)
        self.superParent.draw.rect(self.parent, self.color, self.object)

        

        
        
    