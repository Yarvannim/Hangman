import GetRandomWord
import Database.db
import pwinput


def start():
    _choice = input('Do you want to register or login?: ')
    if(_choice == 'register'):
        register()
    elif(_choice == 'login'):
        login()
    else:
        print('Please choose one of the given choices')
        start()

def register():
    _username = input('Please enter your username: ')
    _password = pwinput.pwinput(prompt='Please enter your password: ')
    _registerstatus = Database.db.register(_username, _password)
    if(_registerstatus == False):
        print(_registerstatus[1])
    else:
        print('You registered successfully')
        print('Redirecting to login screen')
        print('- - - - - - - - -')
        login()

def login():
    _username = input('Please enter your username: ')
    _password = pwinput.pwinput(prompt='Please enter your password: ')
    _loginData = Database.db.login(_username, _password)
    if(_loginData[0] == True):
        print('Welcome', _loginData[1])
        play()
    else:
        print("Your login credentials don't exist in our system")
        start()

def selectDifficulty():
    difficulty = input('Select difficulty: Easy, Intermediate, Hard: ')
    if(difficulty == "Easy"):
        _word = GetRandomWord.getEasyWord()
        return _word
    elif(difficulty == 'Intermediate'):
        _word = GetRandomWord.getIntermediateWord()
        return _word
    elif(difficulty == 'Hard'):
        _word = GetRandomWord.getHardWord()
        return _word
    else:
        print('You did not choose a valid option, Choose a valid option')
        selectDifficulty()

def playAgain():
    agian = input('Do you wish to play again? Yes or No? ')
    print(agian)
    if(agian == 'Yes' or agian == 'Y'):
        play()
    else:
        print('Have a good one!')
        exit()    

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
            _guessedCharacters.append(guess)
            if(guess not in _word):
                print(guess + ' is not in the word')
                _lives -=1
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
    start()

main()

