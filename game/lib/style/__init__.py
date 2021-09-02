
colors = {'none': '\033[01;m',
             'red': '\033[01;31m',
             'green': '\033[01;32m',
             'yellow': '\033[01;33m',
             'blue': '\033[01;34m'}

def write(text, color, line=False):

    print(colors[color])

    if (line == True):
        print('-' * 155)
        print(text.center(155))
        print('-' * 155)

    else:
        print(text.center(155))

    print(colors['none'])






