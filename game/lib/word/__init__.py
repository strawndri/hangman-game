from random import choice, randint

# choose a specific theme and a word
def chooseWord():
    words = {'food': ['apple', 'avocado', 'banana', 'beet', 'blueberry', 'bacon', 'bread', 'broccoli',
                      'cucumber', 'cheese', 'jellybean', 'lemon', 'lime', 'milk', 'potato', 'rice', 'sausage',
                      'strawberry', 'soda', 'coconut', 'coffee', 'cake', 'cabbage', 'donut', 'egg', 'french fries',
                      'fungi', 'grape', 'guava', 'hamburger', 'honey', 'hot dog', 'lollipop', 'mango', 'melon',
                      'orange', 'onion', 'pie', 'tomato', 'watermelon', 'yogurt', 'zucchini', 'eggplant', 'pumpkin',
                      'cauliflower', 'garlic', 'onion', 'carrot', 'pepper', 'kiwi', 'peach', 'passion fruit', 'papaya',
                      'pear', 'pineapple', 'tea', 'juice', 'water', 'wine', 'cookie', 'cupcake', 'ice cream', 'chocolate',
                      'toast', 'pancakes'],

             'animal': ['cat', 'cow', 'dog', 'fish', 'frog', 'horse', 'pig', 'turtle', 'penguin', 'elephant', 'lion',
                        'bee', 'monkey', 'alligator', 'snake', 'wolf', 'tiger', 'spider', 'worm', 'mice', 'mouse',
                        'butterfly', 'chicken', 'crab', 'crocodile', 'dragonfly', 'camel', 'duck', 'owl', 'whale',
                        'shark', 'bat', 'iguana', 'bear', 'giraffe', 'jellyfish', 'ladybird'],

             'color': ['blue', 'yellow', 'green', 'red', 'purple', 'pink', 'gray', 'orange', 'white', 'black',
                       'brown', 'turquoise', 'fuchsia', 'gold', 'lilac'],

             'object': ['pen', 'cup', 'notebook', 'paper', 'shoe', 'glasses', 'book', 'air conditioner', 'bag',
                        'bed', 'chair', 'computer', 'dishwasher', 'lamp', 'microwave', 'towel', 'umbrella',
                        'vacuum cleaner', 'television', 'ring', 'bicycle', 'ball', 'earring', 'necklace', 'cup',
                        'cellphone', 'spoon', 'mirror', 'knife', 'camera', 'window', 'bin', 'backpack', 'guitar',
                        'newspaper', 'sofa', 'keyboard', 'eraser', 'broom', 'bookshelf', 'pillow', 'toilet'],

             'place': ['house', 'hospital', 'restaurant', 'bookstore', 'library', 'factory', 'movie theater', 'museum',
                       'gas station', 'school', 'office', 'supermarket', 'hotel', 'fire department', 'church', 'square',
                       'cafe', 'bank', 'pharmacy', 'hair salon', 'barber shop', 'laundry'],

             'job': ['teacher', 'postman', 'postwoman', 'vet', 'actor', 'actress', 'musician', 'nurse', 'barber', 'dentist',
                     'farmer', 'plumber', 'chemist', 'policeman', 'policewoman', 'painter', 'detective', 'artist', 'cleaner',
                     'baker', 'singer', 'driver', 'doctor', 'pilot', 'waitress', 'waiter', 'dancer', 'gardener', 'dustman',
                     'dustwoman', 'astronaut', 'businesswoman', 'businessman', 'cook', 'firefighter', 'cashier']}

    theme = choice(['food', 'animal', 'color', 'object', 'place'])
    item = randint(0, (len(theme) - 1))
    word = words[theme][item]

    return theme, word.upper()
