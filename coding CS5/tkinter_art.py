#tkinter art
from random import *
import tkinter
from turtle import color

#wd = int(input("Widht: "))
#ht = int(input("Height: "))

canvas=tkinter.Canvas(bg='black',width=1200,height=1200)
canvas.pack()

x=10
y=10

for i in range(1,26):
    x=x+20
    y=y+20
    canvas.create_line(x,10,510,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)

x = 510
y = 10

for i in range(1,26):
    x=x-20
    y=y+20
    canvas.create_line(x, 510, 510,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)

x = 510
y = 510

for i in range(1,26):
    x=x-20
    y=y-20
    canvas.create_line(x,510, 10,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)
    print(x, y)


x = 510
y = 10

for i in range(1,26):
    x=x-20
    y=y+20
    canvas.create_line(x,10, 10,y,fill='white',width=2)
    canvas.update()
    canvas.after(100)


x1 = 520
y1 = 520

x2 = 10
y2 = 1040
#canvas.create_line(520, 10, 1040, 10, 1040, 520, 520, 520, 520, 10, fill="white")
#canvas.create_line(540, 10, 1040, 30, 1020, 520, 520, 500, 540, 10, fill="white")

for i in range(1):
    canvas.create_line(520, 10, 1040, 10, 1040, 520, 520, 520, 520, 10, fill="white")
#canvas.create_rectangle(520+20, 10, 1040-20, 520-20, outline="white")









canvas.mainloop()

