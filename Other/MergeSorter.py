'''
This module allows you to merge sort a list of items that you input
'''

import math, random, time, sys
from tkinter import *

class MergeSortException(Exception):
    pass

def load(filename):
    '''Using the file at filename, loads list into program returns list'''

    lst = []
    f = open(filename, 'r')
    for line in f:
        lst.append(line)
    f.close()
    return lst

def save(lst, filename):
    '''Writes current board representation to filename'''
    f = open(filename, 'w')
    for i in range(len(lst)):
        f.write(lst[i])
        f.write('\n')
    f.close()

def mergeSort(lst, start, end):
    if(start < end):
        mid = (start + end) / 2
        mergeSort(lst, start, mid)
        mergeSort(lst, mid+1, end)

    merge(lst, start, mid, end)

if __name__ == '__main__':
    try:
        filename = input('Enter the filename for the list to be mergesorted: ')
        scrambledList = load(filename)
        while True:
            choice = input('Enter your choice. (1) or (2): ')
            if(choice == '1'):
                pass
            elif(choice == '2'):

            else:
                raise MergeSortException('Wrong Choice! (1) or (2) only')
    except IOError as e:
        print(e)
    except MergeSortException as e:
        print(e)
