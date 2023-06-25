#generates random balls
import tkinter
import random

window = tkinter.Tk()
wdt = 1000
hdt = 1000
canvas = tkinter.Canvas(width=wdt, height=hdt, background="white")
canvas.pack()

def apple(x, y, fillCol):
    canvas.create_oval(x-50, y-50, x+50, y+50, fill=fillCol)

def player(x, y):
    canvas.crea

for i in range(5):
    apple(random.randint(100, 900), random.randint(100, 900), "red")
    
startPos = [500, 500]
apple(500, 500, "blue")
num = 1
while False:
    canvas.delete('all')
    num *= 100**10
    canvas.update()
    canvas.after(50)
canvas.bind()
window.mainloop()