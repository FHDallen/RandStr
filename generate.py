### generate.py
### Oregon State University - CS 361
### Dylan Allen

import random

def generate_string(iterator: int):
    """Generates a random string of iterator length
    
    Params: 
        iterator:: positive integer   

    Returns: 
        string:: a random string of X length, where X = iterator
    """

    char_list = [] 

    while iterator > 0:
        iterator -= 1
        char = chr(random.randint(33,126)) # Generates a random ASCII character
        char_list.append(char)
    
    return "".join(char_list)
