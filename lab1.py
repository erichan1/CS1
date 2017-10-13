
#1.1 6
#1.2 20
#1.3 4.5
#1.4 -4.5
#1.5 1
#1.6 -1
#1.7 -1.0
#1.8 -4.5
#1.9 19
#1.10 35

#2.1 100
#2.2 110
#2.3 130
#2.4 90
#2.5 40
#2.6 120
#2.7 24.0
#2.8 0.0

#3 First, the statement x-x is evaluated, which equals 0.
#Then x adds 0 to itself, which equals 3.

#4.1 3.4j
#4.2 (-16+0j)
#4.3 (0.44+0.08j)
#4.4 (-3+4j)
#4.5 (1+4j)
#4.6 Without parentheses, python multiplies the real numbers together and
#adds that to the product of the imaginary numbers.
#With parentheses, python multiplies all elements within each paranthesis.

#5.1 (-3.165778513216168+1.959601041421606j)
#5.2 (1.2652585805200263+1.856847768512215j)
#5.3 (-1-1.2246467991473532e-16j)
#5.4 if you use from, then if functions have the same name in cmath and math,
#the function in cmath will overwrite the function in the math class.
# On the other hand, if you use import, then you have to
#use the class name when calling a function which avoids this problem.

#6.1 'foobar'
#6.2 'foobar'
#6.3 'foobar'
#6.4
#File "<stdin>", line 1
#    a b
#      ^
#SyntaxError: invalid syntax


#7 'A\nB\nC'

##8
#-*80'


#9 'first line \nsecond line \nthird line'

#10.1 print('The rabbit is {}.'.format(3))
#10.2 print('The rabbit is {} years old.'.format(3))
#10.3 print('{} is average.'.format(12.5))
#10.4 print('{} * {}.'.format(12.5,3))
#10.5 print('{} * {} is 37.5.'.format(12.5,3))

#11
num = float(input('Enter a number: '))
print(num)

#12
def quadratic(a,b,c,x):
    return a*x*x+b*x+c

#13
def GC_content(str):
    '''GC_content takes a string with only chars A,C,T,and G.
    It returns the proportion of that string which is C and G.'''
    return (str.count('C') + str.count('G'))/len(str)
