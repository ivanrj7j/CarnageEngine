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

screen = pygame.display.set_mode(displayResoultion)
# initalising the display 

pygame.display.set_caption("Carnage Engine Tests")
# setting the title 

borderLine = pygame.Rect(0, displayResoultion[1], displayResoultion[0], 50)
# the bottom border line of the game for collision testing and its invisible btw

collisionObjects = [borderLine]
# list containing every collision object in the scene 

rectBoi = Entity(object=pygame.Rect(30, 30, 160, 90),
 color=(0,255,255),
  parent=screen,
   superParent=screen,
    gravityScale=1,
     collisionObjects=collisionObjects,
       centreOfMass=Vector2(30,30),
        surface=pygame.Surface((160,90)),
         shouldUseColor=True)
# the default square 

defaultCamera = Camera(Vector3(0, 0, 0), screen, Color(50, 36, 69))
# initialising the main camera 

def drawing(deltatime, entityList):
    """
    Draws the camera and every entity
    """
    defaultCamera.update(entityList, deltatime)
    

def zoom(value = Vector3(0,0,0.01)):
    """
    Change the camera position, just for testing purposes
    """
    defaultCamera.positon += value

def inputControls(key, dt):
    """
    Handles input
    """
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
    if key == pygame.K_v:
        defaultCamera.wiggle(4, min=-4)


def main():
    deltaTime = 0
    # deltaTime between this and last frame 

    running = True
    # returns true if the game is running 

    clock = pygame.time.Clock()
    # initialising the clock object

    previousFrame = time.time()
    # tracking the time of the previous frame 

    while running:
        """
        main game loop
        """
        clock.tick(FPS)
        # stabilising the FPS 

        deltaTime = (time.time() - previousFrame) * 60
        # updating the deltaTime 

        previousFrame = time.time()
        # updating the previous frame 

        drawing(deltatime=deltaTime, entityList=[rectBoi])
        # drawing everything 

        pygame.display.update()
        # updating the display 


        for event in pygame.event.get():
            """
            Event Listener
            """

            if event.type == pygame.QUIT:
                running = False
                # quitting the game when 'x' is pressed 

            elif event.type == pygame.KEYDOWN:
                inputControls(event.key, deltaTime)
                # updating the controls 

            keysPressed = pygame.key.get_pressed()
            # getting the keys pressed 

            if keysPressed[pygame.K_j]:
                defaultCamera.wiggle(min=-4, max= 4)
                # wiggling the camera and this is only for testing purposes btw 


    pygame.quit()
    # quitting the game after the game loop 

main()
# running the main loop 