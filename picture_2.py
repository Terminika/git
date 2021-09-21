import pygame
from pygame.draw import *
screen = pygame.display.set_mode((1600, 800))

rect(screen, '#afdafc', (0, 0, 1600, 400))
rect(screen, '#30ba8f', (0, 400, 1600, 800))
# boy
ellipse(screen, '#baacc7', (330 - 200, 250, 140, 350))
circle(screen, '#dcdcdc', (400 - 200, 200), 70)
line(screen, 'black', (360 - 200, 280), (280 - 200, 450))
line(screen, 'black', (440 - 200, 280), (600 - 200, 450))
line(screen, 'black', (360 - 200, 570), (300 - 200, 730))
line(screen, 'black', (300 - 200, 730), (270 - 200, 730))
line(screen, 'black', (440 - 200, 570), (500 - 200, 730))
line(screen, 'black', (500 - 200, 730), (530 - 200, 730))

# heart
line(screen, 'black', (80, 460), (80, 200))
polygon(screen, 'red', [(80, 250), (40, 150), (120, 145)])
circle(screen, 'red', (60, 145), 25)
circle(screen, 'red', (100, 145), 25)

# girl
polygon(screen, '#cf59b1', [(800 - 200, 230), (710 - 200, 600), (890 - 200, 600)])
circle(screen, '#dcdcdc', (800 - 200, 200), 70)
line(screen, 'black', (790 - 200, 280), (600 - 200, 450))
line(screen, 'black', (810 - 200, 280), (910 - 200, 380))
line(screen, 'black', (910 - 200, 380), (1000 - 200, 280))

line(screen, 'black', (760 - 200, 600), (680 - 200, 730))
line(screen, 'black', (680 - 200, 730), (660 - 200, 730))
line(screen, 'black', (840 - 200, 600), (920 - 200, 730))
line(screen, 'black', (920 - 200, 730), (940 - 200, 730))


# girl2
polygon(screen, '#cf59b1', [(1000, 230), (910, 600), (1090, 600)])
circle(screen, '#dcdcdc', (1000, 200), 70)
line(screen, 'black', (1010, 280), (1200, 450))
line(screen, 'black', (890, 380), (990, 280))
line(screen, 'black', (800, 280), (890, 380))

line(screen, 'black', (760 + 200, 600), (680 + 200, 730))
line(screen, 'black', (680 + 200, 730), (660 + 200, 730))
line(screen, 'black', (840 + 200, 600), (920 + 200, 730))
line(screen, 'black', (920 + 200, 730), (940 + 200, 730))

# ice cream
line(screen, 'black', (800, 300), (800, 200))
polygon(screen, 'yellow', [(800, 460 - 250), (750, 360 - 250), (850, 360 - 250)])
circle(screen, 'red', (825, 340 - 250), 25)
circle(screen, 'brown', (775, 340 - 250), 25)
circle(screen, 'white', (800, 300 - 250), 25)


# boy2
ellipse(screen, '#baacc7', (1270, 250, 140, 350))
circle(screen, '#dcdcdc', (1340, 200), 70)
line(screen, 'black', (1380, 280), (1450, 450))
line(screen, 'black', (1300, 280), (1200, 450))
line(screen, 'black', (360 + 940, 570), (300 + 940, 730))
line(screen, 'black', (300 + 940, 730), (270 + 940, 730))
line(screen, 'black', (440 + 940, 570), (500 + 940, 730))
line(screen, 'black', (500 + 940, 730), (530 + 940, 730))

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
