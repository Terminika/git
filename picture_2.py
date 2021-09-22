import pygame
from pygame.draw import *
screen = pygame.display.set_mode((1600, 800))

x = 130
y = 250
rect(screen, '#afdafc', (0, 0, 1600, 400))
rect(screen, '#30ba8f', (0, 400, 1600, 800))
# boy
ellipse(screen, '#baacc7', (x, y, 140, 350))
circle(screen, '#dcdcdc', (x + 70, y - 50), 70)
# hands
line(screen, 'black', (x + 30, y + 30), (x - 50, y + 200))
line(screen, 'black', (x + 110, y + 30), (x + 270, y + 200))
# legs
line(screen, 'black', (x + 30, 570), (x - 30, 730))
line(screen, 'black', (x - 30, 730), (x - 30 - 30, 730))
line(screen, 'black', (x + 110, 570), (x + 170, 730))
line(screen, 'black', (x + 170, 730), (x + 200, 730))

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

x1 = 800
y1 = 280
size = 25
# ice cream
line(screen, 'black', (x1, y1), (x1, y1 - 100))
polygon(screen, 'yellow', [(x1, y1 - 90), (x1 - 50, y1 - 190), (x1 + 50, y1 - 190)])
circle(screen, 'red', (x1 + 25, y1 - 200), size)
circle(screen, 'brown', (x1 - 25, y1 - 200), size)
circle(screen, 'white', (x1, y1 - 240), size)


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
