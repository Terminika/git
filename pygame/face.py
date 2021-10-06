import pygame
from pygame.draw import *
screen = pygame.display.set_mode((500, 500))

rect(screen, 'grey', (0, 0, 500, 500))
circle(screen, 'yellow', (250, 220), 200)
circle(screen, 'red', (170, 140), 50)
circle(screen, 'red', (350, 140), 30)
circle(screen, 'black', (170, 140), 25)
circle(screen, 'black', (350, 140), 15)
rect(screen, 'black', (150, 300, 200, 40))
polygon(screen, 'black', [(200, 120), (210, 100), (100, 60), (90, 80)])
polygon(screen, 'black', [(410, 60), (420, 80), (320, 120), (310, 100)])




FPS = 30
clock = pygame.time.Clock()
finished = False

pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
