import GetRandomWord
import Database.db
import pwinput

#function that runs to get the register or login 'screen'
def start():
    print('Welcome to the word guessing game!')
    while True:
        _choice = input('Do you want to register or login?: ')
        if(_choice == 'register'):
            return 1
        elif(_choice == 'login'):
            return 2
        else:
            print('Please choose one of the given choices')

# function that returns a smiley that get a little bit sadder with every life that is lost
def displaySmiley(_stage):
    _smiley = ''
    if(_stage == 6): _smiley=':)'
    elif(_stage == 5): _smiley=':}'
    elif(_stage == 4): _smiley=':]'
    elif(_stage == 3): _smiley=':{'
    elif(_stage == 2): _smiley=':['
    elif(_stage == 1): _smiley=':('
    return _smiley

# Sends username and password to register in db.py file, if username is already taken it will tell you
def register():
    _username = input('Please enter your username: ')
    _password = pwinput.pwinput(prompt='Please enter your password: ')
    _registerstatus = Database.db.register(_username, _password)
    while(_registerstatus == False):
        _username = input('Please enter your username: ')
        _password = pwinput.pwinput(prompt='Please enter your password: ')
        _registerstatus = Database.db.register(_username, _password)
        if(_registerstatus == False):
            print('Your credentials have already been taken!')
    else:
        print('You registered successfully')
        print('Redirecting to login screen')
        print('- - - - - - - - -')
        return True

# Sends username and password to login function in db.py if the user is found it prints welcome and otherwise it will say user is not known
def login():
    _username = input('Please enter your username: ')
    _password = pwinput.pwinput(prompt='Please enter your password: ')
    _loginData = Database.db.login(_username, _password)
    if(_loginData[0] == True):
        print('Welcome', _loginData[1])
        return True
    else:
        print("Your login credentials don't exist in our system")
        return False

# in this function the user selects a difficulty it will go to the GetRandomWord.py file to get a word
def selectDifficulty():
    while True:
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

# in this function you ask if the user wants to play again and if yes you just rerun the play function
def playAgain():
    agian = input('Do you wish to play again? Yes or No? ')
    if(agian == 'Yes' or agian == 'Y'):
        return True
    else:
        print('Have a good one!')
        exit()

# basically the main function of the whole program, many comments that are not really needed but wanted it to be clear
def play():
    # get word from selectdifficulty function that get word from GetRandomWord.py
    # also set all the values to variables that i need
    _word = selectDifficulty()
    _wordchars = len(_word)
    _lives = 6
    _wordguessed = False
    _guessedCharacters = []
    print('_' * _wordchars) 
    # as long as the lives are more than zero and _wordguessed is not true it will repeat the while loop
    while(_lives > 0 and not _wordguessed):
        # variable to display the word with underscores and characters once they are guessed
        _wordProgress = ''
        smile = displaySmiley(_lives)
        print(str(_lives) + ' life(s) left ' + smile)
        guess = input('Guess a character: ')
        # only if the guess length is equal to one it will actually do something with the guess
        if(len(guess) == 1):
            _guessedCharacters.append(guess)
            if(guess not in _word):
                print(guess + ' is not in the word')
                _lives -=1
            for character in _word:
                # if the character it loops over is in the guessedcharacter array it will add it to the variable to display how far the progress on guessing the word is
                if(character in _guessedCharacters):
                    _wordProgress += character
                    # if the word progress is the same as the the word it ends the while loop
                    if(_wordProgress == _word):
                        _wordguessed = True
                else:
                    _wordProgress += '_'
            # after it looped through the whole word it display the guessing progress
            print(_wordProgress)
        # if the user immediately guessed the word this happens
        elif(_wordProgress == _word):
            print('got here')
            _wordguessed = True
        # if the user guessed more than 1 character it will run this
        else:
            print('You can only guess one character at a time')
    # if the user has guessed the word it will congratulate you and otherwise it will tell you what the word was and run the playagain function
    if _wordguessed:
        print('Well played, you won the wordguessing game!')
    else:
        print('Sorry you do not have any tries left :( the word was: ' + _word)
# just the main function in which you start the whole game
def main():
    _playstate = True
    _loginstatus = False
    _status = start()
    if(_status == 1):
        register()
    while(_loginstatus == False):
        _loginstatus = login()
    while(_playstate == True):
        play()
        _playstate == playAgain()
        
main()

