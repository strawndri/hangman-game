from lib import style as s
from lib import word as w
from time import sleep
import sys

secret_word = []
letters = []
man = ['', '', '', '', '', '', '', '']

def hanged_man(check=True, n=0):
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

    list = [head, rope, arm_left, body, arm_right, body2, leg_left, leg_right]

    if check == False:
        man.pop()
        man.insert(n, list[n])

    for i, item in enumerate(man):
        if (i == 2 or i == 3 or i == 6):
            print(item, end='')
        else:
            print(item)


def checkLetters(theme, word, l='_'):
    if (l == '_'):
        for item in word:
            if (item == ' '):
                secret_word.append('*')
            else:
                secret_word.append('_')
    elif l != 'none':
        for i, item in enumerate(word):
            if (l == item):
                secret_word.pop(i)
                secret_word.insert(i, l)
        letters.append(l)

    if (l not in word and l != 'none'):
        c = False
    else:
        c = True

    return c


def message(letters_list, t, sw, number=0):

    if number == 1:
        s.write(" Well done! Let's continues...", 'green', line=True)
    elif number == 2:
        s.write(" Poor you... wrong letter :( ", 'red', line=True)
    elif number == 3:
        s.write(' (!) ERROR -> Insert a correct value.', 'red', line=True)

    s.write(f'LETTERS: ', 'blue', br=False)
    for item in letters_list:
        print(item, end=', ')

    s.write(f'Theme: {t.upper()}  -->   ', 'yellow', br=False)

    for item in sw:
        print(item, end=' ')
    s.write(' ')


def play():
    s.write('WELCOME TO THE GAME: HANGMAN', 'blue', True)
    s.write("Wait for a minute, we're choosing a word...", 'blue')
    # sleep(3)

    # --- variables
    theme, word = w.chooseWord()
    error = 0
    check = ' '
    n = 0
    # -------------

    print('\n' * 10)
    s.write(" HANGMAN ", 'blue', line=True)
    checkLetters(theme, word)
    message(letters, theme, secret_word, n)
    while True:

        if check == ' ':
            hanged_man(check)
        elif (check == True):
            hanged_man(check)
            n = 1
        else:
            hanged_man(check, error)
            error += 1
            n = 2
        print('\n' * 8)

        s.write('> Choose a letter: ', 'purple', br=False)
        letter = input()

        if not letter.isalpha() or len(letter) > 1:
            n = 3
            letter = 'none'

        check = checkLetters(theme, word, letter)
        message(letters, theme, secret_word, n)

