import tkinter
import accounts_omac
import random

wordLenght = [4, 7]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]

# PART 1

start_window = tkinter.Tk()

def doNothing():
    print('no')

def changeWord(*args):
    global word_var
    global startButton
    word_var.set(accounts_omac.removeCharacters(accounts_omac.removeCharacters(word_var.get(), numbers)))
    if len(word_var.get()) >= wordLenght[0] and len(word_var.get()) <= wordLenght[1]:
        startButton.configure(state = 'normal')
    else:
        startButton.configure(state = 'disabled')

def startGame():
    start_window.destroy()

wordText = tkinter.Label(start_window, text = f'choose a word from {wordLenght[0]} to {wordLenght[1]} letters').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")

word_var = tkinter.StringVar()
word_entry = tkinter.Entry(start_window,textvariable = word_var, font=('calibre',10,'normal'))
word_entry.grid(column=1, row=0, ipadx=20, ipady=10, sticky="EW")
word_var.trace('w', changeWord)

startButton = tkinter.Button(start_window, text = 'start')
startButton.configure(state = 'disabled',command=startGame)
startButton.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW",columnspan=2)

start_window.protocol("WM_DELETE_WINDOW", doNothing)
start_window.mainloop()

# Part 2

woord = word_var.get()

game_window = tkinter.Tk()

for spinboxNumber in range(len(woord)):
    letters = accounts_omac.easy.addRandomNoDuplicates(alphabet, 4, [woord[spinboxNumber]])
    random.shuffle(letters)
    exec(f"current_value{spinboxNumber} = tkinter.StringVar()")
    exec(f"current_value{spinboxNumber}.set(letters[0])")
    exec(f"spin_box{spinboxNumber} = tkinter.Spinbox(game_window, value = letters, textvariable=current_value{spinboxNumber},wrap=True, state = 'readonly')")
    exec(f"spin_box{spinboxNumber}.grid(column={spinboxNumber}, row=0, ipadx=20, ipady=10, sticky='EW')")
game_window.mainloop()