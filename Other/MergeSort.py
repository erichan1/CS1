import math, random, time, sys

class MergeSortException(Exception):
    pass

class List:
    def __init__(self, initialList):
        self.list = initialList
        self.length = len(self.list)

    def mergeSort(self, start, end):
        if start >= end:
            return

        mid = int((start + end) / 2)
        self.mergeSort(start, mid)
        self.mergeSort(mid + 1, end)
        self.merge(start, end)

    def merge(self, start, end):
        temp = []
        mid = int((start + end) / 2)
        leftIndex = start
        rightIndex = mid + 1
        while True:
            if(getChoice(self.list[leftIndex], self.list[rightIndex])):
                temp.append(self.list[leftIndex])
                leftIndex += 1
            else:
                temp.append(self.list[rightIndex])
                rightIndex += 1
            if leftIndex > mid:
                for i in range(rightIndex, end + 1):
                    temp.append(self.list[i])
                break
            elif rightIndex > end:
                for i in range(leftIndex, mid + 1):
                    temp.append(self.list[i])
                break
        for i in range(start, end + 1):
            self.list[i] = temp[i-start]

def load(filename):
    '''Using the file at filename, loads list into program returns list'''

    lst = []
    f = open(filename, 'r')
    for line in f:
        lst.append(line.rstrip())
    f.close()
    return lst

def save(lst, filename):
    '''Writes current board representation to filename'''
    f = open(filename, 'w')
    for i in range(len(lst)):
        f.write(lst[i])
        f.write('\n')
    f.close()


def getChoice(e1, e2):
    print('Which one is better: (1){} or (2){}'.format(e1, e2))
    choice = input('Enter your choice. (1), (2), or (3): ')
    print()
    if choice == '1':
        return True
    elif choice == '2':
        return False
    elif choice == '3':
        return random.choice([True, False])
    #somehow gets the choice between the two
    # true if element 1 is greater
    # false if not
    # When kinda equal, then pick 3. picks randomly.


if __name__ == '__main__':
    try:
        filename = input('Enter the filename for the list to be mergesorted: ')
        scrambledList = List(load(filename))
        scrambledList.mergeSort(0, scrambledList.length - 1)
        sortedList = scrambledList
        print(sortedList.list)
        #saveFile = input('Enter the filename to save the mergesorted list: ')

    except IOError as e:
        print(e)
