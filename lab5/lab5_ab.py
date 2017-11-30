import math

class Point:
    '''Represents a point in three dimensional space'''


    def __init__(self, x, y, z):
        '''
        Constructor
        Arguments - x, y, and z coordinates. Numbers.
        Action - Sets properties x, y, and z to arguments
        '''

        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, point):
        '''
        Arguments - Another point.
        Action - Finds distance between the two points.
        '''

        return math.sqrt((self.x - point.x) ** 2 +
        (self.y - point.y) ** 2 + (self.z - point.z) ** 2)

class Triangle:
    '''Represents a triangle in three dimensional space'''

    def __init__(self, point1, point2, point3):
        '''
        Constructor
        Arguments - Three points
        Action - Sets the properties of the triangle, which are its three
        points to the arguments
        '''

        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def area(self):
        '''
        Arguments - none
        Action - Finds the area of the triangle using Heron's formula
        '''

        length1 = self.point1.distanceTo(self.point2)
        length2 = self.point2.distanceTo(self.point3)
        length3 = self.point3.distanceTo(self.point1)
        sperim = (length1 + length2 + length3) / 2
        area = math.sqrt(sperim * (sperim - length1) *
        (sperim - length2) * (sperim - length3))
        return area

class Averager:
    '''Class that holds a list of numbers, their sum, and the number of
    items in the list as its properties. Has a number of methods to
    operate on these numbers.'''


    def __init__(self):
        '''
        Constructor
        Arguments - none
        Action - Sets properties nums to empty list, total to zero, and
        n (number of items) to zero.
        '''

        self.nums = []
        self.total = 0
        self.n = 0

    def getNums(self):
        '''
        Getter Function
        Arguments - none
        Action - returns the class list of numbers
        '''

        return self.nums[::]

    def append(self, num):
        '''
        Arguments - a number
        Action - appends the number to the end of the class list
        '''

        self.nums.append(num)
        self.n += 1
        self.total += num

    def extend(self, lst):
        '''
        Arguments - a list of numbers
        Action - appends the elements within the list of numbers to the end of
        the class list.
        '''

        for num in lst:
            self.append(num)

    def average(self):
        '''
        Arguments - none
        Action - averages the numbers in the class list of numbers
        '''

        if self.n == 0:
            return 0
        else:
            return self.total / self.n

    def limits(self):
        '''
        Arguments - none
        Action - returns the highest and lowest number in class list of
        numbers
        '''

        if self.n == 0:
            return (0, 0)
        else:
            maxNum = max(self.nums)
            minNum = min(self.nums)
            return (minNum, maxNum)

# B.1
# Don't need if statement or else statement
def is_positive(x):
    '''Test if x is positive.'''

    return x > 0

# B.2
# Unnecessary variables with found and location. Causes lots of needless
# assignment. Also superfluous else statement at end.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''

    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

# B.3
# Adding elif statements instead of if statements means that if an if statement
# is fulfilled, the if statements below it won't need to be checked.
# Also don't need x > 0 statement in second elif and can use else instead of an
# if statement in fourth comparator. 
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''

    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x < 10:
        category = 'small'
    else:
        category = 'large'
    return category

# B.4
# Superfluous if and elif statements.
# Just use one for loop to take care of any size list.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''

    total = 0
    for item in lst:
        total += item
