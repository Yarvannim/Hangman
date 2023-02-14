import GetRandomWord
import Database.db
import pwinput

#function that runs to get the register or login 'screen'
def start():
    _choice = input('Do you want to register or login?: ')
    if(_choice == 'register'):
        register()
    elif(_choice == 'login'):
        login()
    else:
        print('Please choose one of the given choices')
        start()

# Sends username and password to register in db.py file, if username is already taken it will tell you
def register():
    _username = input('Please enter your username: ')
    _password = pwinput.pwinput(prompt='Please enter your password: ')
    _registerstatus = Database.db.register(_username, _password)
    if(_registerstatus == False):
        print(_registerstatus[1])
        start()
    else:
        print('You registered successfully')
        print('Redirecting to login screen')
        print('- - - - - - - - -')
        login()

# Sends username and password to login function in db.py if the user is found it prints welcome and otherwise it will say user is not known
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

# in this function the user selects a difficulty it will go to the GetRandomWord.py file to get a word
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

# in this function you ask if the user wants to play again and if yes you just rerun the play function
def playAgain():
    agian = input('Do you wish to play again? Yes or No? ')
    print(agian)
    if(agian == 'Yes' or agian == 'Y'):
        play()
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
        print('Well played, you guessed the word!')
    else:
        print('Sorry you do not have any tries left :( the word was: ' + _word)
    playAgain()
# just the main function in which you start the whole game
def main():
    start()

main()

