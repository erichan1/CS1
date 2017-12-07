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
        self.board = [[0]*9 for i in range(9)]
        self.moves = []


    def load(self, filename):
        '''Using the file at filename,
        loads board into class board representation'''
        f = open(filename, 'r')
        for i in range(9):
            line = f.readline().rstrip()
            if len(line) == 0:
                raise IOError('IOError: Incorrect number of lines')
            elif len(line) != 9:
                raise IOError('IOError: Incorrect line length')
            for j in range(9):
                val = int(line[j])
                if val < 0 or val > 9:
                    raise IOError('IOError: Value not between 0 and 9')
                self.board[i][j] = val
        f.close()


    def save(self, filename):
        '''Writes current board representation to filename'''
        f = open(filename, 'w')
        for i in range(9):
            line = ''
            for j in range(9):
                line += str(self.board[i][j])
            f.write(line)
            f.write('\n')
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
        colLst = []
        for rw in self.board:
            colLst.append(rw[col])

        if(type(row) != int or type(col) != int or
        row < 0 or row > 9 or col < 0 or col > 9):
            raise SudokuMoveError('SudokuMoveError: Invalid coordinates')
        if(self.board[row][col] != 0):
            raise SudokuMoveError('SudokuMoveError: Invalid move. Value already exists in space')
        elif(val in self.board[row]):
            raise SudokuMoveError('SudokuMoveError: Invalid move. Same value in row')
        elif(val in colLst):
            raise SudokuMoveError('SudokuMoveError: Invalid move. Same value in column')
        elif(self.boxErrorHandle(row, col, val)):
            raise SudokuMoveError('SudokuMoveError: Invalid move. Same value in box')


        self.board[row][col] = val
        self.moves.append((row, col, val))

    def boxErrorHandle(self, row, col, val):
        if(row <= 2):
            if(col <= 2):
                box = (0, 0)
            elif(col <= 5):
                box = (0, 1)
            else:
                box = (0, 2)
        elif(row <= 5):
            if(col <= 2):
                box = (1, 0)
            elif(col <= 5):
                box = (1, 1)
            else:
                box = (1, 2)
        else:
            if(col <= 2):
                box = (2, 0)
            elif(col <= 5):
                box = (2, 1)
            else:
                box = (2, 2)
        for i in range(box[0], box[0] + 3):
            for j in range(box[1], box[1] + 3):
                if val == self.board[i][j]:
                    return False
        return True


    def undo(self):
        move = self.moves.pop()
        self.board[move[0]][move[1]] = 0

    def solve(self):
        try:
            while True:
                move = input('sudoku> ')
                moveLst = list(map(int, move))
                if len(move) == 3 and moveLst[0] > 0 and moveLst[0] < 10 and \
                moveLst[1] > 0 and moveLst[1] < 10 \
                and moveLst[2] > 0 and moveLst[2] < 10:
                    self.move(int(move[0]) - 1, int(move[1]) - 1, int(move[2]))
                    self.show()
                elif move == 'q':
                    break
                elif move == 'u':
                    self.undo()
                    self.show()
                elif move[0:2] == 's ':
                    self.save(move[2:])
                else:
                    raise SudokuCommandError(move)
        except SudokuCommandError as e:
            print('SudokuCommandError: Incorrect argument {}. Can only be q, \
            u, or three integers between 1 and 9').format(e)
        except SudokuMoveError as e:
            print(e)


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
