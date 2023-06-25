#generates grass based on mousclick
import tkinter
from turtle import color, width

window = tkinter.Tk()
wdt = 500
hdt = 500
canvas = tkinter.Canvas(width=wdt, height=hdt, background="#baad6e")
canvas.pack()

def grass(coordinates):
    x = coordinates.x
    y = coordinates.y
    canvas.create_line(wdt/2, hdt-10, x, y, fill="green", width=2)

canvas.bind('<Button-1>', grass)
window.mainloop()