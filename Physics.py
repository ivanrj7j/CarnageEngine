import pygame
from Vector import Vector

class Physics():
    def __init__(self, object:pygame.Rect,collisionObjects:list, gravityScale=1, defaultGravityAccelaration=-9.81, mass = 1, airDrag = 0.2) -> None:
        self.object = object
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.velocity = Vector(0,0)
        self.mass = mass
        self.collisionObjects = collisionObjects
        self.acceleration = Vector(0,0)
        self.force = Vector(self.mass*self.acceleration.x, self.mass*self.acceleration.x)
        self.airDrag = 1-airDrag
        self.potentialEnergy = 0
        self.doesapplyGravity = True

    def applyGravity(self, deltaTime):
        self.force.y = ((self.gravityScale*self.defaultGravityAccelaration) * self.airDrag) * deltaTime
        self.calculateAccelaration(deltaTime)
        self.calculateVelocityandForce(deltaTime)
        self.move(deltaTime=deltaTime)
        
    def applyForce(self, deltaTime, considerMass = True):
        pass

    def move(self, deltaTime):
        self.object.x += self.velocity.x * deltaTime
        self.object.y += self.velocity.y * deltaTime
        # moving the object according to the velocity 

    def collision(self, dt):
        for collisionObject in self.collisionObjects: 
            if (self.object.bottom) >= collisionObject.y:
                self.doesapplyGravity = False
                self.acceleration = Vector(0,0)
                self.velocity = Vector(0,0)
                self.force = Vector(0,0)
                self.move(dt)
            else:
                self.doesapplyGravity = True

    def calculateVelocityandForce(self,deltaTime):
        self.velocity.x += self.acceleration.x * deltaTime
        self.velocity.y += self.acceleration.y * deltaTime
        # calculating the velocity (a = v/t)
        self.force.x = (self.acceleration.x*self.mass) * deltaTime
        self.force.y = (self.acceleration.y*self.mass) * deltaTime
        # calculating force (f=ma)

    def calculateAccelaration(self, deltaTime):
        self.acceleration = Vector((self.force.x / self.mass)*deltaTime, (self.force.y / self.mass) * deltaTime)
        # calculating accelaration (a = f/m)
        