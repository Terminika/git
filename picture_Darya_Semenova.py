import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 780))
rect(screen, (135, 206, 235), (0, 0, 600, 780))


def main():
    """
    Вызывает фунцию рисования картинки
    :return:
    """
    draw_picture()


def draw_picture():
    """
    Вызывает функции, необходимые для рисования картинки.
    :return:
    """
    mountains()
    grass()
    kust(400, 505, 3)
    kust(500, 700, 2)
    koza(200, 500, 6)
    koza(100, 500, 5)
    kust(150, 700, 4)


def mountains():
    """
    Рисует горы.
    :return:
    """
    polygon(screen, (169, 169, 169), (
        (0, 150), (50, 220), (100, 500), (150, 130), (220, 310), (240, 50), (320, 290), (420, 205), (460, 400),
        (500, 150),
        (550, 243), (600, 600), (600, 800), (0, 800)), width=0)
    aalines(screen, (0, 0, 0), True, (
        (0, 150), (50, 220), (100, 500), (150, 130), (220, 310), (240, 50), (320, 290), (420, 205), (460, 400),
        (500, 150),
        (550, 243), (600, 600), (600, 800), (0, 800)), blend=10000000)


def grass():
    """
    Рисует траву
    :return:
    """
    polygon(screen, (152, 251, 152), ((
        (0, 500), (100, 506), (230, 496), (280, 502), (320, 494), (420, 505), (460, 500), (500, 503), (520, 504),
        (600, 499),
        (600, 800), (0, 800))))

    aalines(screen, (0, 0, 0), True, (
        (0, 500), (100, 506), (230, 496), (280, 502), (320, 494), (420, 505), (460, 500), (500, 503), (520, 504),
        (600, 499),
        (600, 800), (0, 800), (500, 800), (0, 800)), blend=10000000)


def kust(x1, y1, size):
    """
    Рисует куст
    :param x1: абсцисса козы
    :param y1: ордината козы
    :param size: размер козы
    :return:
    """
    circle(screen, (0, 205, 0), (x1, y1), size * 30)

    for i in range(5):
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        ellipse(screen, (255, 255, 255),
                (x1 - size * 1 + size * i * a, y1 - size * 21 / 10 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1),
                (x1 - size * 1 + size * i * a, y1 - size * 21 / 10 + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 255),
                (x1 + size * 1 + size * i * a, y1 - size * 17 / 10 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1),
                (x1 + size * 1 + size * i * a, y1 - size * 17 / 10 + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 255), (x1 + size * 3 + size * i * a, y1 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1), (x1 + size * 3 + size * a * i, y1 + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 0), (x1 + size * i * a, y1 + size * i * b, size * 5, size * 3))
        ellipse(screen, (255, 255, 255), (x1 - size * 4 + size * i * a, y1 - size + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1), (x1 - size * 4 + size * i * a, y1 - size + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 255),
                (x1 + size * 3 + size * i * a, y1 + size * 2 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1), (x1 + size * 3 + size * i * a, y1 + size * 2 + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 255),
                (x1 - size * 7 / 2 + size * i * a, y1 + size * 4 / 3 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1),
                (x1 - size * 7 / 2 + size * i * a, y1 + size * 4 / 3 + size * i * b, size * 5, size * 3), 1)
        ellipse(screen, (255, 255, 255),
                (x1 - size * 1 + size * i * a, y1 + size * 21 / 10 + size * i * b, size * 5, size * 3))
        ellipse(screen, (1, 1, 1),
                (x1 - size * 1 + size * i * a, y1 + size * 21 / 10 + size * i * b, size * 5, size * 3), 1)


def koza(x, y, size):
    """
    Рисует козу.
    :param x: абсцисса середины козы
    :param y: ордината середины козы
    :param size: размер козы
    :return:
    """
    ellipse(screen, (255, 255, 255), (x, y, size * 22, size * 10))
    ellipse(screen, (255, 255, 255), (x + size * 18, y - size * 13, size * 6, size * 16))
    ellipse(screen, (255, 255, 255), (x + size * 20, y - size * 17, size * 9, size * 6))
    polygon(screen, (255, 255, 255),
            ((x + size * 20, y - size * 19), (x + size * 21, y - size * 15), (x + size * 23, y - size * 15)))
    polygon(screen, (255, 255, 255),
            ((x + size * 22, y - size * 19), (x + size * 23, y - size * 15), (x + size * 25, y - size * 15)))
    ellipse(screen, (138, 43, 226), (x + size * 22, y - size * 16, size * 4, size * 4))
    ellipse(screen, (0, 0, 0), (x + size * 23, y - size * 15, size * 2, size * 2))

    # legs
    ellipse(screen, (255, 255, 255), (x + size * 18, y + size * 6, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x + size * 3, y + size * 7, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x - size, y + size * 6, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x + size * 13, y + size * 6, size * 4, size * 10))

    ellipse(screen, (255, 255, 255), (x + size * 18, y + size * 16, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x + size * 3, y + size * 17, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x - size, y + size * 16, size * 4, size * 10))
    ellipse(screen, (255, 255, 255), (x + size * 13, y + size * 16, size * 4, size * 10))

    ellipse(screen, (255, 255, 255), (x + size * 19, y + size * 25, size * 5, size * 4))
    ellipse(screen, (255, 255, 255), (x + size * 4, y + size * 26, size * 5, size * 4))
    ellipse(screen, (255, 255, 255), (x - size, y + size * 25, size * 5, size * 4))
    ellipse(screen, (255, 255, 255), (x + size * 14, y + size * 25, size * 5, size * 4))


main()

pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
