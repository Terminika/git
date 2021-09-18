import pygame
from pygame.draw import *
screen = pygame.display.set_mode((1200, 800))

rect(screen, '#afdafc', (0, 0, 1200, 400))
rect(screen, '#30ba8f', (0, 400, 1200, 800))
# boy
ellipse(screen, '#baacc7', (330, 250, 140, 350))
circle(screen, '#dcdcdc', (400, 200), 70)
line(screen, 'black', (360, 280), (280, 450))
line(screen, 'black', (440, 280), (600, 450))
line(screen, 'black', (360, 570), (300, 730))
line(screen, 'black', (300, 730), (270, 730))
line(screen, 'black', (440, 570), (500, 730))
line(screen, 'black', (500, 730), (530, 730))

polygon(screen, 'yellow', [(290, 460), (250, 380), (200, 420)])
circle(screen, 'red', (225, 380), 20)
circle(screen, 'brown', (200, 400), 20)
circle(screen, 'white', (190, 370), 20)

# girl
polygon(screen, '#cf59b1', [(800, 230), (710, 600), (890, 600)])
circle(screen, '#dcdcdc', (800, 200), 70)
line(screen, 'black', (790, 280), (600, 450))
line(screen, 'black', (810, 280), (920, 380))
line(screen, 'black', (920, 380), (1010, 280))

line(screen, 'black', (1000, 320), (1060, 200))
polygon(screen, 'red', [(1060, 200), (1100, 150), (1060, 145)])
circle(screen, 'red', (1070, 145), 15)
circle(screen, 'red', (1090, 145), 15)


line(screen, 'black', (760, 600), (680, 730))
line(screen, 'black', (680, 730), (660, 730))
line(screen, 'black', (840, 600), (920, 730))
line(screen, 'black', (920, 730), (940, 730))



FPS = 30
clock = pygame.time.Clock()
finished = False

pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
