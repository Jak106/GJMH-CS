import tkinter

window = tkinter.Tk()
wdt = 1000
hdt = 1000
origin = {"x": wdt/2, "y": hdt/2 }
canvas = tkinter.Canvas(width=wdt, height=hdt, background="#0091FA")
canvas.pack()

canvas.create_oval(origin["x"]-300, origin["y"]-300, origin["x"]+300, origin["y"]+300, fill="#c7b279", outline="#0091FA")
hour = canvas.create_line(origin["x"], origin["y"], origin["x"], origin["y"]-300, fill="black", width=5) #hour
minute = canvas.create_line(origin["x"], origin["y"], origin["x"], origin["y"]-250, fill="white", width=3) #minute
second = canvas.create_line(origin["x"], origin["y"], origin["x"], origin["y"]-200, fill="red", width=1) #second
canvas.create_oval(origin["x"]-10, origin["y"]-10, origin["x"]+10, origin["y"]+10, fill="black")



window.mainloop()