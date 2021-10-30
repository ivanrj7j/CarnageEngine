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
        self.airDrag = airDrag

    def applyGravity(self, deltaTime):
        self.force["x"] += self.force["x"]
        self.force["y"] += self.force["y"]
        self.applyForce(deltaTime=deltaTime, considerMass=False)

    def applyForce(self, deltaTime, considerMass = True):
        print(self.force["y"])
        if not considerMass:
            self.acceleration["x"] = ((self.force["x"] * (1-self.airDrag)) * deltaTime)
            self.acceleration["y"] = ((self.force["y"] * (1-self.airDrag)) * deltaTime)
            self.velocity["x"] += self.acceleration["x"]
            self.velocity["y"] += self.acceleration["y"]
        else:
            self.acceleration["x"] = (((self.force["x"]/self.mass)*(1-self.airDrag)) * deltaTime)
            self.acceleration["y"] = (((self.force["y"]/self.mass)*(1-self.airDrag)) * deltaTime)
            self.velocity["x"] += self.acceleration["x"]
            self.velocity["y"] += self.acceleration["y"]
        self.move(deltaTime=deltaTime)

    def move(self, deltaTime):
        self.object.x += self.velocity["x"] * deltaTime
        self.object.y += self.velocity["y"] * deltaTime

    def collision(self, deltaTime):
        for CollisionObject in self.collisionObjects:
            if (self.object.y + (self.object.height/2)) >= (CollisionObject.y):
                self.acceleration = {"x":0, "y":0}
                self.velocity = {"x":0, "y":0}
                self.force["x"] += -self.force["x"] * 2
                self.force["y"] += -self.force["y"] * 2

    def calculateForce(self):
        self.force = {"x" : self.mass*self.acceleration["x"], "y" : self.mass*self.acceleration["y"]}
        