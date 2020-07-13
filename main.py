# imports & modules
import time
import random
import pangrams

# statics & data structures
APPNAME = 'ICBIN Terminal'
GAMELENGTH = 3

MENU_ALIASES = {
    'quickplay' : 'quickplay',
    'help' : 'help',
    'exit' : 'app_exit'
}

# function definitions
def welcome_msg():
    print(f'Welcome to {APPNAME}!')

def quickplay():
    print('quickplay activated')
    for sentence in random.sample(pangrams.pangrams, GAMELENGTH):
        user_type = input(f'Sentence is:\n{sentence}\n')
        if user_type == sentence:
            print('Nice')
        else:
            print('Aww, sad')

def help():
    print('printing help message')

def app_exit():
    print('Thanks for playing!')
    exit()

# main program
welcome_msg()
continue_playing = True
while True:
    user_in = input('Input Command: ')
    if user_in in MENU_ALIASES:
        eval(f'{MENU_ALIASES[user_in]}()')
    else:
        print('Sorry, I didn\'t understand. Could you rephrase that?')
    

