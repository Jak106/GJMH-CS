#generates text based on specified number

import tkinter as tk
import tkinter.font as tkf
import random

wd = 500
ht = 500

window = tk.Tk()

my_canvas = tk.Canvas(window, width=wd, height=ht)

#generate text in rows and columns specified

#wd = int(input("Width = "))
#ht = int(input("Height = "))
#timesX = int(input("How many columns do you want? "))
#timesY = int(input("How many rows do you want? "))

#xAdd = wd/timesX
#yAdd = ht/timesY

#x = xAdd/2

#while x < ht:
#    y = yAdd/2
#    while y < wd:
#        my_canvas.create_text(x, y, text="Python", font="Arial")
#        y += yAdd
#    x += xAdd

#generates as much text as possible so that it doesn't overlap

used = []

for i in range(10):
    x = 200#random.randint(0, 500)
    y = random.randint(0, 500)
    for coordinate in used:
        while y > coordinate[1]-(tkf.Font(font="Arial").metrics('linespace')/2) and y < coordinate[1]+(tkf.Font(font="Arial").metrics('linespace')/2):
            y = random.randint(0, 500)
            print(y)
    my_canvas.create_text(x, y, text="Python", font="Arial")
    #label = tk.Label(text="Python", font="Arial")
    #label.pack()
    #print(label.winfo_width())
    used.append([x, y])
    print(used)
#my_canvas.create_line(250, 250, 290, 250)
#my_canvas.create_line(250, 250+(tkf.Font(font="Arial").metrics('linespace')/2), 300, 250+(tkf.Font(font="Arial").metrics('linespace')/2))



my_canvas.pack()
tk.mainloop()
