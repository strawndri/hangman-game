from lib import style as s

s.write('WELCOME TO THE GAME: HANGMAN', 'blue', True)



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

    man = ['',
           '',
           '',
           '',
           '',
           '',
           '',
           '']

    for i, item in enumerate(man):
        if (i == 2 or i == 3 or i == 6):
            print(item, end='')
        else:
            print(item)



man()

s.write('Deseja jogar?', 'yellow', True)