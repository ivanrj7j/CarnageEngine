import pygame
from pygame import color
from .Physics import Physics
from .Vector import Vector2
import math

"""
Still under development, full features not yet implemented
"""

class Entity(Physics):
    def __init__(self,superParent:pygame.display,parent, object:pygame.Rect,color:tuple,collisionObjects:list, centreOfMass:Vector2,surface:pygame.Surface, gravityScale=1, defaultGravityAccelaration=9.81, mass = 1, doesapplyGravity = True, airDrag = 0.2, Kinematic=False, shouldUseColor=True, isActive = True):
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
        self.velocity = Vector2(0,0)
        self.collisionObjects = collisionObjects
        self.airDrag = airDrag
        self.kinematic = Kinematic
        self.kineticEnergy = 1
        self.centreOfMass = centreOfMass
        self.shouldUseColor = shouldUseColor
        self.rotation = 0
        self.isActive = isActive
        # Initialising all the variables 

    def update(self, deltaTime, offset:Vector2, distance:float, cameraWidth:float, fov:float):
        if self.isActive:
            if distance < 0:
                d = ((1/distance) * -1) + 1
            elif distance == 0:
                d = 1
            else:
                d = distance
            
            if distance != 0:
                cameraDistance = d * cameraWidth
                # hypotenuse = math.sqrt((cameraDistance**2) + ((cameraWidth / 2)**2))
                # finding the hypotenuse of the imaginary triangle formed by the object and the camera
                base =  (2*cameraDistance) * math.tan(math.radians(fov / 2))
                # finding the base of the chord of the circle connecting 2 radius with 'fov' angle distance
                ratio = cameraWidth / base
                # finding the ratio of the sizes of the objects 


                newWidth = ratio * self.object.width
                newHieght = ratio * self.object.height
                newSurface = pygame.transform.scale(self.surface, (int(self.surface.get_width() * ratio), int(self.surface.get_height() * ratio)))
                # scaling up the object according to the camera

            if not self.kinematic:
                self.collision(deltaTime)
                if self.doesapplyGravity:
                    self.applyGravity(deltaTime)
                    # applying gravity  
            # applying all the forces to the object 

            if self.shouldUseColor:
                self.surface.fill(self.color)
                # filling the color 

            if distance != 0:
                objectOffset = Vector2((self.object.x * ratio) , (self.object.y * ratio) )
                self.superParent.blit(newSurface, (objectOffset.x, objectOffset.y, newWidth, newHieght))
            else:
                self.superParent.blit(self.surface, (self.object.x, self.object.y, self.object.width, self.object.height))
            # drawing the object 
    
    def toggleActive(self, *keyWordArguments:bool):
        if keyWordArguments:
            self.isActive = keyWordArguments[0]
        else:
            if self.isActive == True:
                self.isActive = False
            else:
                self.isActive = True

        

        
        
    