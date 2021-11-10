import pygame
from pygame import color
from Physics import Physics
from Vector import Vector

class Entity(Physics):
    def __init__(self,superParent:pygame.display,parent, object:pygame.Rect,color:tuple,collisionObjects:list, centreOfMass:Vector,surface:pygame.Surface, gravityScale=1, defaultGravityAccelaration=9.81, mass = 1, doesapplyGravity = True, airDrag = 0.2, Kinematic=False, shouldUseColor=True) -> None:
        self.object = object
        self.surface = surface
        self.surfaceOriginal = self.surface
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
        self.kinematic = Kinematic
        self.kineticEnergy = 1
        self.centreOfMass = centreOfMass
        self.shouldUseColor = shouldUseColor
        self.rotation = 0
        # Initialising all the variables 

    def update(self, deltaTime, offset:Vector):
        if not self.kinematic:
            self.collision(deltaTime)
            if self.doesapplyGravity:
                self.applyGravity(deltaTime)
                # applying gravity  
        # applying all the forces to the object 

        if self.shouldUseColor:
            self.surface.fill(self.color)
            # filling the color 
        objectOffset = Vector(self.object.x + offset.x , self.object.y + offset.y)
        print(objectOffset)
        self.superParent.blit(self.surface, (objectOffset.x, objectOffset.y, self.object.width, self.object.height))
        # drawing the object 

        

        
        
    