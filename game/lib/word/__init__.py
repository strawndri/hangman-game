from random import choice, randint


def chooseWord():
    words = {'food': ['apple', 'avocado', 'banana', 'beet', 'blueberry', 'bacon', 'bread', 'broccoli',
                      'cucumber', 'cheese', 'jellybean', 'lemon', 'lime', 'milk', 'potato', 'rice', 'sausage',
                      'strawberry', 'soda'],
             'animal': ['cat', 'cow', 'dog', 'fish', 'frog', 'horse', 'pig', 'turtle'],
             'color': ['blue', 'yellow', 'green', 'red', 'purple', 'pink', 'gray', 'orange', 'white', 'black',
                       'brown', 'turquoise'],
             'object': ['pen', 'cup', 'notebook', 'paper', 'shoe', 'glasses', 'book'],
             'place': ['house', 'hospital', 'restaurant', 'bookstore', 'library', 'factory', 'movie theater', 'museum',
                       'gas station', 'school', 'office']}

    theme = choice(['food', 'animal', 'color', 'object'', place'])
    item = randint(0, (len(theme) - 1))
    word = words[theme][item]

    return theme, word.upper()
