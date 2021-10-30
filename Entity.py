import pygame
from Physics import Physics
from Vector import Vector

class Entity(Physics):
    def __init__(self,superParent:pygame,parent, object:pygame.Rect,color:tuple,collisionObjects:list, gravityScale=1, defaultGravityAccelaration=9.81, mass = 1, doesapplyGravity = True, airDrag = 0.2, Kinematic=False) -> None:
        self.object = object
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.mass = mass
        self.doesapplyGravity = doesapplyGravity
        self.color = color
        self.parent = parent
        self.superParent = superParent
        self.velocity = Vector(0,0)
        self.collisionObjects = collisionObjects
        self.airDrag = airDrag
        self.acceleration = Vector(0,0)
        self.force = Vector(self.mass*self.acceleration.x, self.mass*self.acceleration.x)
        self.kinematic = Kinematic

    def update(self, deltaTime):
        if not self.kinematic:
            self.collision(deltaTime)
            if self.doesapplyGravity:
                self.applyGravity(deltaTime=deltaTime)
                # applying gravity 
            self.collision(deltaTime)
            # applying collision 
        self.superParent.draw.rect(self.parent, self.color, self.object)
        # drawing the object 

        

        
        
    