from lib import style as s
from lib import word as w
from time import sleep
import pygame
pygame.init()

secret_word = []
letters = []
man = ['', '', '', '', '', '', '', '']

correct = pygame.mixer.Sound('./assets/correct.mp3')
error = pygame.mixer.Sound('./assets/error.mp3')
congratulations = pygame.mixer.Sound('./assets/congratulations.mp3')
game_over = pygame.mixer.Sound('./assets/game_over.mp3')

def loading():

    for item in range(0, 26):
        print(f'\r{item * 4}%', end=' ')
        print('▒▒▒▒▒▒' * item, end='')
        sleep(0.3)

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

    if (l == 'none'):
        n = 3
        c = True
    elif (l not in word):
        c = False
        n = 2
    else:
        c = True
        n = 1

    return c, n


def message(letters_list, t, sw, number=0):

    if number == 1:
        correct.play()
        s.write(" Well done! Let's continues...", 'green', line=True)
    elif number == 2:
        error.play()
        s.write(" Poor you... wrong letter :( ", 'red', line=True)
    elif number == 3:
        error.play()
        s.write(' (!) ERROR -> Insert a correct value.', 'red', line=True)
    elif number == 4:
        error.play()
        s.write(" (!) ERROR -> You've just written this word. Try again.", 'red', line=True)

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
    s.write('Write "stop" to stop the game.', 'blue')
    print('\n' * 10)
    loading()

    # --- variables
    theme, word = w.chooseWord()
    error = 0
    check = ' '
    num = 0
    # -------------

    print('\n' * 10)
    s.write(" HANGMAN ", 'blue', line=True)
    checkLetters(theme, word)
    message(letters, theme, secret_word, num)
    while True:

        if check == ' ':
            hanged_man(check)
        elif (check == True):
            hanged_man(check)
        else:
            hanged_man(check, error)
            error += 1
        print('\n' * 8)

        s.write('> Choose a letter: ', 'purple', br=False)
        letter = input()


        if not letter.isalpha() or len(letter) > 1 or letter in letters:
            letter = 'none'

        check, num = checkLetters(theme, word, letter)
        message(letters, theme, secret_word, num)

        if not '_' in secret_word:
            congratulations.play()
            s.write('CONGRATULATIONS! You got it!', 'green', line=True)
            s.write(f'WORD: {word}', 'blue', line=True)
            print('\n' * 15)
            sleep(2)
            break
        elif (error == 8):
            game_over.play()
            s.write('GAME OVER', 'red', line=True)
            s.write(f'WORD: {word.upper()}', 'blue', line=True)
            print('\n' * 15)
            sleep(2)
            break



