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


def writeLetters(theme, word, l='_'):

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


    s.write(f'LETTERS: ', 'blue', br=False)
    for item in letters:
        print(item, end=', ')

    s.write(f'Theme: {theme.upper()}  -->   ', 'yellow', br=False)

    for item in secret_word:
        print(item, end=' ')
    s.write(' ')


    if (l not in word and l != 'none'):
        return False
    else:
        return True



def play():
    s.write('WELCOME TO THE GAME: HANGMAN', 'blue', True)
    s.write("Wait for a minute, we're choosing a word...", 'blue')
    #sleep(3)
    theme, word = w.chooseWord()
    print('\n' * 20)
    writeLetters(theme, word)
    check = True
    num = 0
    while True:

        if (check):
            hanged_man(check)
        else:
            hanged_man(check, num)
            num += 1
        print('\n' * 8)

        s.write('> Choose a letter: ', 'purple', br=False)
        letter = input()

        if check == False:
            s.write(" Poor you... wrong letter :( ", 'red', line=True)
        else:
            s.write(" Well done! Let's continues...", 'green', line=True)

        if not letter.isalpha() or len(letter) > 1:
            print('\n' * 5)
            s.write(' (!) ERROR -> Insert a correct value.', 'red', line=True)
            letter = 'none'

        check = writeLetters(theme, word, letter)





