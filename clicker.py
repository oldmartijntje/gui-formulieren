import tkinter

gameVersion = 'v5'
#old variant: [name,[time],{appDictionary},randint1,randint2,[data with lock += 2 randints],[dataHistory],[data with lock without 2 randints]]
#new variant: [name,[time],{appDictionary},randint1,randint2,[data with lock += 2 randints],[dataHistory],[data with lock without 2 randints]], {achievements}, {collectables}

import pickle
import os
import datetime
import random
import configparser


if os.path.isfile("systemConfig.ini"):#read config if it exists
    config = configparser.ConfigParser()
    config.read('systemConfig.ini')
else:#create config
    with open('systemConfig.ini', 'w') as configfile:
        config = configparser.ConfigParser(allow_no_value=True)
        folder = input('do you have a specific folder where you want to store account data?\nimport the path, or not\n>')
        config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
            'fileExtention' : 'mcld'}
        if os.path.isdir(folder):#check if the inputted folder exists
            if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                folder += '\\'
            config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : 'False', 'AccountName' : 'testaccount'}
        else:
            config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : 'False', 'AccountName' : 'testaccount'}
            try:
                os.mkdir('accounts/')
            except:
                pass
        config.write(configfile)
        print('we created systemConfig.ini, this contains configurations for the account system, change the [User] section at any time')

#load config data
fileExtention = config['DEFAULT']['fileExtention']
path = config['User']['SaveFileFolder']
autoLogin = config['User']['AutoLogin']
autoLoginName = config['User']['AccountName']

def checkSave(pickledData):#check if account is corrupted
    def corruptedAccount():#what to do when account is corrupted
        exit()
    try:
        name, list1, dictionary, num1, num2, data1, data2, data3, achievements, collectables = pickledData
    except:
        name, list1, dictionary, num1, num2, data1, data2, data3 = pickledData
    if data3[1] - data3[0] != data1[1] - data1[0] or data1[0] != data3[0] + (num1 * num2):#check if decryption is possible
        input('Account Data Corrupted, Please find a way to fix it or create a new one')
        corruptedAccount()
        return False
    else:
        print('Account Loaded Correctly')
        return True

def fixData(data):#remove encryption
    data[1] = data[1] - data[0]
    return data

def loadAccount():
    if checkSave(pickle.load( open(f'{path}{search}.{fileExtention}', "rb" ))) == True: #check if it is not corrupted (in my encryption)
        try:
            name, list1, appDataDict, num1, num2, data1, data2, data3, achievements, collectables= pickle.load( open(f'{path}{search.lower()}.{fileExtention}', "rb" )) #load the account
        except:
            name, list1, appDataDict, num1, num2, data1, data2, data3 = pickle.load( open(f'{path}{search.lower()}.{fileExtention}', "rb" )) #load old variant of account
            achievements = {}
            collectables = {}
        startTime = datetime.datetime.now()#start counting how long you are using the program
        data = fixData(data3)#decrypt data
    return name, list1, appDataDict, num1, num2, data1, data2, data3, achievements, collectables, startTime, data


def closeAccount(name, list1, data1):#close the account
    def scrambleData(data,num1,num2,key, num):
        data[0] = key + ((num1 * num2) * num)#add encryption
        data[1] += data[0]
        return data
    global startTime
    closeTime = datetime.datetime.now()#check the time
    list1[0] = round(list1[0] + ((closeTime - startTime).total_seconds()) // 60)#check difference in time from when opened
    num1 = random.randint(0,1000)#key1
    num2 = random.randint(0,1000)#key2
    key = random.randint(0,10000)#masterKey
    #this was used when the data is still encrypted, but if it's decrypted, keep this a comment:
    #data1 = fixData(data1)
    pickle.dump([name, list1, appDataDict, num1, num2, scrambleData(list(data1),num1,num2,key,1), scrambleData(list(data1),num1,num2,key,2), scrambleData(list(data1),num1,num2,key,0), achievements, collectables] , open(f'{path}{name}.{fileExtention}', "wb" ) )

def stringToSeed(seedString): #turns everything into ther ASCII value
    seedList = []
    for x in seedString:
        seedList.append(ord(x))#change every character into its ASCII value
    seedString = ''.join([str(elem) for elem in seedList])#add list together into string
    seed = int(seedString)
    return seed

#for easy loading and testing the account, you can enable this in the config
if autoLogin.lower() == 'true':
    search = autoLoginName
else:
    search = input('please give username\n>')


if os.path.exists(f'{path}{search.lower()}.{fileExtention}'):#check if account exists
    print('user found')
    name, list1, appDataDict, num1, num2, data1, data2, data3, achievements, collectables, startTime, data = loadAccount()
        
else:
    while True:
        print('user not found, do you want to create a new user with this name? Y/N')

        #for easy loading and testing the account
        #answer = 'y'#you can use this to skip the input for testing your code

        answer = input('you will be logged out afterwards\n>')
        if answer.lower() == 'y':
            pickle.dump([search.lower(), [0], {}, 69, 420, [41325, 41325], [41325, 41325], [12345, 12345], {}, {}], open(f'{path}{search.lower()}.{fileExtention}', "wb" ) )
            exit()
        elif answer.lower() == 'n':
            exit()

#example achievement


#use the dictonary for app related files, like for example rebirths or amounts of diamonds
#change this to your app their name
appName = 'clickerV5Martin'

if appName not in appDataDict:#if the user hasn't played before
    appDataDict[appName] = [gameVersion, 0]
else:
    #print(appDataDict[appName])#prints your data, just to show you how it works
    pass
if appName not in achievements:#if the user hasn't played before
    achievements[appName] = [[],{}]
achievements[appName][1] = {69:['haha nice','you got the funny number'],42069:['noice','the upgraded version of 69'],404:['i am not here','404 not found'],1234567890:['how did we get here?','thats the order of the numbers on your keyboard, :0'],-1:['wow','congrats bro, u have got a minus'],50:['congrats','gefeliciteerd abraham'],666:['satans waltz','Dancing with the devil'],777:['OwO','Holy number']}

#this is your game data, for easy use. but you can also just access your gamedata without this
appData = appDataDict[appName]
#it works the same with the collectables and achievements dictionaries as with the account data dict








#code:


















window = tkinter.Tk()
amount = appData[1]
string = tkinter.StringVar(value=amount)
window.configure(bg = 'grey')
touching = False
lastClicked = 'None'

def on_closing():
    global appDataDict
    window.destroy()
    #use this line if you edited the gamedata before the closeAccount(), if you didn't edit the gamedata, you can skip it
    
    appDataDict[appName][1] = amount
    #close the account correctly (so it won't get corrupted), use this where you need it, and save it here as a comment
    closeAccount(name, list1, data)

def achievementCheck():
    global achievements
    if amount in achievements[appName][1].keys():
        if amount in achievements[appName][0]:
            pass
        else:
            achievements[appName][0].append(amount)
            print(f'\n\nachievement unlocked: {achievements[appName][1][amount][0]}\nDescription: {achievements[appName][1][amount][1]}')


def changeColor():
    if touching == True:
        pass
    elif amount > 0:
        window.configure(bg = 'green')
    elif amount < 0:
        window.configure(bg = 'red')
    else:
        window.configure(bg = 'grey')

def change(change, button = 'None'):
    global amount
    global lastClicked
    global checkbutton
    lastClicked = button
    if lastClicked != 'None':
        checkbutton.configure(state= "normal")
        
    amount = change
    if amount == 404:
        string.set('')
    else:
        string.set(amount)
    achievementCheck()
    changeColor()

def enter(event):
    global touching
    touching = True
    window.configure(bg = 'yellow')

def leave(event):
    global touching
    touching = False
    changeColor()

def doubleClick(event):
    global amount
    match lastClicked:
        case 'Up':
            amount = amount * 3
        case 'Down':
            amount = amount // 3
    string.set(amount)

def tick():
    if checkboxVar.get() == 1:
        if lastClicked == 'Up':
            change(amount + 1,'Up')
        else:
            change(amount - 1,'Down')
    window.after(200, tick)

checkboxVar = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(window)
checkbutton.configure(text = 'autoclicker',state= "disabled", variable=checkboxVar)
checkbutton.pack()


button1 = tkinter.Button(window)
button1.configure(text='Up', command= lambda: change(amount + 1,'Up'))
button1.pack(ipady=10, fill = 'x', padx = 10, pady = 10)

label = tkinter.Label(window)
label.configure(textvariable=string)
#label.configure(command = lambda: change(amount * -1,'Middle'))
label.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)
label.bind('<Enter>',enter)
label.bind('<Leave>',leave)
label.bind('<Double-Button-1>',doubleClick)
window.bind('<space>',doubleClick)
window.bind('<+>',lambda event: change(amount + 1,'Up'))
window.bind('-',lambda event: change(amount - 1,'Down'))



button3 = tkinter.Button(window)
button3.configure(text='Down', command= lambda: change(amount -1,'Down'))
button3.pack(ipady=10, ipadx=200, fill = 'x', padx = 10, pady = 10)

window.protocol("WM_DELETE_WINDOW", on_closing)

tick()
achievementCheck()

window.mainloop()