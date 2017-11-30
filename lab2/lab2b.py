# D.1
import random

def make_random_code():
    '''Returns a random four letter string only composed of the letters
    RGBYOW. Takes no arguments.'''
    str = ''
    for i in range(4):
        str += random.choice(['R','G','B','Y','O','W'])
    return str

# D.2
def count_exact_matches(str1,str2):
    '''Takes two strings as arguments and
    returns how many matches there are for both letter and location'''
    matchCount=0
    for i in range(4):
        if str1[i] == str2[i]:
            matchCount+=1
    return matchCount

# D.3
def count_letter_matches(str1,str2):
    '''Takes two strings as arguments and
    returns how many total letter matches there are between them.'''
    matchCount=0
    list1= list(str1)
    list2=list(str2)
    while(len(list1)>0):
        if list1[0] in list2:
            matchCount += 1
            list2.remove(list1[0])
        del list1[0]
    return matchCount

# D.4
def compare_codes(str1,str2):
    '''Takes two arguments as strings and compares them.
    Returns a string that shows how many exact location matches there are and
    how many letter, but not location matches there are'''
    whiteNum = count_letter_matches(str1,str2) - count_exact_matches(str1,str2)
    blackNum = count_exact_matches(str1,str2)
    emptyNum = 4 - blackNum - whiteNum
    guessCode = 'b'*blackNum + 'w'*whiteNum + '-'*emptyNum
    return guessCode

# D.5
def run_game():
    '''Runs the game Mastermind. Takes no arguments'''
    print('New Game.')
    secretCode = make_random_code()
    moveCounter=0
    while(True):
        guess = input('Enter your guess: ')
        moveCounter+=1
        guessCode = compare_codes(secretCode,guess)
        print('Result: {}'.format(guessCode))
        if(guessCode == 'bbbb'):
            print('Congratulations! You cracked the code in {} moves'.format(moveCounter))
            break
