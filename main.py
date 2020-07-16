# imports & modules
import time
import random
import pangrams

# statics & data structures
APPNAME = 'ICBIN TTT'
GAMELENGTH = 3
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
    print(f'Get ready for the next sentence in {timer} seconds!')
    time.sleep(1)
    for sec in range(timer, 0, -1):
        print(sec)
        time.sleep(1)
    print(COUNTDOWN_MSG)

def longer_len(str1, str2):
    if len(str1) >= len(str2):
        return len(str1)
    else:
        return len(str2)

def quickplay():
    print('quickplay activated')
    sess_char_count = 0
    total_time_sec = 0
    len_total = 0
    for sentence in random.sample(pangrams.pangrams, GAMELENGTH):
        countdown(COUNTDOWN_TIMER)
        seg_start = time.time()
        sentence_length = len(sentence)
        sentence_correct_chars = 0
        user_type = input(f'Sentence is:\n{sentence}\n')
        seg_end = time.time()
        seg_time = seg_end - seg_start
        for index, char in enumerate(sentence):
            try:
                if char == user_type[index]:
                    sentence_correct_chars += 1
            except:
                pass
        sentence_accuracy = sentence_correct_chars / longer_len(sentence, user_type)
        print(f'This sentence was typed with {(sentence_accuracy * 100):.02f}% accuracy!')
        sess_char_count += sentence_correct_chars
        total_time_sec += seg_time
        len_total += longer_len(sentence, user_type)
    total_time_min = total_time_sec / 60
    cpm = sess_char_count / total_time_min
    wpm = cpm / 5
    overall_accuracy = sess_char_count / len_total
    print('Great work! Tabulating results', end = '')
    for i in range(0, COUNTDOWN_TIMER):
        print('.', end='')
        time.sleep(1)
    print(f'Your CPM (characters per minute) is {cpm:.02f}!')
    print(f'Your WPM (words per minute) is {wpm:.02f}!')
    print(f'Your overall accuracy was {(overall_accuracy * 100):.02f}%!')

def help():
    print('printing help message')

def app_exit():
    print('Thanks for playing!')
    exit()

# main program flow
welcome_msg()
# continue_playing = True
while True:
    user_in = input('Input Command: ')
    if user_in in MENU_ALIASES:
        eval(f'{MENU_ALIASES[user_in]}()')
    else:
        print('Sorry, I didn\'t understand. Could you rephrase that?')
    

