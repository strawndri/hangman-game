from lib import style as s
from lib import word as w
from time import sleep
import sys

secret_word = []


def man():
    print(f'''{" ":>53}==================================================
              {" ":>64}||''')

    head = f' {"(╥﹏╥)":>80}'
    rope = f' {"≡≡≡≡":>80}'
    arm_left = f'{" /":>77}'
    arm_right = '\\'
    body = f'{"|  |"}'
    body2 = f'{"|  |":>81}'
    leg_left = f'{"  /":>78}'
    leg_right = f'  \\'

    man = ['', '', '', '', '', '', '', '']

    for i, item in enumerate(man):
        if (i == 2 or i == 3 or i == 6):
            print(item, end='')
        else:
            print(item)

def writeLetters(l='_'):

    theme, word = w.chooseWord()

    if (l == '_'):
        for item in word:
            if (item == ' '):
                secret_word.append('*')
            else:
                secret_word.append('_')
    else:
        for i, item in enumerate(word):
            if (item == l):
                secret_word.pop(i)
                secret_word.insert(i, l)

    s.write(f'Theme: {theme.upper()}  -->   ', 'yellow', br=False)

    for item in secret_word:
        print(item, end=' ')
    s.write(' ')






def play():
    s.write('WELCOME TO THE GAME: HANGMAN', 'blue', True)
    s.write("Wait for a minute, we're choosing a word...", 'blue')
    sleep(1)
    writeLetters()
    man()
    while True:
        s.write('> Choose a letter: ', 'purple', br=False)
        letter = input()
        writeLetters(letter)


