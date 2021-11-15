"""
This file is just for debugging, ignore this file.
This file would be removed when the first version is released.
You can use this as a guid on how to use the game engine
"""
import pygame
import time

from pygame import Color, image
from CarnageEngine.Vector import Vector2, Vector3
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
rectBoi = Entity(object=pygame.Rect(30, 30, 160, 90), color=(0,255,255), parent=screen, superParent=screen, gravityScale=1, collisionObjects=collisionObjects, defaultGravityAccelaration=9.80665, centreOfMass=Vector2(30,30), surface=pygame.Surface((160,90)), shouldUseColor=True)
# the default square 

defaultCamera = Camera(Vector3(0, 0, 0), screen, Color(50, 36, 69))
# initialising the main camera 

def drawing(deltatime, entityList):
    defaultCamera.update(entityList, deltatime)
    

def zoom(value = Vector3(0,0,0.01)):
    defaultCamera.positon += value

def inputControls(key, dt):
    if key == pygame.K_SPACE:
        zoom()
    if key == pygame.K_LSHIFT:
        zoom(Vector3(0,0,-0.01))
    if key == pygame.K_w:
        zoom(Vector3(0, -5, 0))
    if key == pygame.K_s:
        zoom(Vector3(0, 5, 0))
    if key == pygame.K_a:
        zoom(Vector3(-5, 0, 0))
    if key == pygame.K_d:
        zoom(Vector3(5, 0, 0))


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