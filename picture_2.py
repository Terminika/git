import pygame
from pygame.draw import *
screen = pygame.display.set_mode((1600, 800))

rect(screen, '#afdafc', (0, 0, 1600, 400))
rect(screen, '#30ba8f', (0, 400, 1600, 800))
# boy
ellipse(screen, '#baacc7', (130, 250, 140, 350))
circle(screen, '#dcdcdc', (200, 200), 70)
# hands
line(screen, 'black', (160, 280), (80, 450))
line(screen, 'black', (240, 280), (400, 450))
# legs
line(screen, 'black', (160, 570), (100, 730))
line(screen, 'black', (100, 730), (70, 730))
line(screen, 'black', (240, 570), (300, 730))
line(screen, 'black', (300, 730), (330, 730))

# heart
line(screen, 'black', (80, 460), (80, 200))
polygon(screen, 'red', [(80, 250), (40, 150), (120, 145)])
circle(screen, 'red', (60, 145), 25)
circle(screen, 'red', (100, 145), 25)

# girl
polygon(screen, '#cf59b1', [(600, 230), (510, 600), (690, 600)])
circle(screen, '#dcdcdc', (600, 200), 70)
# hands
line(screen, 'black', (590, 280), (400, 450))
line(screen, 'black', (610, 280), (710, 380))
line(screen, 'black', (710, 380), (800, 280))
# legs
line(screen, 'black', (560, 600), (480, 730))
line(screen, 'black', (480, 730), (460, 730))
line(screen, 'black', (640, 600), (720, 730))
line(screen, 'black', (720, 730), (740, 730))


# girl2
polygon(screen, '#cf59b1', [(1000, 230), (910, 600), (1090, 600)])
circle(screen, '#dcdcdc', (1000, 200), 70)
# hands
line(screen, 'black', (1010, 280), (1200, 450))
line(screen, 'black', (890, 380), (990, 280))
line(screen, 'black', (800, 280), (890, 380))
# legs
line(screen, 'black', (960, 600), (880, 730))
line(screen, 'black', (880, 730), (860, 730))
line(screen, 'black', (1040, 600), (1120, 730))
line(screen, 'black', (1120, 730), (1140, 730))

# ice cream
line(screen, 'black', (800, 300), (800, 200))
polygon(screen, 'yellow', [(800, 460 - 250), (750, 360 - 250), (850, 360 - 250)])
circle(screen, 'red', (825, 340 - 250), 25)
circle(screen, 'brown', (775, 340 - 250), 25)
circle(screen, 'white', (800, 300 - 250), 25)


# boy2
ellipse(screen, '#baacc7', (1270, 250, 140, 350))
circle(screen, '#dcdcdc', (1340, 200), 70)
# hands
line(screen, 'black', (1380, 280), (1450, 450))
line(screen, 'black', (1300, 280), (1200, 450))
# legs
line(screen, 'black', (1300, 570), (1240, 730))
line(screen, 'black', (1240, 730), (1210, 730))
line(screen, 'black', (1380, 570), (1440, 730))
line(screen, 'black', (1440, 730), (1470, 730))

# ice cream
line(screen, 'black', (1450, 450), (1500, 300))
polygon(screen, 'yellow', [(1500, 300), (1470, 200), (1550, 220)])
circle(screen, 'red', (1490, 190), 25)
circle(screen, 'brown', (1530, 200), 25)
circle(screen, 'white', (1520, 155), 25)


FPS = 30
clock = pygame.time.Clock()
finished = False

pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
