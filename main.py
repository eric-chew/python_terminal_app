# imports & modules
import time
import random
import pangrams

# statics & data structures
APPNAME = 'ICBIN TTT'
GAMELENGTH = 1
COUNTDOWN_TIMER = 3
COUNTDOWN_MSG = 'GO!'

MENU_ALIASES = {
    'quickplay' : 'quickplay',
    'q' : 'quickplay', # consider removing
    'help' : 'help',
    'exit' : 'app_exit'
}

# function definitions
def welcome_msg():
    print(f'Welcome to {APPNAME}!')

def countdown(timer):
    for sec in range(timer, 0, -1):
        print(sec)
        time.sleep(1)
    print(COUNTDOWN_MSG)

def quickplay():
    print('quickplay activated')
    char_count = 0
    start = time.time()
    for sentence in random.sample(pangrams.pangrams, GAMELENGTH):
        char_count += len(sentence)
        user_type = input(f'Sentence is:\n{sentence}\n')
        if user_type == sentence:
            print('Nice')
        else:
            print('Aww, sad')
    end = time.time()
    total_time_sec = end - start
    total_time_min = total_time_sec / 60
    cpm = char_count / total_time_min
    wpm = cpm / 5
    print(f'Your CPM (characters per minute) is {cpm:.02f}!')
    print(f'Your WPM (words per minute) is {wpm:.02f}!')

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
    

