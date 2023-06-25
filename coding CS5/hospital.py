import tkinter

window = tkinter.Tk()
wdt = 450
hdt = 500
canvas = tkinter.Canvas(width=wdt, height=hdt, background="blue")
canvas.pack()


canvas.create_polygon(150, 100, 200, 100, 200, 200, 250, 200, 250, 100, 300, 100, 300, 350, 250, 350, 250, 250, 200, 250, 200, 350, 150, 350, 150, 100,  fill="white")
canvas.create_text(220, 400, text="NEMOCNICA", font=('Arial', 25), fill="white")

window.mainloop()


