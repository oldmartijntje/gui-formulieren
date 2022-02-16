import tkinter
window = tkinter.Tk()
blackOrWhite = 'black'
for x in range(10):
    for y in range(10):
        if x % 2 == 0:tkinter.Label(window,bg = blackOrWhite).grid(column=y, row=x, ipadx=10, ipady=5)
        else:tkinter.Label(window,bg = blackOrWhite).grid(column=9-y, row=x, ipadx=10, ipady=5)
        if blackOrWhite == 'black': blackOrWhite = 'white'
        else: blackOrWhite = 'black'
window.mainloop()