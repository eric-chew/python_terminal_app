#!/usr/sbin/python

# imports & modules
import time
import random
import sys
import pangrams
from termcolor import colored, cprint

# statics & data structures
APPNAME = 'Terminal Typing Test'
GAMELENGTH = 5
COUNTDOWN_TIMER = 3
COUNTDOWN_MSG = 'GO!'
SPEECH_DELAY = 0.02
PAUSE_DELAY = 0.75
CPW = 5 # Characters per word
TIMER_DELAY = 1

SENTENCE_LIST = pangrams.pangrams

MENU_ALIASES = {
    '1' : 'quickplay',
    'quickplay' : 'quickplay',
    '2' : 'help',
    'help' : 'help',
    '3' : 'app_exit',
    'exit' : 'app_exit',
}

# End of Game Aliases
EOG_ALIASES = {
    '1' : True,
    '1. play again' : True,
    'play' : True,
    'play again': True,
    'again' : True,
    '2' : False,
    '2. return to menu' : False,
    'return' : False,
    'return to menu' : False,
    'menu' : False
}

# Punctuation the terminal will pause at
EOL_PUNCT = {'.', '!', '?', '\n'}

# function definitions
# 'Talking' Print, prints with delay
def tprint(str):
    for i in str:
        cprint(i, 'yellow', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

# 'Talking' Input
def tinput(str):
    for i in str:
        cprint(i, 'cyan', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    user_input = input('')
    return user_input

# Variation of input that adds ellipses with a longer delay at the end
def thinking(str, num):
    for i in str:
        cprint(i, 'yellow', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    for i in range(0, num):
        cprint('.', 'yellow', 'on_grey', end='', flush = True)
        time.sleep(PAUSE_DELAY)
    print('')

# Variation of tprint that doesn't do a long pause at periods (to avoid stops in floating point numbers)
def tprint_float(str):
    for i in str:
        cprint(i, 'yellow', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT and i != '.':
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

# Print Welcome message
def welcome_msg():
    tprint(f'Welcome! My name is {APPNAME}!')

# Prints count down from timer
def countdown(timer):
    tprint(f'Get ready for the next sentence in {timer} seconds!')
    time.sleep(PAUSE_DELAY)
    for sec in range(timer, 0, -1):
        cprint(f'{sec}' + sec * '.', 'yellow', 'on_grey')
        time.sleep(TIMER_DELAY)
    cprint(COUNTDOWN_MSG, 'yellow', 'on_grey')

# Returns the length of the longer sequence of two
def longer_len(str1, str2):
    if len(str1) >= len(str2):
        return len(str1)
    else:
        return len(str2)

# Takes a correct sentecne and a user input and marks up differences in the user input
def markup_scoring(correct, user):
    adj_user = []
    # Compare correct & user and format character by character
    for cindex, char in enumerate(correct):
        try:
            # Format correct characters in green
            if char == user[cindex]:
                adj_user.append(colored(user[cindex], 'green', 'on_grey'))
            else:
                # Change background colour for incorrect spaces for visibility
                if user[cindex] == ' ':
                    adj_user.append(colored(' ', 'red', 'on_red', attrs = ['bold']))
                # Format incorrect characters in red
                else:
                    adj_user.append(colored(user[cindex], 'red', 'on_grey', attrs = ['bold']))
        # If len(correct) > len(user), the rest of the user input must be incorrect
        except:
            adj_user.append(colored(' ', 'red', 'on_red', attrs = ['bold']))
    # Logic for when the user has entered too many characters
    if len(user) > len(correct):
        for i in range(cindex + 1, len(user)):
            if user[i] == ' ':
                adj_user.append(colored(' ', 'red', 'on_red', attrs = ['bold']))
            else:
                adj_user.append(colored(user[i], 'red', 'on_grey', attrs = ['bold']))
    # Print sentences
    print('Given Sentence: ' + colored(correct, 'white', 'on_grey'))
    print('What you wrote: ' + ''.join(adj_user))

# Main execution for quick play
def quickplay():
    play = True
    tprint('Let\'s Play!')
    while play:
        total_time_sec = 0
        total_correct_chars = 0
        total_incorrect_chars = 0
        sentence_list = SENTENCE_LIST
        try:
            sess_sentences = random.sample(sentence_list, GAMELENGTH)
        except:
            sess_sentences = random.sample(sentence_list, len(pangrams.pangrams))
        sess_len = len(sess_sentences)
        for sindex, sentence in enumerate(sess_sentences, 1):
            tinput(f'Press ENTER when ready')
            countdown(COUNTDOWN_TIMER)
            seg_start = time.time()
            cprint(sentence, 'white', 'on_grey')
            sentence_length = len(sentence)
            sentence_correct_chars = 0
            sentence_incorrect_chars = 0
            user_type = input('')
            seg_end = time.time()
            seg_time = seg_end - seg_start
            for cindex, char in enumerate(sentence):
                try:
                    if char == user_type[cindex]:
                        sentence_correct_chars += 1
                    else:
                        sentence_incorrect_chars += 1
                except:
                    sentence_incorrect_chars += 1
            if sentence_length < len(user_type):
                sentence_incorrect_chars += len(user_type) - sentence_length
            sentence_accuracy = sentence_correct_chars / (sentence_correct_chars + sentence_incorrect_chars)
            tprint_float(f'This sentence was typed with {(sentence_accuracy * 100):.02f}% accuracy!')
            total_time_sec += seg_time
            total_correct_chars += sentence_correct_chars
            total_incorrect_chars += sentence_incorrect_chars
            if sentence_incorrect_chars > 0:
                markup_scoring(sentence, user_type)
            if sindex == sess_len:
                tinput(f'Press ENTER to continue to results')
        total_time_min = total_time_sec / 60
        cpm = total_correct_chars / total_time_min
        wpm = cpm / CPW
        overall_accuracy = total_correct_chars / (total_correct_chars + total_incorrect_chars)
        thinking('Great work! Calculating Performance', COUNTDOWN_TIMER)
        tprint_float(f'Your typing speed is {wpm:.02f}WPM (words per minute)!')
        tprint_float(f'Your overall accuracy was {(overall_accuracy * 100):.02f}%!')
        while True:
            next = tinput('''Would you like to:
1. Play Again
2. Return to Main Menu
''').lower().strip()
            try:
                play = EOG_ALIASES[next]
                break
            except:
                tprint('Sorry, I didn\'t understand. Could you rephrase that?')

def mm_msg():
    tprint_float(
f'''This is the main menu
Reminder that your available commands are:
1. Quickplay: A quick test using from a pre-defined list of sentences
2. Help: An explanation of the different menu options
3. Exit: Exits program
''')

def help():
    tprint('help content')
    tinput('Press ENTER to return to the main menu')

def app_exit():
    tprint('Thanks for playing!')
    exit()

def main():
    welcome_msg()
    while True:
        mm_msg()
        user_in = tinput('Input Command: ').lower().strip()
        if user_in in MENU_ALIASES:
            eval(f'{MENU_ALIASES[user_in]}()')
        else:
            tprint('Sorry, I didn\'t understand. Could you rephrase that?')

# main program flow with sys.argv tests
# 'normal' run
if len(sys.argv) == 1:
    main()
elif len(sys.argv) > 2:
    print('./main.py only takes 1 argument. Please use --help or refer to README.md for help.')
else:
    if sys.argv[1] == '--debug':
        APPNAME = 'Terminal Typing Test: Testing Tool'
        GAMELENGTH = 3
        COUNTDOWN_TIMER = SPEECH_DELAY = PAUSE_DELAY = 0
        SENTENCE_LIST = pangrams.pangrams_test
        main()
    elif sys.argv[1] == '--help':
        print('--help content')
    else:
        print('Valid arguments to ./main.py are: --debug & --help')
    

