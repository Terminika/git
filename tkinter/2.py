from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
score = 0
objects = []
canv.create_text(800, 100, text=f'Score:{score}', anchor=W)
canv.pack(fill=BOTH, expand=1)
l = Label(root, bg='black', fg='white', text=f'Score:{score}', width=20)
l.pack()


colors = ['red', 'orange', 'yellow', 'blue', 'green', 'black']


def all_balls():
    canv.delete(ALL)
    if len(objects) < 10:
        objects.append(new_ball())
        print('all new')
    else:
        for i in range(len(objects)):
            r = objects[i][2]
            res = move(objects[i][0], objects[i][1], r, objects[i][3])
            color = objects[i][4]
            x, y, direction = res[0], res[1], res[2]
            objects.pop(i)
            objects.insert(i, (x, y, r, direction, color))
            canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
    root.after(100, all_balls)


def move(x, y, r, direction):
    if direction == 1:
        if y - r <= 0 and x + r >= 800:
            direction = 3
        elif y - r <= 0 <= x + r <= 800:
            direction = 4
        elif 0 <= y - r <= y + r <= 600 and x + r >= 800:
            direction = 2
    elif direction == 2:
        if x - r - 2 <= 0 and y - r - 2 <= 0:
            direction = 4
        elif x - r - 2 <= 0:
            direction = 1
        elif y - r - 2 <= 0:
            direction = 3
    elif direction == 3:
        if x - r <= 0 and y + r >= 600:
            direction = 1
        elif x - r <= 0:
            direction = 4
        elif y + r >= 600:
            direction = 2
    elif direction == 4:
        if x + r >= 800 and y + r >= 600:
            direction = 2
        elif x + r >= 800:
            direction = 3
        elif y + r >= 600:
            direction = 1

    if direction == 1:
        x += 2
        y -= 2
    elif direction == 2:
        x -= 2
        y -= 2
    elif direction == 3:
        x -= 2
        y += 2
    else:
        x += 2
        y += 2
    return x, y, direction


def new_ball():
    """Функция создания нового шарика"""
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    color = choice(colors)
    direction = rnd(1, 4)
    return x, y, r, direction, color


def click(event):
    global score, objects
    x1, y1 = event.x, event.y
    i = 0
    while i < len(objects):
        x, y, r, color = objects[i][0], objects[i][1], objects[i][2], objects[i][4]
        if (x1 - x) ** 2 + (y1 - y) ** 2 <= r ** 2:
            if color == 'black':
                score = 0
                objects = []
                break
            else:
                score += 1
                objects.pop(i)
                i += 1
                print(x1, y1, score)
        i += 1
    l.config(text=f'Score:{score}')
    l.pack()

all_balls()
canv.bind('<Button-1>', click)
root.mainloop()
