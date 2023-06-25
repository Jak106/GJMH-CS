import tkinter
import random

window = tkinter.Tk()
wdt = 1000
hdt = 1000
canvas = tkinter.Canvas(width=wdt, height=hdt, background="white")
canvas.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

boats = []

for x in range(1, 16):
    lodicka(30, 40*x)
    boats.append([30, 40*x])

race_is_on = True

racePos = []

while race_is_on:
    canvas.delete('all')
    for i in range(15):
        
        boats[i][0] = boats[i][0] + random.randint(1,10)
        lodicka(boats[i][0], boats[i][1])
        try:
            racePos[i] = [boats[i][0], boats[i][1]]
        except:
            racePos.append([boats[i][0], boats[i][1]])
    
    for x in range(15):
        if racePos[x][0] >= 950:
            race_is_on = False
            canvas.create_text(500, 500, text=f"Winner is boat {x+1}")

    canvas.create_line(950, 0, 950, 1000, fill="red", width=5)

    canvas.update()
    canvas.after(50)

window.mainloop()