#/usr/sbin/python

# imports & modules
import time
import random
import pangrams
from termcolor import colored, cprint

# statics & data structures
APPNAME = 'ICBIN TTT'
GAMELENGTH = 3
COUNTDOWN_TIMER = 3
COUNTDOWN_MSG = 'GO!'
SPEECH_DELAY = 0.02
PAUSE_DELAY = 0.75
CPW = 5 # Characters per word
TIMER_DELAY = 1

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
    tprint(f'Welcome to {APPNAME}!')

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
    tprint('quickplay activated.')
    total_time_sec = 0
    total_correct_chars = 0
    total_incorrect_chars = 0
    try:
        sess_sentences = random.sample(pangrams.pangrams_test, GAMELENGTH)
    except:
        sess_sentences = random.sample(pangrams.pangrams_test, len(pangrams.pangrams_test))
    sess_len = len(sess_sentences)
    for sindex, sentence in enumerate(sess_sentences, 1):
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
        if sindex < sess_len:
            tinput(f'Press ENTER to continue')
    total_time_min = total_time_sec / 60
    cpm = total_correct_chars / total_time_min
    wpm = cpm / CPW
    overall_accuracy = total_correct_chars / (total_correct_chars + total_incorrect_chars)
    thinking('Great work! Calculating Performance', COUNTDOWN_TIMER)
    tprint_float(f'Your typing speed is {wpm:.02f}WPM (words per minute)!')
    tprint_float(f'Your overall accuracy was {(overall_accuracy * 100):.02f}%!')

def help():
    tprint('printing help message.')

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
    

