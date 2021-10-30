import pygame
import time

from pygame import draw
from Entity import Entity
# importing dependencies 

pygame.init()
# initilising pygame 
displayResoultion = (500, 600)
# setting the resolution of the screen 
FPS = 60
# defining the default fps rate of the game 
DefaultGravity = 9.81
# defining the default gravity of the scene 


screen = pygame.display.set_mode(displayResoultion)
# initalising the display 
pygame.display.set_caption("Physics Engine?")
# setting the title 
borderLine = pygame.Rect(0, displayResoultion[1], displayResoultion[0], 50)
collisionObjects = [borderLine]
rectBoi = Entity(object=pygame.Rect(30, 30, 60, 60), color=(0,255,255), parent=screen, superParent=pygame, gravityScale=1/100, collisionObjects=collisionObjects)
# the default square 

def drawing(deltatime):
    screen.fill((255,255,255))
    # filling the screen 


    rectBoi.update(deltaTime=deltatime)
    # updating the rectangle 

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

        drawing(deltatime=deltaTime)
        # drawing everything 

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

main()