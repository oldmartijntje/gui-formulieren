import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning
import smtplib, ssl
import random
import string
import accounts_omac

configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(configSettings)
if data == False:
    exit()

appIDorName = 'AnimeClubRegistration'

#there is a function to create your data folders
#it returns the data back to you with empty lists for the 'appData' 'collectables' 'achievements' dicts
data = accounts_omac.createAppData(data, appIDorName)



messagesTitle = 'EA'
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
sender_mail = 0
window = tkinter.Tk()
letterSting = string.ascii_letters
punctuationString = []
listAnimes = list()
confirmation = random.randint(0,1000000000000)
usedButton = False
registrationCode = 0
failOrNot = 0
numbers_used = ['1','6','9','0']
numbers_used2 = ['2','6','9','4','3']
numbers_used3 = ['8','6','9','5','2']
numbers_used4 = ['7','6','9','4','3']


def inputCode(*args):
    def checkCode():
        code = code_var.get()
        if len(str(1111110111111)) == len(code):
            if code.isnumeric():
                if (code[6] == str(0) or code[6] == str(1)) and code[0] in numbers_used and code[1] in numbers_used2 and code[2] in numbers_used3 and code[len(code)-1] in numbers_used4:
                    if str(code)[6] == str(0):
                        tkinter.messagebox.showinfo(title=messagesTitle,message ='You were not accepted, sorry')
                    else:
                        tkinter.messagebox.showinfo(title=messagesTitle,message ='You were accepted, YAY!')
                else:
                    tkinter.messagebox.showerror(title=messagesTitle,message ='This is not a valid Registration Code! Are you sure you got this one in your mail?')
            else:
                tkinter.messagebox.showerror(title=messagesTitle,message ='This is not a valid Registration Code! u doofus')
        else:
            tkinter.messagebox.showerror(title=messagesTitle,message ='This is not a valid Registration Code!')

    window.destroy()
    newWindow = tkinter.Tk()
    code_var = tkinter.StringVar()
    confirmationLabel = tkinter.Label(newWindow,text='Your registration code:').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")
    confirmationEntry = ttk.Entry(newWindow, textvariable=code_var).grid(column=1, row=0, ipadx=20, ipady=10, sticky="EW")
    confirmationButton = ttk.Button(newWindow, text='Check Results', command = checkCode).grid(column=2, row=0, ipadx=20, ipady=10, sticky="EW")





def config():
    global sender_mail
    global password
    import configparser
    import os
    if os.path.isfile("mailConfig.ini"):#read config if it exists
        config = configparser.ConfigParser()
        config.read('mailConfig.ini')
    else:#create config
        with open('mailConfig.ini', 'w') as configfile:
            config = configparser.ConfigParser(allow_no_value=True)
            config['DEFAULT'] = {'mail_adress' : 'None',
                'password' : 'cheese'}
            config.write(configfile)
            tkinter.messagebox.showwarning(title=messagesTitle,message ='change your mail and password in mailConfig.ini for this to work')
            window.destroy()
    sender_mail = config['DEFAULT']['mail_adress']
    password = config['DEFAULT']['password']
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_mail, password)



def nameChanges(*args):
    if name_var.get() != name_var2.get():
        tkinter.messagebox.showerror(title=messagesTitle,message ='your name isn\'t the same')

def changes(*args):
    global age_var
    global selectedCharacter
    age_var.set(f'your Age: {ageList[age_value.get()]}')
    selectedCharacter.set(f'Selected: {characterList[selectedCharacterSlider.get()]}')

def addCharacter(*args):
    global anime_var
    global selectedCharacter
    if characterList[selectedCharacterSlider.get()] == 'Delete':
        if len(anime_var.get()) > 0:
            anime_var.set(anime_var.get()[0:-1])
            random.shuffle(characterList)
    else:
        anime_var.set(anime_var.get()+characterList[selectedCharacterSlider.get()])
        random.shuffle(characterList)
    selectedCharacter.set(f'Selected: {characterList[selectedCharacterSlider.get()]}')


def addAnime(*args):
    global animeWatchedCombobox
    global anime_var
    if len(anime_var.get()) > 0:
        listAnimes.append(anime_var.get())
        animeWatchedCombobox.configure(values = listAnimes)
        anime_var.set('')

def checkWin():
    global failOrNot
    if ageList[age_value.get()] > 8 and ageList[age_value.get()] < 40 and len(accounts_omac.removeCharacters(name_var.get())) >= 3 and len(listAnimes) > 1 and type_var.get() == 'Hentai':
        failOrNot = 1
    else:
        failOrNot = 0


def sendMail():
    global registrationCode
    checkWin()
    
    registrationCode = f'{numbers_used[random.randint(0,len(numbers_used))]}{numbers_used2[random.randint(0,len(numbers_used2))]}{numbers_used3[random.randint(0,len(numbers_used3))]}{random.randint(100,999)}{failOrNot}{random.randint(10000,99999)}{numbers_used4[random.randint(0,len(numbers_used4))]}'
    animeListString = ''

    for x in range(len(listAnimes)):
        animeListString = animeListString + f"        '{listAnimes[x]}',\n"
    message = f"""\
Subject: sIGN UP TO THE aNIME cLUB iNTERNSHIP

Your Data:\n\n{{\n    'name' : '{accounts_omac.removeCharacters(name_var.get())}',\n    'age' : '{ageList[age_value.get()]}',\n    'animes' : [ \n{animeListString}    ],\n    'favoriteType' : '{type_var.get()}',\n    'publicHentaiWatching' : '{together_var.get()}'\n}}\n\nYour registration code: {registrationCode}"""
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_mail, password)
        server.sendmail(sender_mail, email_var.get(), message)



def apply(*args):
    if len(name_var.get()) > 0 and len(name_var2.get()) > 0:
        if name_var.get() == name_var2.get():
            if len(listAnimes) > 0:
                if '@' in email_var.get() and '.' in email_var.get():
                    if len(type_var.get()) > 1:
                        if len(together_var.get()) > 1:
                            if len(confirmationCode_var.get()) > 0:
                                if confirmationCode_var.get().isnumeric():
                                    if int(confirmationCode_var.get()) == confirmation:
                                        if usedButton == True:
                                            sendMail()
                                            tkinter.messagebox.showinfo(title=messagesTitle,message ='You will receive a mail with the information and your unique registration code. It\'s also sent to our team to review')
                                        else:
                                            tkinter.messagebox.showerror(title=messagesTitle,message ='you guessed the code correctly, but you didn\'t get it legit, so press the "(re)Send Code" button and then try again')
                                    else:
                                        tkinter.messagebox.showerror(title=messagesTitle,message ='the confirmation code is incorrect')
                                else:
                                    tkinter.messagebox.showerror(title=messagesTitle,message ='the confirmation code is NaN')
                            else:
                                tkinter.messagebox.showerror(title=messagesTitle,message ='you have not entered the confirmation code')
                        else:
                            tkinter.messagebox.showerror(title=messagesTitle,message ='you have not given your preference to watching together')
                    else:
                        tkinter.messagebox.showerror(title=messagesTitle,message ='you have not entered what type of anime you watch the most and prefer')
                else:
                    tkinter.messagebox.showerror(title=messagesTitle,message ='not a valid mail adress')
            else:
                tkinter.messagebox.showerror(title=messagesTitle,message ='no anime added to your watched / watching list')
        else:
            tkinter.messagebox.showerror(title=messagesTitle,message ='the names aren\'t the same')
    else:
        tkinter.messagebox.showerror(title=messagesTitle,message ='no name entered')


def sendCode(*args):
    global confirmation
    global usedButton
    if usedButton == False:
        usedButton = True
    if email_var.get() != '':
        confirmation = random.randint(0,1000000000000)
        message = f"""\
Subject: Confirmation Code

Your confirmation code is: {confirmation}\nOwO"""
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_mail, password)
            server.sendmail(sender_mail, email_var.get(), message)
        tkinter.messagebox.showinfo(title=messagesTitle,message =f'Your confirmation code has been sent to: {email_var.get()}\nIs this not your mail account? then please change it.\nThe confirmation code will work until you reopen the program or click the "(re)Send code" button')
    else:
        tkinter.messagebox.showerror(title=messagesTitle,message ='no mail account entered, can\'t send a mail to nothing')

ageList = list()
characterList = [' ', 'Backspace','Delete', 'Spacebar']
for x in range(len(letterSting)+len(punctuationString)):
    if x < len(letterSting):
        characterList.append(letterSting[x])
    else:
        
        characterList.append(punctuationString[x - len(letterSting)])
        
for x in range(150):
    ageList.append(x)

random.shuffle(ageList)
random.shuffle(characterList)


titleLabel = tkinter.Label(window, text= 'aNIME cLUB iNTERNSHIP').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW", columnspan= 3)

nameLabel = tkinter.Label(window, text= 'Name:').grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
name_var = tkinter.StringVar()
nameEntry = ttk.Entry(window, textvariable= name_var).grid(column=1, row=1, ipadx=20, ipady=10, sticky="EW", columnspan= 2)
name_var.trace('w', nameChanges)

nameLabel2 = tkinter.Label(window, text= 'confirm Name:').grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
name_var2 = tkinter.StringVar()
animeEntry = ttk.Entry(window, textvariable= name_var2).grid(column=1, row=2, ipadx=20, ipady=10, sticky="EW", columnspan= 2)
name_var2.trace('w', nameChanges)

age_value = tkinter.IntVar()

age_var = tkinter.StringVar()
ageLabel = tkinter.Label(window, textvariable= age_var).grid(column=0, row=3, ipadx=20, ipady=10, sticky="EW", columnspan= 3)

selectedCharacterSlider = tkinter.IntVar()

ageSlider = ttk.Scale(window,from_=0,to=149,orient='horizontal',variable=age_value, command = changes).grid(column=0, row=4, ipadx=20, ipady=10, sticky="EW", columnspan= 3)
animeSlider = ttk.Scale(window,from_=0,to=len(characterList)-1,orient='horizontal',variable=selectedCharacterSlider, command = changes).grid(column=0, row=8, ipadx=20, ipady=10, sticky="EW", columnspan= 3)

selectedCharacter = tkinter.StringVar()

buttonAdd = ttk.Button(window, text='Add', command=addCharacter).grid(column=1, row=7, ipadx=20, ipady=10, sticky="EW")
buttonComplete = ttk.Button(window, text='Add to list',command=addAnime).grid(column=2, row=7, ipadx=20, ipady=10, sticky="EW")
selectedCharacterLabel = tkinter.Label(window, textvariable= selectedCharacter).grid(column=0, row=7, sticky="EW")

animeWatchedLabel = tkinter.Label(window,text='anime\'s watched/watching:').grid(column=0, row=5, ipadx=20, ipady=10, sticky="EW")
animeWatchedCombobox = ttk.Combobox(window,state="readonly", values = listAnimes)
animeWatchedCombobox.grid(column=1, row=5, ipadx=20, ipady=10, sticky="EW", columnspan= 2)

anime_var = tkinter.StringVar()
animeEntry = ttk.Entry(window, textvariable= anime_var,state="readonly").grid(column=1, row=6, ipadx=20, ipady=10, sticky="EW", columnspan= 2)
animeLabel = tkinter.Label(window, text= 'Anime Name:').grid(column=0, row=6, ipadx=20, ipady=10, sticky="EW")

emailLabel = tkinter.Label(window, text= 'mail adress:').grid(column=0, row=11, ipadx=20, ipady=10, sticky="EW")
email_var = tkinter.StringVar()
emailEntry = ttk.Entry(window, textvariable= email_var).grid(column=1, row=11, ipadx=20, ipady=10, sticky="EW", columnspan= 2)

type_var = tkinter.StringVar()
animeHentaiYiff1 = ttk.Radiobutton(window, text='Anime', value='Anime', variable=type_var, state = 'disabled').grid(column=0, row=9, ipadx=20, ipady=10, sticky="EW")
animeHentaiYiff2 = ttk.Radiobutton(window, text='Hentai', value='Hentai', variable=type_var).grid(column=1, row=9, ipadx=20, ipady=10, sticky="EW")
animeHentaiYiff3 = ttk.Radiobutton(window, text='Yiff', value='Yiff', variable=type_var).grid(column=2, row=9, ipadx=20, ipady=10, sticky="EW")

together_var = tkinter.StringVar()
thoughtsLabel = tkinter.Label(window, text= 'would you want to watch hentai together?').grid(column=0, row=10, ipadx=20, ipady=10, sticky="EW", columnspan= 2)
together1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=together_var).grid(column=2, row=10, ipadx=20, ipady=10, sticky="EW")

confirmationCode_var = tkinter.StringVar()
confirmationLabel = tkinter.Label(window,text='Confirmation Code:').grid(column=0, row=12, ipadx=20, ipady=10, sticky="EW")
confirmationEntry = ttk.Entry(window, textvariable=confirmationCode_var).grid(column=1, row=12, ipadx=20, ipady=10, sticky="EW")
confirmationButton = ttk.Button(window, text='(re)Send Code', command = sendCode).grid(column=2, row=12, ipadx=20, ipady=10, sticky="EW")


buttonFinished = ttk.Button(window, text= 'Apply', command=apply).grid(column=0, row=14, ipadx=20, ipady=10, sticky="EW", columnspan= 2)
buttonFinished = ttk.Button(window, text= 'I already applied', command=inputCode).grid(column=2, row=14, ipadx=20, ipady=10, sticky="EW")

config()



changes()
window.mainloop()

data = accounts_omac.saveAccount(data, configSettings)