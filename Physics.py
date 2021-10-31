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
        self.airDrag = 1-airDrag
        self.potentialEnergy = 0
        self.doesapplyGravity = True
        self.kineticEnergy = 1

    def applyGravity(self, dt):
        if self.doesapplyGravity:
            self.velocity += (0, self.defaultGravityAccelaration*self.gravityScale*self.airDrag)
            self.object.x += self.velocity.x * dt
            self.object.y += self.velocity.y * dt

        
    def applyForce(self, dt ,force:Vector, considerMass = True, kineticEnergy = 1, applyKineticEnergy = False):
        if applyKineticEnergy:
            self.kineticEnergy = kineticEnergy
        if considerMass:
            self.velocity += force/self.mass
            self.move(dt)
        else :
            self.velocity += force
            self.move(dt)

    def move(self, dt):
        self.object.x += self.velocity.x * dt
        self.object.y += self.velocity.y * dt
        

    def collision(self, dt):
        for collisionBody in self.collisionObjects:
            if self.object.bottom >= collisionBody.y:
                self.velocity = Vector(0,0)
                self.doesapplyGravity = False
                if self.kineticEnergy <= 1 and self.kineticEnergy >=0:
                    self.kineticEnergy -= ((self.defaultGravityAccelaration*self.gravityScale*self.airDrag) * self.mass * self.object.height) / 1000
                    if self.kineticEnergy < 0:
                        self.kineticEnergy = 0
                force = Vector(0,-(self.defaultGravityAccelaration*self.gravityScale*self.airDrag)) * self.mass * self.object.height / 5 
                force = Vector(force.x * self.kineticEnergy, force.y * self.kineticEnergy)
                self.applyForce(force=force, considerMass=False, dt=dt)
            else:
                self.doesapplyGravity = True
    def calculateVelocityandForce(self,dt):
        pass

    def calculateAccelaration(self, dt):
       pass