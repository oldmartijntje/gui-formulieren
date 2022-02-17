import tkinter
from tkinter import ttk
from datetime import date
from tkinter.messagebox import showerror, showwarning, showinfo
complete = [1,0,1]
today = date.today()

def checkButton():
    global startButton
    if complete == [1,1,1]:
        startButton.configure(state= "normal")
    else:
        startButton.configure(state= "disabled")


def showDate():
    todayDay = today.strftime("%Y/%m/%d")
    todayDay = todayDay.split('/')
    whatMonth = months.index(f"{selected_month.get()}") + 1
    day0 = date(int(todayDay[0]), int(todayDay[1]), int(todayDay[2]))
    day1 = date((int(selected_year.get())), whatMonth, int(selected_day.get()))
    delta = day1 - day0
    if delta.days < 0:
        showwarning('Meep', f'that\'s {delta.days * -1} days ago')
    elif delta.days == 0:
        showwarning('Meep', 'that\'s today')
    else:
        showwarning('Meep', f'that\'s in {delta.days} days')
def daySelected(event):
    global complete
    complete[0] = 1
    checkButton()


def changeMonth(event):
    global day
    global selected_day
    global complete
    global day
    day.configure(state= 'readonly')
    if selected_month.get() == 'Feb':
        if int(selected_day.get()) not in februaryDays:
            selected_day.set(1)
        day.configure(values=februaryDays)
    elif selected_month.get() in evenMonths:
        if int(selected_day.get()) not in evenDays:
            selected_day.set(1)
        day.configure(values=evenDays)
    else:
        day.configure(values=unevenDays)
    complete[1] = 1      
    checkButton()  

    

def changeYear(*args):
    global complete
    while selected_year.get() != ''and selected_year.get() != '-':
        try:
            timeVariable=int(selected_year.get())
            if timeVariable < 0:
                selected_year.set(timeVariable * -1)
            elif timeVariable == 0:
                selected_year.set(1)
            break
        except:
            selected_year.set(selected_year.get()[0:-1])
    if selected_year.get() == '' or selected_year.get() == '-':
        complete[2] = 0
    else:
        complete[2] = 1
    checkButton()

years = list()
evenDays = list()
februaryDays = list()
unevenDays = list()

for x in range(-4000,3000):
 years.append(x)
for x in range(1,29):februaryDays.append(x)
for x in range(1,31):evenDays.append(x)
for x in range(1,32):unevenDays.append(x)


months = ['Jan','Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
window = tkinter.Tk()
evenMonths = ['Apr', "Jun", 'Sep', 'Nov']



selected_month = tkinter.StringVar()
month = ttk.Combobox(window,values=months,state="readonly",textvariable=selected_month)
month.bind('<<ComboboxSelected>>', changeMonth)
month.grid(column=3, row=2)

selected_day = tkinter.IntVar()
day = ttk.Combobox(window,state="readonly",textvariable=selected_day)
selected_day.set(1)
day.grid(column=1, row=2)
day.bind('<<ComboboxSelected>>', daySelected)
day.configure(state= "disabled")


selected_year=tkinter.StringVar()
selected_year.set(today.strftime("%Y"))
YearEntry = tkinter.Entry(window,textvariable = selected_year, font=('calibre',10,'normal'))
YearEntry.grid(column=5, row=2)
selected_year.trace('w', changeYear)

tkinter.Label(window,text='-').grid(column=2, row=2)
tkinter.Label(window,text='-').grid(column=4, row=2)
tkinter.Label(window,text='Date:', font=("Comic Sans MS", 11)).grid(column=3, row=1)

startButton = tkinter.Button(window)
startButton.configure(fg = 'black', bg = 'white', font=("Comic Sans MS", 11), text = 'press here to start', command = showDate, state= "disabled")
startButton.grid(column=3, row=3)


window.mainloop()