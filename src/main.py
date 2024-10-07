import pygame
from os.path import join
from random import randint

#general setup of pygame
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Galaxy Flare')
running = True

#surface
sur = pygame.Surface((100, 200))
sur.fill('orange')
x = 100

#importing an image
player = pygame.image.load('../img/player.png').convert_alpha()
stars = pygame.image.load('../img/stars.png').convert_alpha()
galaxy = pygame.image.load('../img/galaxy.png').convert_alpha()
sun = pygame.image.load('../img/sun.png').convert_alpha()
lightStar1 = pygame.image.load('../img/lightStar1.png').convert_alpha()
lightStar2 = pygame.image.load('../img/lightStar2.png').convert_alpha()
space = pygame.image.load('../img/space.png').convert_alpha()

player = pygame.transform.scale(player, (100/1.8, 145/1.8))
stars = pygame.transform.scale(stars, (200, 200))
galaxy = pygame.transform.scale(galaxy, (WINDOW_WIDTH, WINDOW_HEIGHT))
sun = pygame.transform.scale(sun, (100, 100))
lightStar1 = pygame.transform.scale(lightStar1, (50, 50))
lightStar2 = pygame.transform.scale(lightStar2, (30, 30))
space = pygame.transform.scale(space, (WINDOW_WIDTH, WINDOW_HEIGHT))

ls1_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(5)]
ls2_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for j in range(5)]

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    display.fill('darkgray')
    display.blit(space, (0, 0))
    display.blit(galaxy, (0, 0))
    display.blit(sun, (0, 0))
    display.blit(lightStar1, (0, 0))
    display.blit(lightStar2, (50, 0))
    display.blit(stars, (0, 0))
    display.blit(stars, (198, 0))
    display.blit(stars, (198*2, 0))
    display.blit(stars, (198*3, 0))
    display.blit(stars, (0, 198))
    display.blit(stars, (198, 198))
    display.blit(stars, (198*2, 198))
    display.blit(stars, (198*3, 198))
    display.blit(stars, (0, 198*2))
    display.blit(stars, (198, 198*2))
    display.blit(stars, (198*2, 198*2))
    display.blit(stars, (198*3, 198*2))
    for pos in ls1_positions:
        display.blit(lightStar1, pos)
    for pos in ls2_positions:
        display.blit(lightStar2, pos)
    display.blit(player, (x, 0))

    pygame.display.update()

pygame.quit()
