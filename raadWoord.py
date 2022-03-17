import tkinter
import accounts_omac
import random
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter import ttk

replay = True
wordLenght = [4, 7]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]
score = 0

while replay:
    # PART 1

    start_window = tkinter.Tk()
    start_window.attributes('-topmost', True)

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

    word = word_var.get()

    score = len(word) * len(word)

    def check():
        if score <= 0:
            game_window.destroy()
            tkinter.messagebox.showerror(title='Result', message = 'And you failed!')


    def takeGuess():
        global replay
        global score
        global guess_label_var
        guess = {'right': 0, 'wrong': 0}
        for spinboxNumber in range(len(word)):
            test = 0

            #for some reason exec() is weird
            ldict = {}
            exec(f"testData = current_value{spinboxNumber}.get()",globals(),ldict)
            test = ldict['testData']

            if test == word[spinboxNumber]:
                guess['right'] += 1
            else:
                guess['wrong'] += 1
        if guess['right'] == len(word):
            game_window.destroy()
            if tkinter.messagebox.askokcancel("Time is up!", f'You won!\nScore: {score}\nWant to play again?'):
                pass
            else:
                replay = False
        elif guess['wrong'] == len(word):
            guess_label_var.set(f"ur so bad at this my guy, everything is wrong")
        else:
            guess_label_var.set(f"{guess['right']} were right, {guess['wrong']} were wrong")
        score -= guess['wrong'] * 2
        check()

        


    game_window = tkinter.Tk()
    game_window.attributes('-topmost', True)

    for spinboxNumber in range(len(word)):
        letters = accounts_omac.easy.addRandomNoDuplicates(alphabet, 4, [word[spinboxNumber]])
        random.shuffle(letters)
        exec(f"current_value{spinboxNumber} = tkinter.StringVar()")
        exec(f"current_value{spinboxNumber}.set(letters[0])")
        exec(f"spin_box{spinboxNumber} = ttk.Spinbox(game_window, value = letters, textvariable=current_value{spinboxNumber},wrap=True, state = 'readonly')")
        exec(f"spin_box{spinboxNumber}.grid(column={spinboxNumber}, row=0, ipadx=20, ipady=10, sticky='EW')")

    guess_label_var = tkinter.StringVar()
    guess_label_var.set('Guess!')

    guessButton = tkinter.Button(game_window, text = 'start')
    guessButton.configure(command=takeGuess)
    guessButton.grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW",columnspan=len(word))

    guessLabel = tkinter.Label(game_window, textvariable = guess_label_var)
    guessLabel.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW",columnspan=len(word))

    game_window.mainloop()
