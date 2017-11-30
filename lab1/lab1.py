
# C.1.1 6
# C.1.2 20.0
# C.1.3 4.5
# C.1.4 -4.5
# C.1.5 1
# C.1.6 -1
# C.1.7 1
# C.1.8 -4.5
# C.1.9 19
# C.1.10 35

# C.2.1 100
# C.2.2 110
# C.2.3 130
# C.2.4 90
# C.2.5 40
# C.2.6 120
# C.2.7 24.0
# C.2.8 0.0

# C 3 First, the statement x - x is evaluated, which equals 0.
# Then x adds 0 to itself, which equals 3.

# C.4.1 3.4j
# C.4.2 (-16+0j)
# C.4.3 (0.44+0.08j)
# C.4.4 (-3+4j)
# C.4.5 (1+4j)
# C.4.6 Without parentheses, python follows standard order of operations. First, multiply 2j and 1. Then add.
# With parentheses, python multiplies all elements within each paranthesis.

# C.5.1 (-3.165778513216168+1.959601041421606j)
# C.5.2 (1.2652585805200263+1.856847768512215j)
# C.5.3 (-1-1.2246467991473532e-16j)
# C.5.4 if you use from, then if functions have the same name in cmath and math,
# the function in cmath will overwrite the function in the math class.
# On the other hand, if you use import, then you have to
# use the class name when calling a function which avoids this problem.

# C.6.1 'foobar'
# C.6.2 'foobar'
# C.6.3 'foobar'
# C.6.4
# File "<stdin>", line 1
#     a b
#       ^
# SyntaxError: invalid syntax

# C.7 'A\nB\nC'

# C.8
# '-' * 80

# C.9 'first line\nsecond line\nthird line'

# C.10.1
x=3
y=12.5
print('The rabbit is {}.'.format(x))
# C.10.2
print('The rabbit is {} years old.'.format(x))
# C.10.3
print('{} is average.'.format(y))
# C.10.4
print('{} * {}'.format(y,x))
# C.10.5
print('{} * {} is '.format(y,x) + str(x * y) + '.')

# C.11
num = float(input('Enter a number: '))
print(num)

# C.12
def quadratic(a,b,c,x):
    return a * x * x + b * x + c

# C.13
def GC_content(str):
    '''GC_content takes a string with only chars A,C,T,and G.
    It returns the proportion of that string which is C and G.'''
    return (str.count('C') + str.count('G')) / len(str)
