import pygame
from .Vector import Vector2
from .Vector import calculateAngleBetweenTwoVectors
from .Vector import calculateDistanceBetweenTwoVectors
import math

"""
Still under development, full features not yet implemented
"""

class Physics():
    def __init__(self, object:pygame.Rect,collisionObjects:list, centreOfMass:Vector2,surface:pygame.Surface, gravityScale=1, defaultGravityAccelaration=-9.81, mass = 1, airDrag = 0.2) -> None:
        self.object = object
        self.surface = surface
        self.surfaceOriginal = self.surface
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.velocity = Vector2(0,0)
        self.mass = mass
        self.collisionObjects = collisionObjects
        self.airDrag = 1-airDrag
        self.potentialEnergy = 0
        self.doesapplyGravity = True
        self.kineticEnergy = 1
        self.centreOfMass = centreOfMass
        self.rotation = 0
        # Initialising all the variables 

    def applyGravity(self, dt):
        """
        Applies gravitational force to the object 
        """
        if self.doesapplyGravity:

            self.velocity += (0, self.defaultGravityAccelaration*self.gravityScale*self.airDrag)
            # accelarating object 

            self.object.x += self.velocity.x * dt
            self.object.y += self.velocity.y * dt
            # moving the object 
            #   calculating the motion 

            """
            Calculation of the rotation is behaving buggy, so I commented it out
            This would be implemented in the future
            """
            # radius = calculateDistanceBetweenTwoVectors(self.centreOfMass, Vector2(0, self.object.width / 2))
            # # calculating distance between centre of mass and top of the object 
            # force_applying = ((self.defaultGravityAccelaration*self.gravityScale*self.airDrag) * self.mass)
            # # calculating the force applied to the object 
            # angle = calculateAngleBetweenTwoVectors(self.centreOfMass, Vector2(0, self.object.width / 2))
            # # calculating the angle between centre of mass and top of the object 
            # # rotation = radius * force_applying * math.sin(angle) * (dt/60)
            # rotation_accelaration = (2*force_applying) / (self.mass * radius)
            # rotation = dt + ((rotation_accelaration / 2)*(dt**2)) * self.kineticEnergy
            # self.rotation = (self.rotation + rotation) % 360
            # # finding the rotation 
            # self.surface = self.rotate(self.surfaceOriginal, -self.rotation)
            # # rotating the object 

            # # calculating the rotation 
            
        
    def applyForce(self, dt ,force:Vector2, considerMass = True, kineticEnergy = 1, applyKineticEnergy = False):
        """Applies a force to the object"""

        if applyKineticEnergy:
            self.kineticEnergy = kineticEnergy
            # applies kinetic energy 

        if considerMass:
            self.velocity += force/self.mass
            # updating the velocity of the object 

            self.move(dt)
            # moving the object 

        else :
            self.velocity += force
            # updating the velocity of the object without considering the mass of the object 

            self.move(dt)
            # moving the object 
        

    def move(self, dt):
        """
        Moves the object with the current velocity
        """

        self.object.x += self.velocity.x * dt
        self.object.y += self.velocity.y * dt
        

    def collision(self, dt):
        """
        Handles collision
        """

        for collisionBody in self.collisionObjects:

            if self.object.bottom >= collisionBody.y:
                """
                does this every time when the bottom of the object is colliding with the
                top of any other object
                """

                self.velocity = Vector2(0,0)
                # setting the velocity to zero 

                self.doesapplyGravity = False
                # stopping the gravity force 

                if self.kineticEnergy <= 1 and self.kineticEnergy >=0:
                    self.kineticEnergy -= ((self.defaultGravityAccelaration*self.gravityScale*self.airDrag) * self.mass * self.object.height) / 1000
                    # reducing the kinetic energy of the object when in collides 

                    if self.kineticEnergy < 0:
                        self.kineticEnergy = 0
                        # stops the kinetic energy from going below zero
 
                force = Vector2(0,-(self.defaultGravityAccelaration*self.gravityScale*self.airDrag)) * self.mass * self.object.height / 5 
                force = Vector2(force.x * self.kineticEnergy, force.y * self.kineticEnergy)
                # calculating the reaction force 

                self.applyForce(force=force, considerMass=False, dt=dt)
                # applying the reaction force to the object 
                
            else:
                self.doesapplyGravity = True
                # makes the object affected by gravity when it is not collideed 

            if self.object.bottom >= collisionBody.y:
                self.object.y = collisionBody.y - self.object.height
                # stopping the overlaping of 2 object 

    def rotate(self, surface, angle):
        """Rotates the given surface with the given angle"""
        rotated_rect = pygame.transform.rotate(surface, angle)
        return rotated_rect