
colors = {'none': '\033[01;m',
             'red': '\033[01;31m',
             'green': '\033[01;32m',
             'yellow': '\033[01;33m',
             'blue': '\033[01;34m',
             'purple': '\033[01;35m'}

def write(text, color='none', line=False, br=True):

    print(colors[color])

    if (line == True):
        print('-' * 155)
        print(text.center(155))
        print('-' * 155, colors['none'])
    elif (br == False):
        print(f'{text:>74}', end=' ')
    else:
        print(text.center(155), colors['none'])







