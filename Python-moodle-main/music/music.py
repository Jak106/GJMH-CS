import tkinter
from tkinter.constants import ARC

root = tkinter.Tk()

canvas = tkinter.Canvas(root, bg="white", height = 1000, width = 1500)

def celfDusan():
    canvas.create_line(50, 250, 50, 200, 75, 200, smooth=1, width=5)
    canvas.create_line(75, 200, 100, 200, 100, 250, smooth=1, width=5)
    canvas.create_line(100, 250, 100, 300, 50, 300, smooth=1, width=5)
    canvas.create_line(50, 300, 0, 225, 50, 150, smooth=1, width=5)
    canvas.create_line(50, 150, 90, 122.5, 80, 75, smooth=1, width=5)
    canvas.create_line(80, 75, 80, 50, 70, 50, smooth=1, width=5)
    canvas.create_line(70, 50, 60, 50, 60, 75, smooth=1, width=5)
    canvas.create_line(60, 75, 60, 400, width=5)
    canvas.create_line(60, 400, 60, 425, 45, 425, smooth=1, width=5)
    canvas.create_line(45, 425, 30, 425, 30, 400, smooth=1, width=5)

def celfMine():
    originX = 750
    originY = 500
    size = 200
    canvas.create_line(originX, originY-size, originX, originY+size, width=3)
    canvas.create_arc(originX, originY-size-50, originX+100, originY-size+50, width=3, extent=180, style=ARC)
    canvas.create_line(originX+100, originY-size, originX+100, originY-size+100, originX, originY-50, width=3, smooth=True)
    canvas.create_arc(originX, originY-50, originX-100, originY+100, width=3, extent=180, start=90, style=ARC)

for y in range(400, 400+50*5, 50):
    canvas.create_line(0, y, 1500, y, fill="black", width=3)

celfDusan()

celfMine()

canvas.pack()
root.mainloop()