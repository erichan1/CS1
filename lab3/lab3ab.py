#Lab 3 Parts A and B.
'''Module for part a of lab3 of CS1. Various functions depending on the problems.'''

# A.1
def list_reverse(lst):
    '''Takes a single list as argument. Copies that list into a new
    list and returns the reversed list'''
    returnList = lst[:]
    returnList.reverse()
    return returnList

# A.2
def list_reverse2(lst):
    '''Does the same thing as list_reverse but uses a for loop instead'''
    returnList = []
    for i in range(len(lst) - 1, -1, -1):
        returnList.append(lst[i])
    return returnList

# A.3
def file_info(fileName):
    '''Takes a filename as an argument, and returns the number of lines,
    characters, and words in that file in the form of a tuple, like so:
    (lines, characters, words)'''
    txtfile = open(fileName, 'r')
    lines = 0
    words = 0
    characters = 0
    for line in txtfile:
        lines += 1
        characters += len(line)
        words += len(line.split())
    txtfile.close()
    return (lines, words, characters)

# A.4
def file_info2(fileName):
    '''Takes a filename as an argument, and returns the number of lines,
    characters, and words in that file in a dictionary in something like
    {'lines' : 100, 'characters' : 500, 'words' : 230}'''
    temptuple = file_info(fileName)
    return {'lines' : temptuple[0], 'characters' : temptuple[1], 'words' : temptuple[2]}

# A.5
def longest_line(fileName):
    '''Takes a fileName as an argument and returns the longest line itself and
    the length of that line in a tuple'''
    txtfile = open(fileName, 'r')
    longestLen = 0;
    longestLine = ''
    for line in txtfile:
        if(len(line) > longestLen):
            longestLen = len(line)
            longestLine = line
    txtfile.close()
    return (longestLen, longestLine)

# A.6
def sort_words(string):
    '''Takes a string as an argument, puts each word in a list, and sorts that list
    in alphabetical order. The sorted list is returned'''
    lst = string.split()
    lst.sort()
    return lst

# A.7
# 2**1 + 2**3 + 2**4 + 2**6 + 2**7 = 218
# The largest eight digit binary number is 255 in decimal

# A.8
def binaryToDecimal(lst):
    '''Takes a list that represents a binary number as an argument and
    returns a decimal integer'''
    integer = 0
    index = 0
    for i in range(len(lst) - 1, -1, -1):
        integer+= lst[i] * 2 ** index
        index += 1
    return integer

# B.1
# No spaces between operators. No spaces after commas.
# Bad function name. excessive abbreviation.
# Lack of docstring or comment

def sumOfCubes(a, b, c):
    '''This function receives three numbers as arguments and returns
    the sum of the cubes of each of the numbers'''
    return a ** 3 + b ** 3 + c ** 3

# B.2
# No space after open-comment sign.
# excessive argument length for all four args. ex: argumenta should just be a.
# excessive line length
# comment misspelled
# Instead of comment, put docstring.

def sumOfCubes(a, b, c):
    '''This function receives three numbers as arguments and returns
    the sum of the cubes of each of the numbers'''
    return a ** 3 + b ** 3 + c ** 3

# B.3
# Lack of docstring or comment explaining function
# Instead of x * x * x, use x**3. Simpler and more understandable.
# No whitespace between functions. put in 1 line.
# Too much indentation on sum_of_squares. Not consistent

def sum_of_squares(x, y):
    '''Returns sum of squares of two numbers'''
    return x ** 2 + y ** 2

def sum_of_three_cubes(x, y, z):
    '''Returns sum of cubes of three numbers'''
    return x ** 3 + y ** 3 + z ** 3
