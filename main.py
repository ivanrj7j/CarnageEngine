from math import trunc
import pygame
import time
from CarnageEngine.Vector import Vector
from CarnageEngine.Entity import Entity
from CarnageEngine.InputControl import hasInput
from CarnageEngine.Camera import Camera
# importing dependencies 

pygame.init()
# initilising pygame 
displayResoultion = (500, 600)
# setting the resolution of the screen 
FPS = 60
# defining the default fps rate of the game 
DefaultGravity = 9.80665
# defining the default gravity of the scene 


screen = pygame.display.set_mode(displayResoultion)
# initalising the display 
pygame.display.set_caption("Physics Engine?")
# setting the title 
borderLine = pygame.Rect(0, displayResoultion[1], displayResoultion[0], 50)
collisionObjects = [borderLine]
rectBoi = Entity(object=pygame.Rect(30, 30, 80, 45), color=(0,255,255), parent=screen, superParent=screen, gravityScale=1, collisionObjects=collisionObjects, defaultGravityAccelaration=9.80665, centreOfMass=Vector(30,30), surface=pygame.Surface((80,45)), shouldUseColor=True)
# the default square 

defaultCamera = Camera(Vector(20,0), screen)

def drawing(deltatime, entityList):
    defaultCamera.update(entityList, deltatime)

def jump(entity:Entity, dt):
    entity.applyForce(dt, Vector(0.5, -50), applyKineticEnergy=True)

def inputControls(key, dt):
    if key == pygame.K_SPACE:
        jump(rectBoi, dt)

def main():
    deltaTime = 0
    running = True
    clock = pygame.time.Clock()
    previousFrame = time.time()
    while running:
        clock.tick(FPS)
        deltaTime = (time.time() - previousFrame) * 60
        previousFrame = time.time()
        # updating deltaTime 

        drawing(deltatime=deltaTime, entityList=[rectBoi])
        # drawing everything 

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                inputControls(event.key, deltaTime)


    pygame.quit()

main()