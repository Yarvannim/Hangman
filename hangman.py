import requests
import random
import json

def getWordFromApi(_length):
    _response = requests.get("https://random-word-api.herokuapp.com/word?length=" + str(_length))
    _json = json.loads(_response.text)
    _word = _json[0]
    print(_word)
    return _word

def selectDifficulty():
    difficulty = input('Select difficulty: Easy, Intermediate, Hard: ')
    if(difficulty == "Easy"):
        _wordLength = random.randint(3,6)
        _word = getWordFromApi(_wordLength)
        return _word
    elif(difficulty == 'Intermediate'):
        _wordLength = random.randint(7,8)
        _word = getWordFromApi(_wordLength)
        return _word
    elif(difficulty == 'Hard'):
        _wordLength = random.randint(9,15)
        _word = getWordFromApi(_wordLength)
        return _word
    else:
        print('You did not choose a valid option, Choose a valid option')
        difficulty = input('Select difficulty: Easy, Intermediate, Hard: ')

def playAgain():
    agian = input('Do you wish to play again? Yes or No? ')
    if(agian == 'Yes' or 'Y' ):
        play()
    else:
        print('Have a good one!')    

def play():
    _word = selectDifficulty()
    _wordchars = len(_word)
    _lives = 5
    _wordguessed = False
    _guessedCharacters = []
    print('_' * _wordchars) 
    while(_lives > 0 and not _wordguessed):
        _wordProgress = ''
        guess = input('Guess a character: ')
        if(len(guess) == 1):
            if(guess not in _word):
                _guessedCharacters.append(guess)
                print(guess + ' is not in the word')
                _lives -=1
            elif(guess in _word):
                _guessedCharacters.append(guess)
            for character in _word:
                if(character in _guessedCharacters):
                    _wordProgress += character
                    if(_wordProgress == _word):
                        _wordguessed = True
                else:
                    _wordProgress += '_'
            print(_wordProgress)
        elif(_wordProgress == _word):
            print('got here')
            _wordguessed = True
        else:
            print('You can only guess one character at a time')
    if _wordguessed:
        print('Well played, you guessed the word!')
    else:
        print('Sorry you do not have any tries left :( the word was: ' + _word)
    playAgain()

def main():
    play()


main()

