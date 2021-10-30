import pygame

class Physics():
    def __init__(self, object:pygame.Rect,collisionObjects:list, gravityScale=1, defaultGravityAccelaration=-9.81, mass = 1, airDrag = 0.2) -> None:
        self.object = object
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.velocity = {"x":0, "y":0}
        self.mass = mass
        self.collisionObjects = collisionObjects
        self.acceleration = {"x":0, "y":0}
        self.force = {"x" : self.mass*self.acceleration["x"], "y" : self.mass*self.acceleration["y"]}
        self.airDrag = 1-airDrag
        self.pendingForce = 0

    def applyGravity(self, deltaTime):
        self.acceleration["x"] = (self.defaultGravityAccelaration * self.gravityScale) * self.airDrag
        self.acceleration["y"] = (self.defaultGravityAccelaration * self.gravityScale) * self.airDrag
        
    def applyForce(self, deltaTime, considerMass = True):
        pass

    def move(self):
        self.object.x += self.velocity["x"]
        self.object.y += self.velocity["y"]
        # moving the object according to the velocity 

    def collision(self, deltaTime):
        pass

    def calculateVelocityandForce(self,deltaTime):
        self.velocity["x"] += self.acceleration["x"] * deltaTime
        self.velocity["y"] += self.acceleration["y"] * deltaTime
        # calculating the velocity (a = v/t)
        self.force["x"] = (self.acceleration["x"]*self.mass) * deltaTime
        self.force["y"] = (self.acceleration["y"]*self.mass) * deltaTime
        # calculating force (f=ma)
        