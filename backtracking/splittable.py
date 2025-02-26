"""
Determing if given string is splittables in to other words.
"""

string = 'BOTHEARTHANDSATURNSPIN'

def is_word(string: str) -> bool:
    #might be more words in string, but enough for this problem
    words = ['BOT', 'BOTH','HE', 'THE', 'HEAR', 'HEART', 'EAR', 'EARTH', 'ART', 'HAND', 'HANDS', 'AND', 'SATURN', 'AT', 'TURN', 'URN', 'SPIN', 'PIN', 'IN'] 
    return string in words

def is_splittable(string: str):
    n = len(string)
    if n == 0:
        return True
    for i in range(1, n + 1):
        if is_word(string[:i]):
            if is_splittable(string[i:]):
                return True
    return False

print(is_splittable(string))

