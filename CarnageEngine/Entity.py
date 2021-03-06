import pygame
from pygame import color
from .Physics import Physics
from .Vector import *
import math

"""
Still under development, full features not yet implemented
"""

class Entity(Physics):
    def __init__(self,superParent:pygame.display,parent, object:pygame.Rect,color:tuple,collisionObjects:list, centreOfMass:Vector2,surface:pygame.Surface, gravityScale=1, defaultGravityAccelaration=9.80665, mass = 1, doesapplyGravity = True, airDrag = 0.2, Kinematic=False, shouldUseColor=True, isActive = True):
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
        """
        Does all the updating of physics, color, camera rendering and other stuff
        """
        if self.isActive:
            if distance < 0:
                d = (((1/(distance - 1))) * -1)
            else:
                d = distance + 1
            
            if distance != 0:
                cameraDistance = d * cameraWidth
                # finding the camera Distance 

                base =  (2*cameraDistance) * math.tan(math.radians(fov / 2))
                # finding the base of the chord of the circle connecting 2 radius with 'fov' angle distance

                ratio = (cameraWidth / base) / math.sin(math.radians(fov))
                # finding the ratio of the sizes of the objects 


                newWidth = ratio * self.object.width
                newHieght = ratio * self.object.height
                # updating the height and width for rendering in 

                newSurface = pygame.transform.scale(self.surface, (int(self.surface.get_width() * ratio), int(self.surface.get_height() * ratio)))
                # scaling up the object surface according to the camera

            if not self.kinematic:
                self.collision(deltaTime)
                # listening for collisions 

                if self.doesapplyGravity:
                    self.applyGravity(deltaTime)
                    # applying gravity  
            # applying all the forces to the object 

            if self.shouldUseColor:
                self.surface.fill(self.color)
                # filling the color 

            if distance != 0:
                objectOffset = Vector2( ( (self.object.x + offset.x) * ratio) , ( (self.object.y + offset.y) * ratio) )
                # calculating the object offset from its original position 

                self.superParent.blit(newSurface, (objectOffset.x, objectOffset.y, newWidth, newHieght))
                # blitting the object into the screen 
            else:
                objectOffset = Vector2( ( self.object.x + offset.x ) , ( self.object.y + offset.y) )
                # calculating the object offset from its original position 

                self.superParent.blit(self.surface, (objectOffset.x, objectOffset.y, self.object.width, self.object.height))
                # blitting the object into the screen 
    
    def toggleActive(self, *keyWordArguments:bool):
        """
        Changes the active state of the object on and off accordingly
        """

        if keyWordArguments:
            self.isActive = keyWordArguments[0]

        else:

            if self.isActive == True:
                self.isActive = False

            else:
                self.isActive = True      