from lib import style as s
from lib import word as w
from time import sleep

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

def writeLetters(l='none'):

    theme, word = w.chooseWord()
    secret_word = []

    for item in word:
        if(item == l):
            print(l)
            secret_word.append(l)
        elif (item == ' '):
            secret_word.append(' * ')
        else:
            secret_word.append('_')


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
        print('\n' * 100)
        play()



