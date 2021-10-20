from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x625')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
score = 0
objects = []
canv.pack(fill=BOTH, expand=1)
l = Label(root, bg='black', fg='white', text=f'Score:{score}', width=20)
l.pack()
name = None


colors = ['red', 'orange', 'yellow', 'blue', 'green', 'black']


def main():
    """
    Главная функция программы. Запускает процесс игры.
    :return:
    """
    new_name()
    if name:
        canv.delete(ALL)
        all_balls()


def all_balls():
    """
    Регулирует количество шариков и орисовывает все шарики.
    :return:
    """
    canv.delete(ALL)
    if len(objects) < 10:
        objects.append(new_ball())
    else:
        for i in range(len(objects)):
            r = objects[i][2]
            res = move(objects[i][0], objects[i][1], r, objects[i][3])
            color = objects[i][4]
            x, y, direction = res[0], res[1], res[2]
            objects.pop(i)
            objects.insert(i, (x, y, r, direction, color))
            if color == 'black':
                draw_bomb(x, y, r, color)
            else:
                canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
    root.after(50, all_balls)


def new_ball():
    """
    Создает новый шарик
    :return: возвращает парамтры шарика: абсцисса,
     ордината, радиус, направление движения и цвет
    """
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    color = choice(colors)
    direction = rnd(1, 4)
    return x, y, r, direction, color


def move(x, y, r, direction):
    """
    Вычисляет координаты шарика после единичного передвижения.
    :param x: абсцисса шарика
    :param y: ордината шарика
    :param r: радиус шарика
    :param direction: направление движения шарика
    :return: новые координаты и новое направление движения.
    """
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


def draw_bomb(x, y, r, color):
    canv.create_oval(x - r, y - r, x + r, y + r, fill=color)
    canv.create_rectangle(x + r // 2, y - r, x + r // 2 + 20, y - r + 20, fill='red')
    canv.create_line(x + r // 2 + 20, y - r, x + r, y - r - 20, x + r + 20, y - r, smooth=1)

    # img = ImageTk.PhotoImage(Image.open('bomb.png'))
    # panel = Label(root, image=img, width=81, height=8).place(x=x, y=y, width=81, height=83)
    # panel.pack()
    # canv.image.gird(row=0, column=0)


def click(event):
    """
    обрабаывает событие клика мышки.
    В случае попадания по шарику удаляет его и увеличивает счет.
    Если шарик оказался бомбой, счет обнуляется, шарики создаются заново.
    :param event: событие клика мышки
    :return:
    """
    global score, objects, name
    x1, y1 = event.x, event.y
    i = 0
    while i < len(objects):
        x, y, r, color = objects[i][0], objects[i][1], objects[i][2], objects[i][4]
        if (x1 - x) ** 2 + (y1 - y) ** 2 <= r ** 2:
            if color == 'black':
                canv.delete(ALL)
                save_results(score)
                score = 0
                name = None
                objects = []
                break
            else:
                score += 1
                objects.pop(i)
                i += 1
        i += 1
    l.config(text=f'Score:{score}')
    l.pack()


def new_name():
    global name

    def set_name():
        global name
        name = message.get()
        print(name, score)

    message = StringVar()
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text='Введите имя игрока') \
        .pack(expand=1)
    message_entry = Entry(canv, textvariable=message)
    message_entry.place(relx=.5, rely=.1, anchor="c")
    message_button = Button(text="Задать имя", command=set_name)
    message_button.place(relx=.5, rely=.5, anchor="c")
    a.destroy()
    #canv.bind('<Button-2>', set_name)



def save_results(numb):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(name + '  ' + str(numb) + '\n')
    new_name()


main()
canv.bind('<Button-1>', click)
root.mainloop()
