#tkinter touchpad binds
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.pack()

def circle(coordinates):
    #print(coordinates)
    x = coordinates.x
    y = coordinates.y
    canvas.create_oval(x-5, y-5, x+5, y+5)
    
def house(coordinates):
    x = coordinates.x
    y = coordinates.y
    canvas.create_rectangle(x-5, y-5, x+5, y+5)
    canvas.create_line(x-5, y-5, x, y-10, x+5, y-5)

def bored(coordinates):
    x = coordinates.x
    y = coordinates.y
    canvas.create_oval(x-5, y-10, x+5, y+10)


canvas.bind('<Button-1>',circle)
canvas.bind('<Button-3>', house)
canvas.bind('<B1-Motion>', bored)
window.mainloop()