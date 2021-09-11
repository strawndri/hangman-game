from lib import style as s
from lib import word as w
from time import sleep
import pygame
pygame.init()


# variables ----------------------------------------------------
secret_word = []
letters = []
man = ['', '', '', '', '', '', '', '']

# audios
correct = pygame.mixer.Sound('./assets/correct.mp3')
error = pygame.mixer.Sound('./assets/error.mp3')
congratulations = pygame.mixer.Sound('./assets/congratulations.mp3')
game_over = pygame.mixer.Sound('./assets/game_over.mp3')
stop = pygame.mixer.Sound('./assets/stop.mp3')
# --------------------------------------------------------------


# Loading bar
def loading():
    for item in range(0, 26):
        print(f'\r{item * 4}%', end=' ')
        print('▒▒▒▒▒▒' * item, end='')
        sleep(0.3)

# Make the hanged man when the user insert a wrong letter
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

    # auxiliary list
    list = [head, rope, arm_left, body, arm_right, body2, leg_left, leg_right]

    # add parts of the body
    if check == False:
        man.pop()
        man.insert(n, list[n])

    # print the man
    for i, item in enumerate(man):
        if (i == 2 or i == 3 or i == 6):
            print(item, end='')
        else:
            print(item)

# check if the letter is in the chosen word
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

# shows a message on the top of the screen
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

    # Used letters
    s.write(f'LETTERS: ', 'blue', br=False)
    for item in letters_list:
        print(item, end=', ')

    s.write(f'Theme: {t.upper()}  -->   ', 'yellow', br=False)

    for item in sw:
        print(item, end=' ')
    s.write(' ')

# Run the game
def play():

    # Initial Message
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
    end = False
    # -------------

    # First Message
    print('\n' * 10)
    s.write(" HANGMAN ", 'blue', line=True)
    checkLetters(theme, word)
    message(letters, theme, secret_word, num)

    # Ask and Check letters
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
        letter = input().upper().strip()

        if ((not letter.isalpha()) or (len(letter) > 1) or (letter in letters)):
            if letter != 'STOP':
                letter = 'none'

        check, num = checkLetters(theme, word, letter)

        # End Messages -----------------

        if (letter == 'STOP'):
            stop.play()
            s.write('THE GAME WAS BROKE UP', 'yellow', line=True)
            end = True
        elif (not '_' in secret_word):
            congratulations.play()
            s.write('CONGRATULATIONS! You got it!', 'green', line=True)
            end = True
        elif (error == 8):
            game_over.play()
            s.write('GAME OVER', 'red', line=True)
            end = True

        if end:
            s.write(f'WORD: {word}', 'blue', line=True)
            print('\n' * 15)
            sleep(2)
            break

        # Return the message on the top
        message(letters, theme, secret_word, num)



