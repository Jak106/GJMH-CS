import random
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=700, background="white")


myDictionary = ["train", "bus", "electrobike", "informatics", "guess", "idea", "school", "calendar"]

letterList = []
guess = []

word = random.choice(myDictionary)

for letter in word:
    letterList.append(letter)
    guess.append("_")

numTry = 0

def guessFunc():
    global numTry
    if "_" not in guess:
        print("You guessed the correct word, congrats!!!")
        exit()
    letterGuess=inputTxt.get(1.0, "end-1c")
    if letterGuess in letterList:
        for x in range(len(letterList)):
            if letterList[x] == letterGuess:    
                guess[x] = letterGuess
                guessTxt.config(text = ''.join(guess))
    else:
        for x in range(numTry):
            human[x]
        numTry += 1

#create button
button = tk.Button(text="Try this", command=guessFunc)
canvas.create_window(700, 400, window=button, width=100)

#input
inputTxt = tk.Text(root, height=1, width=15, bg="grey")
canvas.create_window(700, 450, window=inputTxt)

#guess text
guessTxt = tk.Label(root, text=''.join(guess))
canvas.create_window(700, 500, window=guessTxt)

#hangman
def human():
    hangman = [canvas.create_line(100, 650, 200, 500, 300, 650, width=3, smooth=True),
    canvas.create_line(200, 575, 200, 200, width=3),
    canvas.create_line(200, 200, 400, 200, width=3),
    canvas.create_line(200, 250, 250, 200, width=3),
    canvas.create_line(400, 200, 400, 300, fill="brown"),
    canvas.create_oval(380, 300, 420, 350, fill="#FFCCCC", outline="white"),
    canvas.create_line(400, 350, 400, 470, fill="#FFCCCC", width=4),
    canvas.create_line(400, 370, 350, 420, fill="#FFCCCC", width=4),
    canvas.create_line(400, 370, 450, 420, fill="#FFCCCC", width=4),
    canvas.create_line(400, 470, 380, 560, fill="#FFCCCC", width=4),
    canvas.create_line(400, 470, 420, 560, fill="#FFCCCC", width=4)]
    
    




#hangman = [canvas.create_line(100, 650, 200, 500, 300, 650, width=3, smooth=True),
#canvas.create_line(200, 575, 200, 200, width=3),
#canvas.create_line(200, 200, 400, 200, width=3),
#canvas.create_line(200, 250, 250, 200, width=3),
#canvas.create_line(400, 200, 400, 300, fill="brown"),
#canvas.create_oval(380, 300, 420, 350, fill="#FFCCCC", outline="white"),
#canvas.create_line(400, 350, 400, 470, fill="#FFCCCC", width=4),
#canvas.create_line(400, 370, 350, 420, fill="#FFCCCC", width=4),
#canvas.create_line(400, 370, 450, 420, fill="#FFCCCC", width=4),
#canvas.create_line(400, 470, 380, 560, fill="#FFCCCC", width=4),
#canvas.create_line(400, 470, 420, 560, fill="#FFCCCC", width=4)]


canvas.pack()
root.mainloop()