'''Lab4_b.py - has an assortment of functions to fulfill part B of lab 4'''

import tkinter
import random

# B.1
def random_size(a, b):
    '''Takes two even integers as arguments and returns
    a random even integer greater than or equal to the first arg and
    smaller than or equal to the second'''
    assert a >= 0 and b >= 0 and a % 2 == 0 and b % 2 == 0 and a <= b
    output = random.randint(a / 2, b / 2) * 2
    assert output % 2 == 0
    return output

# B.2
def random_position(max_x, max_y):
    '''Takes two integers as arguments, a max X and Y, and returns a tuple of
    two randomly chosen x and y coordinates that are smaller than max_x and
    max_y, respectively, but both greater than zero.'''
    assert max_x >= 0 and max_y >= 0
    return (random.randint(0, max_x), random.randint(0, max_y))

# B.3
def random_color():
    '''Takes no arguments. Returns a random color value that is recognized
    by tkinter package. Is of the form #RRGGBB. Values are in hexadecimal.'''
    color = ''
    hexaList = [0, 1, 2 , 3, 4, 5, 6 ,7 ,8 ,9, 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += str(random.choice(hexaList))
    return '#' + color

# B.4
def count_values(dct):
    '''takes a single dictionary as an argument and
    returns a count of the number of distinct values it contains.'''
    values = list(dct.values())
    distinct = []
    for val in values:
        if val not in distinct:
            distinct.append(val)
    return len(distinct)

# B.5
def remove_value(dct, val):
    '''takes a dictionary and an arbitrary item which
    could be a value in the dictionary. It removes all key/value pairs
    from the dictionary which have that value.'''
    toRemove = []
    keys = list(dct.keys())
    for key in keys:
        if dct[key] == val:
            toRemove.append(key)
    for i in range(len(toRemove)):
        del dct[toRemove[i]]

# B.6
def split_dict(dct):
    '''takes as its argument a dictionary which uses strings as keys and
    returns a tuple of two dictionaries whose
    key/value pairs are from the original dictionary:
    those whose keys start with the letters a-m (lower- or uppercase)
    and those whose keys start with the letters n-z (lower- or uppercase).'''
    aToM = {}
    nToZ = {}
    for key in dct:
        if 'n' <= key[0] <= 'z'  or 'N' <= key[0] <= 'Z':
            nToZ[key] = dct[key]
        elif 'a' <= key[0] <= 'm' or 'A' <= key[0] <= 'M':
            aToM[key] = dct[key]
    return (aToM, nToZ)

# B.7
def count_duplicates(dct):
    '''takes a dictionary as an argument and returns the
    number of values that appear two or more times.'''
    values = list(dct.values())
    distinct = []
    duplicate = []
    for val in values:
        if val not in distinct:
            distinct.append(val)
        elif val not in duplicate:
            duplicate.append(val)
    return len(duplicate)
