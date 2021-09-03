from random import choice, randint

def chooseWord():
    words = {'food': ['apples', 'avocado', 'banana', 'beet', 'blueberry', 'bacon', 'bread', 'broccoli',
                      'cucumber', 'cheese', 'jellybean', 'lemon', 'lime', 'milk', 'potato', 'rice', 'sausage',
                      'strawberry', 'soda'],
             'animal': ['cat', 'cow', 'dog', 'fish', 'frog', 'horse', 'pig', 'turtle'],
             'color': ['blue', 'yellow', 'green', 'red', 'purple', 'pink', 'gray', 'orange', 'white', 'black',
                       'brown', 'turquoise'],
             'object': ['pen', 'cup', 'notebook', 'paper', 'shoe', 'glasses', 'book'],
             'place': ['house', 'hospital', 'restaurant', 'bookstore', 'library', 'factory', 'movie theater', 'museum',
                       'gas station', 'school', 'office']}


    return words['place'][6]