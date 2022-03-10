import random
import accounts_omac
configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingConsole(configSettings)
file = open("wordle.txt", "r+")
wordsList = file.read().split('\n')
wordOfTheDay = wordsList[random.randint(0,len(wordsList)-1)].lower()
#print(wordOfTheDay)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def guessFunction():
    guessDict = {}
    for x in range(len(word)):
        if guess[x] == word[x]:
            print(f'{guess[x]} is correct')
            if guess[x] not in guessDict:
                guessDict[guess[x]] = 1
            elif guessDict[guess[x]] < wordDict[guess[x]]:
                guessDict[guess[x]] += 1
        elif guess[x] not in wordDict:
            if guess[x] in alphabet:
                alphabet.pop(alphabet.index(guess[x]))
            print(f'{guess[x]} is incorrect')
        else:
            if guess[x] not in guessDict:
                guessDict[guess[x]] = 1
                print(f'{guess[x]} is placed wrong')
            elif guessDict[guess[x]] < wordDict[guess[x]]:
                guessDict[guess[x]] += 1
                print(f'{guess[x]} is placed wrong')
            else:
                print(f'{guess[x]} is incorrect')


word = wordOfTheDay.lower()
wordDict = {}
guess = ''


for x in range(len(word)):
    if word[x] not in wordDict:
        wordDict[word[x]] = 1
    else:
        wordDict[word[x]] += 1

while guess != word:
    guess = input(f'{alphabet}\n>').lower()
    if len(guess) == len(word) and guess in wordsList:
        guessFunction()
    else:
        print('that\'s not an option')
data = accounts_omac.saveAccount(data, configSettings)