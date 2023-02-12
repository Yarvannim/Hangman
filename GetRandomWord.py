import requests
import random
import json

def getEasyWord():
    _wordLength = random.randint(3,6)
    _word = getWordFromApi(_wordLength)
    return _word

def getIntermediateWord():
    _wordLength = random.randint(7,8)
    _word = getWordFromApi(_wordLength)
    return _word

def getHardWord():
    _wordLength = random.randint(9,15)
    _word = getWordFromApi(_wordLength)
    return _word

def getWordFromApi(_length):
    _response = requests.get("https://random-word-api.herokuapp.com/word?length=" + str(_length))
    _json = json.loads(_response.text)
    _word = _json[0]
    return _word