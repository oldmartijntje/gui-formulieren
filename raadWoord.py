import tkinter
import accounts_omac

wordLenght = [4, 7]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]


window = tkinter.Tk()



def changeWord(*args):
    global word_var
    global startButton
    word_var.set(accounts_omac.removeCharacters(accounts_omac.removeCharacters(word_var.get(), numbers)))
    if len(word_var.get()) >= wordLenght[0] and len(word_var.get()) <= wordLenght[1]:
        startButton.configure(state = 'normal')
    else:
        startButton.configure(state = 'disabled')

def startGame():
    print('e')

wordText = tkinter.Label(window, text = f'choose a word from {wordLenght[0]} to {wordLenght[1]} letters').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")

word_var = tkinter.StringVar()
word_entry = tkinter.Entry(window,textvariable = word_var, font=('calibre',10,'normal'))
word_entry.grid(column=1, row=0, ipadx=20, ipady=10, sticky="EW")
word_var.trace('w', changeWord)

startButton = tkinter.Button(window, text = 'start')
startButton.configure(state = 'disabled',command=startGame)
startButton.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW",columnspan=2)

window.mainloop()