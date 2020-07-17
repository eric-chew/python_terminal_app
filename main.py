#/usr/sbin/python

# imports & modules
import time
import random
import pangrams
from os import system
from termcolor import colored, cprint

# statics & data structures
APPNAME = 'Terminal Typing Test'
GAMELENGTH = 3
COUNTDOWN_TIMER = 3
COUNTDOWN_MSG = 'GO!'
SPEECH_DELAY = 0.02
PAUSE_DELAY = 0.75
CPW = 5 # Characters per word
TIMER_DELAY = 1

MENU_ALIASES = {
    '1' : 'quickplay',
    'quickplay' : 'quickplay',
    '3' : 'help',
    'help' : 'help',
    '4' : 'app_exit',
    'exit' : 'app_exit',
}

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

EOL_PUNCT = {'.', '!', '?', '\n'}

# function definitions
def tprint(str):
    for i in str:
        cprint(i, 'yellow', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

def tinput(str):
    for i in str:
        cprint(i, 'cyan', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    user_input = input('')
    return user_input

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

def tprint_float(str):
    for i in str:
        cprint(i, 'yellow', 'on_grey', end = '', flush = True)
        if i in EOL_PUNCT and i != '.':
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

def welcome_msg():
    tprint(f'Welcome! My name is {APPNAME}!')

def countdown(timer):
    tprint(f'Get ready for the next sentence in {timer} seconds!')
    time.sleep(PAUSE_DELAY)
    for sec in range(timer, 0, -1):
        cprint(f'{sec}' + sec * '.', 'yellow', 'on_grey')
        time.sleep(TIMER_DELAY)
    cprint(COUNTDOWN_MSG, 'yellow', 'on_grey')

def longer_len(str1, str2):
    if len(str1) >= len(str2):
        return len(str1)
    else:
        return len(str2)

def quickplay():
    play = True
    tprint('quickplay activated.')
    while play:
        total_time_sec = 0
        total_correct_chars = 0
        total_incorrect_chars = 0
        try:
            sess_sentences = random.sample(pangrams.pangrams_test, GAMELENGTH)
        except:
            sess_sentences = random.sample(pangrams.pangrams_test, len(pangrams.pangrams_test))
        sess_len = len(sess_sentences)
        for sindex, sentence in enumerate(sess_sentences, 1):
            if sindex < sess_len:
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
    tprint(
f'''Reminder that your available commands are:
1. Quickplay: A quick test using from a pre-defined list of sentences
2. TBI
3. Help: An explanation of the different menu options
4. Exit: Exits program
''')

def help():
    tprint('printing help message.')

def app_exit():
    tprint('Thanks for playing!')
    exit()

# main program flow
welcome_msg()
while True:
    mm_msg()
    user_in = tinput('Input Command: ').lower().strip()
    if user_in in MENU_ALIASES:
        eval(f'{MENU_ALIASES[user_in]}()')
    else:
        tprint('Sorry, I didn\'t understand. Could you rephrase that?')
    

