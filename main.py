# imports & modules
import time
import random
import pangrams
from termcolor import cprint

# statics & data structures
APPNAME = 'ICBIN TTT'
GAMELENGTH = 1
COUNTDOWN_TIMER = 3
COUNTDOWN_MSG = 'GO!'
SPEECH_DELAY = 0.02
PAUSE_DELAY = 1
CPW = 5 # Characters per word
TIMER_DELAY = 0.5

MENU_ALIASES = {
    'quickplay' : 'quickplay',
    'q' : 'quickplay', # consider removing
    'help' : 'help',
    'exit' : 'app_exit'
}

EOL_PUNCT = {'.', '!', '?'}

# function definitions
def tprint(str):
    for i in str:
        print(i, end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

def tinput(str):
    for i in str:
        print(i, end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    user_input = input('')
    return user_input

def thinking(str, num):
    for i in str:
        print(i, end = '', flush = True)
        if i in EOL_PUNCT:
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    for i in range(0, num):
        print('.', end='', flush = True)
        time.sleep(PAUSE_DELAY)
    print('')

def tprint_float(str):
    for i in str:
        print(i, end = '', flush = True)
        if i in EOL_PUNCT and i != '.':
            time.sleep(PAUSE_DELAY)
        else:
            time.sleep(SPEECH_DELAY)
    print('')

def welcome_msg():
    tprint(f'Welcome to {APPNAME}!')

def countdown(timer):
    print(f'Get ready for the next sentence in {timer} seconds!')
    time.sleep(1)
    for sec in range(timer, 0, -1):
        print(f'{sec}' + sec * '.')
        time.sleep(1)
    print(COUNTDOWN_MSG)

def longer_len(str1, str2):
    if len(str1) >= len(str2):
        return len(str1)
    else:
        return len(str2)

def quickplay():
    tprint('quickplay activated')
    total_time_sec = 0
    total_correct_chars = 0
    total_incorrect_chars = 0
    for sentence in random.sample(pangrams.pangrams, GAMELENGTH):
        countdown(COUNTDOWN_TIMER)
        seg_start = time.time()
        print(sentence)
        sentence_length = len(sentence)
        sentence_correct_chars = 0
        sentence_incorrect_chars = 0
        user_type = input('')
        seg_end = time.time()
        seg_time = seg_end - seg_start
        for index, char in enumerate(sentence):
            try:
                if char == user_type[index]:
                    sentence_correct_chars += 1
                else:
                    sentence_incorrect_chars += 1
            except:
                break
        if sentence_length > len(user_type):
            sentence_incorrect_chars += sentence_length - len(user_type)
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

def help():
    tprint('printing help message')

def app_exit():
    tprint('Thanks for playing!')
    exit()

# main program flow
welcome_msg()
# continue_playing = True
while True:
    user_in = tinput('Input Command: ')
    if user_in in MENU_ALIASES:
        eval(f'{MENU_ALIASES[user_in]}()')
    else:
        tprint('Sorry, I didn\'t understand. Could you rephrase that?')
    

