'''Module for part a of lab2 of CS1. Various functions depending on the problems.'''

# B.1
def complement(str):
    '''Takes in string with only letters A,C,T, and G.
    returns DNA complement in the form of a string.'''
    str2 = ''
    for i in range(len(str)):
        if str[i] == 'A':
            str2 += 'T'
        elif str[i] == 'C':
            str2 += 'G'
        elif str[i] == 'T':
            str2 += 'A'
        elif str[i] == 'G':
            str2 += 'C'
    return str2

# B.2
def list_complement(lst):
    '''Takes in list with only letters A,C,T, and G.
    Alters list to match complement of DNA.'''
    for i in range(len(lst)):
        if lst[i] == 'A':
            lst[i] = 'T'
        elif lst[i] == 'C':
            lst[i] = 'G'
        elif lst[i] == 'T':
            lst[i] = 'A'
        elif lst[i] == 'G':
            lst[i] = 'C'

# B.3
def product(lst):
    '''Takes in a list of numbers and returns the product of
    all numbers in the list. If list is empty, will return 1.'''
    if len(lst)<1:
        return 1
    else:
        return product(lst[1:len(lst)]) * lst[0]

# B.4
def factorial(num):
    '''Takes a non-negative integer and returns the factorial of that integer'''
    numList = []
    for i in range(1,num + 1):
        numList.append(i)
    return product(numList)

# B.5
import random
def dice(m,n):
    '''simulates the rolling of an n number of m sided die.
    Takes m and n as arguments and returns total value of rolled die'''
    totalVal = 0
    for i in range(n):
        totalVal += random.choice(range(1,m + 1))
    return totalVal

# B.6
def remove_all(lst,num):
    '''removes all instances of num in lst.
    Arguments are lst, a list of numbers, and num, the number to be removed.'''
    while(lst.count(num)>0):
        lst.remove(num)

# B.7
def remove_all2(lst,num):
    '''removes all instances of num in lst.
    Arguments are lst, a list of numbers, and num, the number to be removed.'''
    for i in range(lst.count(num)):
        lst.remove(num)

def remove_all3(lst,num):
    '''removes all instances of num in lst.
    Arguments are lst, a list of numbers, and num, the number to be removed.'''
    while(num in lst):
        lst.remove(num)

# B.8
def any_in(lst1,lst2):
    '''Takes two lists as arguments.
    Returns a boolean that checks if any elements in list 1 exist in list 2.'''
    i = 0
    while(i<len(lst1)):
        if(lst1[i] in lst2):
            return True
        i += 1
    return False

# C.1.a
# a=0 is assignment. a==0 will check if a has become a zero.

# C.1.b
# The argument 's' is a one letter string, not the string variable s.
# Because the variable s hasn't been initialized or defined, function will fail.
# Turn the 's' in the argument into just s.

# C.1.c
# 's' + '-Caltech' always equals 's-Caltech'. It doesn't actually use the
# string argument s. Turn 's' into just s.

# C.1.d
# The plus operator doesn't work between lists and strings.
# lst.append('bam') would be a better choice.

# C.1.e
# lst.reverse() doesn't return anything, so lst2 has a null value.
# Docstring for reverse() says it reverses in place.
# lst.append() also doesn't return anything, so nothing will be returned.
# fix would be:
# lst.reverse()
# lst.append(0)
# return lst

# C.1.f
# If you append a list to the end of another list, you get a list
# within another list, like so: ['a','b',['c','d','e']].
# To fix, I would iterate through the string with a for loop and
# append each char in the string to the list.
# Also, in the arguments, a 'list' variable is defined. This overwrites the
# name list. list(str) then fails bc list is now a variable name.

# C.2
# When c is assigned, the values of a and b are 10 and 20. Thus, c=30.
# Changing the value of a after c is assigned does not affect the value of c.

# C.3
# The first line of code would work because add_and_double_1 returns a value.
# That value can be multiplied by 2 and assigned to result.
# On the other hand, add_and_double_2 prints a value and doesn't return it.
# Thus, the function call becomes n = 2 * null, which will cause an error.

# C.4
# Second function call has too many arguments. It's supposed to get x and y through the input function.
# First function call has correct number of arguments.

# C.5
# Strings are immutable once a value is assigned to them. You cannot reassign
# one char in the string.

# C.6
# item is not called by reference. Thus, the item in
# item *= 2 is entirely seperate from the value in the list.
