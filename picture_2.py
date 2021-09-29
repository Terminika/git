import pygame
from pygame.draw import *

screen = pygame.display.set_mode((1600, 800))

FPS = 30
clock = pygame.time.Clock()
finished = False
x_man_1, y_man_1 = 130, 250
x_man_2, y_man_2 = 1270, 250
x_girl_1, y_girl_1 = 600, 230
x_girl_2, y_girl_2 = 1000, 230
x_h, y_h = 80, 200
boys = False
girls = False
other = False


def main():
    global boys, girls, other
    fon()
    triugolniy_animation(x_girl_1, y_girl_1, True, x_girl_2, y_girl_2, False)
    girls = True
    ovalniy_man_animation(x_man_1, y_man_1, True, x_man_2, y_man_2, False)
    boys = True
    arm_animation(x_man_1, y_man_1, True, 0)
    heart_mashtab(x_h, y_h, 0)
    other = True
    fon()


def fon():
    """Рисует все объекты. Аргументов не принимает, ни от чего не зависит. Хорошая функция."""

    rect(screen, '#afdafc', (0, 0, 1600, 400))
    rect(screen, '#30ba8f', (0, 400, 1600, 800))

    if boys:
        ovalniy_man(x_man_1, y_man_1, True, 0)
        ovalniy_man(x_man_2, y_man_2, False, 0)
    if girls:
        triugolniy_man(x_girl_1, y_girl_1, True)
        triugolniy_man(x_girl_2, y_girl_2, False)
    if other:
        heart(x_h, y_h, 0)
        ice(800, 280)
        ice(1450, 430)


def ovalniy_man_animation(x1, y1, side1, x2, y2, side2):
    """
    Анимация мальчиков
    :param x1: абсцисса первого
    :param y1: ордината первого
    :param side1: местоположение первого
    :param x2: абсцисса второго
    :param y2: ордината второго
    :param side2: местоположение второго
    :return: None
    """
    for j in range(150):
        y1 = (y1 + 10)
        if y1 > 850:
            y1 = -800
        y2 = y2 - 10
        if y2 < -450:
            y2 = 1200
        ovalniy_man(x1, y1, side1, 0)
        ovalniy_man(x2, y2, side2, 0)
        pygame.display.update()
        clock.tick(50)
        fon()


def arm_animation(x, y, side, rotate):
    step = 1
    for i in range(100):
        if rotate > 20 or rotate < -20:
            step *= -1
        rotate += step
        ovalniy_man(x, y, side, rotate)
        pygame.display.update()
        clock.tick(50)
        fon()


def ovalniy_man(x, y, side, rotate):
    """Рисует овального человека по заданным координатам. Если переменная side == False, отразит его по вертикали. """

    ellipse(screen, '#baacc7', (x, y, 140, 350))
    circle(screen, '#dcdcdc', (x + 70, y - 50), 70)
    if side:
        if not rotate:
            line(screen, 'black', (x + 30, y + 30), (x - 50, y + 200))
            line(screen, 'black', (x + 110, y + 30), (x + 270, y + 200))
        else:
            line(screen, 'black', (x + 30, y + 30), (x - 50, y + 200))
            line(screen, 'black', (x + 110, y + 30), (x + rotate * 3 + 270, y + rotate * 7 + 200))
    else:
        line(screen, 'black', (x + 110, y + 30), (x + 180, y + 200))
        line(screen, 'black', (x + 30, y + 30), (x - 70, y + 200))
    line(screen, 'black', (x + 30, y + 320), (x - 30, y + 480))
    line(screen, 'black', (x - 30, y + 480), (x - 30 - 30, y + 480))
    line(screen, 'black', (x + 110, y + 320), (x + 170, y + 480))
    line(screen, 'black', (x + 170, y + 480), (x + 200, y + 480))


def triugolniy_animation(x1, y1, side1, x2, y2, side2):
    """
    Анимация девочек
    :param x1: абсцисса первой
    :param y1: ордината второй
    :param side1: местоположение первой
    :param x2: абсцисса второй
    :param y2: ордината второй
    :param side2: местоположение второй
    :return: None
    """
    k1 = -1
    k2 = +1
    for j in range(150):
        x1 = (x1 + 10 * k1)
        if x1 > 700 or x1 < 200:
            k1 *= -1
        x2 = x2 + 10 * k2
        if x2 > 1400 or x2 < 900:
            k2 *= -1
        triugolniy_man(x1, y1, side1)
        triugolniy_man(x2, y2, side2)
        pygame.display.update()
        clock.tick(50)
        fon()


def triugolniy_man(x, y, side):
    """Рисует треугольного человека по заданным координатам.
    Если переменная side == False, отразит его по вертикали. """
    k1 = 90  # подгоночный коэффициент 1
    k2 = 25  # подгоночный коэффициент 2
    if side:
        k3 = 10
        k4 = 200
        k5 = 110
    else:
        k3 = -10
        k4 = -200
        k5 = -110
    polygon(screen, '#cf59b1', [(x, y), (x - k1, y + 370), (x + k1, y + 370)])
    circle(screen, '#dcdcdc', (x, y - 30), 70)
    line(screen, 'black', (x - k3, y + 50), (x - k4, y + 220))
    line(screen, 'black', (x + k3, y + 50), (x + k5, y + 150))
    line(screen, 'black', (x + k5, y + 150), (x + k4, y + 50))
    line(screen, 'black', (x - k2, y + 370), (x - k2, y + 500))
    line(screen, 'black', (x - k2, y + 500), (x - k1, y + 500))
    line(screen, 'black', (x + k2, y + 370), (x + k2, y + 500))
    line(screen, 'black', (x + k2, y + 500), (x + k1, y + 500))


def heart_mashtab(x, y, k):
    """
    Анимация масштабирования сердца
    :param x: абсцисса сердца
    :param y: ордината сердца
    :param k: увеличивающий коэффициент
    :return: None
    """
    step = 0.015
    for i in range(50):
        if k > 0.2 or k < 0:
            step *= -1
        k += step
        heart(x, y, k)
        pygame.display.update()
        clock.tick(30)
        fon()


def heart(x, y, k):
    """
    Рисует сердце на верёвочке
    :param x: абсцисса сердца
    :param y: ордината сердца
    :param k: увличивающий коэффициент
    :return: None
    """
    delta_x = x * k
    delta_y = y * k
    delta_r = 25 * (k + 0.2)
    line(screen, 'black', (x, y + delta_y + 260), (x, y))
    polygon(screen, 'red', [(x, y + delta_y + 50), (x - delta_x - 40, y - delta_y - 50),
                            (x + delta_x + 40, y - delta_y - 50)])
    circle(screen, 'red', (x + - 20, y - delta_y - 50), 25 + delta_r)
    circle(screen, 'red', (x + 20, y - delta_y - 50), 25 + delta_r)


def ice(x1, y1):
    """рисует мороженое. На верёвочке. Принимает на вход его координаты"""
    line(screen, 'black', (x1, y1), (x1, y1 - 100))
    polygon(screen, 'yellow', [(x1, y1 - 90), (x1 - 50, y1 - 190), (x1 + 50, y1 - 190)])
    circle(screen, 'red', (x1 + 25, y1 - 200), 25)
    circle(screen, 'brown', (x1 - 25, y1 - 200), 25)
    circle(screen, 'white', (x1, y1 - 240), 25)


main()


pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True