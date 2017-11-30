'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = 0


    def load(self, filename):
        f = open(filename, 'r')
        for i in range(9):
            line = f.readline()
            for j in range(9):
                self.board[i][j] = line[j]
        f.close()


    def save(self, filename):
        f = open(filename, 'w')
        for i in range(9):
            f.write(self.board[i])
        f.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print()
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        # TODO

    def undo(self):
        # TODO

    def solve(self):
        # TODO

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError as e:
            print(e)

    s.show()
    s.solve()
