# "Guess the number" mini-project - Nick Togneri
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random
rem_guesses = 7
range_ceil = 100
range_is_100 = True


# function to start and restart the game

def new_game():
    # initialize global variables 
    global secret_number
    secret_number = random.randrange(0, range_ceil)
    print
    print 'New game started, range is 1 -', range_ceil
    if range_is_100 is True:
        rem_guesses = 7
    else:
        rem_guesses = 10
    print 'Remaining guesses:', rem_guesses

    
    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_ceil, rem_guesses, range_is_100
    range_ceil = 100
    rem_guesses = 7
    range_is_100 = True
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_ceil, rem_guesses, range_is_100
    range_ceil = 1000
    rem_guesses = 10
    range_is_100 = False
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global rem_guesses

    num_guess = int(guess)
    print
    print 'Guess was:', num_guess
    
    if rem_guesses <= 0:
        print 'Out of guesses!  Starting a new game'
        new_game()
    if num_guess == secret_number:
        print 'Correct!  Nice one!'
        print 'Starting a new game...'
        new_game()
    elif num_guess < secret_number:
        rem_guesses -= 1
        print 'Number of remaining guesses:', rem_guesses
        print 'Higher!'
    elif num_guess > secret_number:
        rem_guesses -= 1
        print 'Number of remaining guesses:', rem_guesses
        print 'Lower!'
    else:
        print 'whaaat?'
            

# create frame

frame = simplegui.create_frame('Guess the Number', 200, 200, 300)


# register event handlers for control elements and start frame

inp = frame.add_input('Enter a guess:', input_guess, 100)

button1 = frame.add_button('Range: 0 - 100', range100)

button2 = frame.add_button('Range: 0 - 1000', range1000)


# Opens frame with two buttons

frame.start


# call new_game 

new_game()


