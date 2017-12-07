
# A.1.1
def union(s1, s2):
    unionSet = set()
    for element in s1:
        unionSet.add(element)
    for element in s2:
        unionSet.add(element)
    return unionSet

# A.1.2
def intersection(s1, s2):
    intersectSet = set()
    for element in s1:
        if element not in s2:
            intersectSet.add(element)
    for element in s2:
        if element not in s1:
            intersectSet.add(element)
    return intersectSet

# A.2
def mysum(*nums):
    try:
        sm = 0
        for num in nums:
            if num < 0:
                raise ValueError('ValueError: Argument not greater than zero.')
            sm += num
        return sm
    except TypeError:
        print('TypeError: Argument not an integer.')

# A.3
def myNewsum(*nums):
    try:
        sm = 0
        if type(nums[0]) == list:
            for num in lst in nums:
                if num < 0:
                    raise ValueError('ValueError: Argument not greater than zero.')
                sm += num
            return sm
        elif type(nums[0]) == int:
            for num in nums:
                if num < 0:
                    raise ValueError('ValueError: Argument not greater than zero.')
                sm += num
            return sm
    except TypeError:
        print('TypeError: Argument not an integer.')

# A.4
def myOpReduce(intLst, **op):
        if len(op) != 1:
            raise valueError('ValueError: Incorrect number of arguments')
        if type(op) != str:
            raise TypeError('typeError: Arg is not string')
        elif op != '+' or op != '*' or op != 'max':
            raise ValueError('ValueError: Arg is not one of +, *, or max)

        elif op == '+':
            sm = 0
            for num in intLst:
                sm += num
            return sm
        elif op == '*':
            prod = 0
            for num in intLst:
                prod *= num
            return prod
        elif op == 'max':
            mx = intLst[0]
            for num in intLst:
                if num > mx:
                    mx = num
            return mx

# B.1
# Do not need to quit. Simply write an error message if wrong key is used.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        print('KeyError: Key not found')

# B.2
