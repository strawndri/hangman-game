from lib import style as s
from lib import word as w
from time import sleep

secret_word = []
letters = []

def man(check=True):
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
        if (i == 2 or i == 3 or i == 7):
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
        letters.append(l)

    s.write(f'    Letters:', 'blue', br=False)
    for item in letters:
        print(item, end=', ')

    s.write(f'Theme: {theme.upper()}  -->   ', 'yellow', br=False)

    for item in secret_word:
        print(item, end=' ')
    s.write(' ')

    if (l not in word):
        return False
    else:
        return True


def play():
    s.write('WELCOME TO THE GAME: HANGMAN', 'blue', True)
    s.write("Wait for a minute, we're choosing a word...", 'blue')
    sleep(3)
    print('\n' * 20)
    writeLetters()
    check = True
    while True:
        man(check)
        print('\n' * 12)
        s.write('> Choose a letter: ', 'purple', br=False)
        letter = input()
        check = writeLetters(letter)



