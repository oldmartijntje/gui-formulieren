
import tkinter
window = tkinter.Tk()
blackOrWhite = 'black'
tekst = ['a','b','c','d','e','f','g','h','i','j']
class tile:
    def __init__(self,bg,fg,text,column,row,ipadx,ipady):
        self.label = tkinter.Label(window,bg = bg,text= text,fg = fg).grid(column=column, row=row, ipadx=ipadx, ipady=ipady)
        

for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            labelClass = tile(blackOrWhite,'red',f'{tekst[y]}{10-x}',y,x,20,10)
            labelClass.label.bind('<Button-1>',lambda event: labelClass.label.configure(fg='red'))
            

        else:
            tkinter.Label(window,bg = blackOrWhite,text= f'{tekst[9-y]}{10-x}',fg = 'red').grid(column=9-y, row=x, ipadx=20, ipady=10)
        if blackOrWhite == 'black': blackOrWhite = 'white'
        else: blackOrWhite = 'black'
window.mainloop()