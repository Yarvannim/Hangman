import requests
import random
import json

# generate integer between 3 and 6 and send the random integer to getword function
def getEasyWord():
    _wordLength = random.randint(3,6)
    _word = getWordFromApi(_wordLength)
    return _word

# generate integer between 7 and 8 and send the random integer ti getword function
def getIntermediateWord():
    _wordLength = random.randint(7,8)
    _word = getWordFromApi(_wordLength)
    return _word

# generate integer between 9 and 15 and send the random integer ti getword function
def getHardWord():
    _wordLength = random.randint(9,15)
    _word = getWordFromApi(_wordLength)
    return _word

# get random word from api based on lentgh from functions based on the choice the user made in his difficulty choice and return the word
def getWordFromApi(_length):
    _response = requests.get("https://random-word-api.herokuapp.com/word?length=" + str(_length))
    _json = json.loads(_response.text)
    _word = _json[0]
    return _word