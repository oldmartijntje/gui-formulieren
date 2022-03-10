import tkinter
import random
window = tkinter.Tk()
blackOrWhite = 'black'
tekst = ['a','b','c','d','e','f','g','h','i','j']

for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            label_id = str(random.random()).replace(".", "")
            exec(f"label{label_id} = tkinter.Label(window)")
            exec(f"label{label_id}.configure(bg = blackOrWhite,text= f'{tekst[y]}{10-x}',fg = blackOrWhite)")
            exec(f"label{label_id}.bind('<Button-1>',lambda event: label{label_id}.configure(fg='red'))")
            exec(f"label{label_id}.grid(column=y, row=x, ipadx=20, ipady=10)")

        else:
            label_id = str(random.random()).replace(".", "")
            exec(f"label{label_id} = tkinter.Label(window)")
            exec(f"label{label_id}.configure(bg = blackOrWhite,text= f'{tekst[9-y]}{10-x}',fg = blackOrWhite)")
            exec(f"label{label_id}.bind('<Button-1>',lambda event: label{label_id}.configure(fg='red'))")
            exec(f"label{label_id}.grid(column=9-y, row=x, ipadx=20, ipady=10)")
        if blackOrWhite == 'black': blackOrWhite = 'white'
        else: blackOrWhite = 'black'
window.mainloop()