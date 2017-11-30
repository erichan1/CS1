# Name: Eric Han
# Login: eshan

# ----------------------------------------------------------------------
# Part 1: Pitfalls
# ----------------------------------------------------------------------

# 1.1
# Docstring should be three apostrophes, not two.
#
# Should be == instead of = in the first if statement.
#
# Because the argument is defined as the string 'lst', then the statement
# if lst will return an error because the variable lst hasn't been defined.
# Also cannot call len(lst) because lst variable isn't defined.
#
# No colon after while statement.
#
# Inconsistent indenting on the else statement.
#

# 1.2
# lst.reverse() doesn't return anything, so cannot use == to compare.
#
# appending a list doesn't append the elements. it appends the entire list.
# Thus, palindromes.append(ps) gets a list with the wrong format.
#
# Cannot use += operator on list to add string. must use append.
#
# isPalindrome should take an argument for each word, but instead uses input.
#
# isPalindrome also prints the result of whether or not a word is a palindrome
# instead of returning it.

# 1.3
# No spacing between some operators
# Excessive spacing between operators (*     i[1][0])
# Bad function Name
# Bad variable names
# Excessive line length
# Should use a for loop to iterate through
# Incomprehensible Docstring
# Indentation should be 4 spaces
# Should be a line of whitespace after docstring. 


# ----------------------------------------------------------------------
# Part 2: Simple functions.
# ----------------------------------------------------------------------

import random, sys

#
# Problem 2.1
#

def draw_box(n):
    '''

    Return a string which, if printed, would draw a box on the terminal.  The
    exterior of the box should be made from '+' '-' and '|' characters.  The
    interior will have dimensions nxn and the characters will be one of the
    characters 'x', 'y', 'o', or '.', which will occur in order (even between
    lines).  There is a blank line before and after the box contents in the
    returned string.

    Examples:

    >>> print(draw_box(1))

    +-+
    |x|
    +-+

    >>> print(draw_box(2))

    +--+
    |xy|
    |o.|
    +--+

    >>> print(draw_box(3))

    +---+
    |xyo|
    |.xy|
    |o.x|
    +---+

    >>> print(draw_box(4))

    +----+
    |xyo.|
    |xyo.|
    |xyo.|
    |xyo.|
    +----+

    >>> print(draw_box(5))

    +-----+
    |xyo.x|
    |yo.xy|
    |o.xyo|
    |.xyo.|
    |xyo.x|
    +-----+

    >>> print(draw_box(10))

    +----------+
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    +----------+

    Arguments:
      n -- a positive integer representing the side length of the box.

    Return value: none.
    '''

    assert n > 0

    boxString = '\n'
    k = 0
    for i in range(n):
        for j in range(n+1):
            if(j == n):
                boxString += '\n'
            elif(i == 0 and j == 0 or i == 0 and j == n - 1 or i == n - 1 and
            j == n - 1 or i == n - 1 and j == 0):
                boxString += '+'
            elif(i == 0 or i == n - 1):
                boxString += '-'
            elif(j == 0 or j == n - 1):
                boxString += '|'
            elif(k == 0):
                boxString += 'x'
                k += 1
            elif(k == 1):
                boxString += 'y'
                k += 1
            elif(k == 2):
                boxString += 'o'
                k += 1
            elif(k == 3):
                boxString += '.'
                k += 1
            if(k == 4):
                k = 0
    return boxString



def test_draw_box():
    print(draw_box(1))
    print(draw_box(2))
    print(draw_box(3))
    print(draw_box(4))
    print(draw_box(5))
    print(draw_box(10))

#
# Problem 2.2
#

def roll():
    '''
    Roll two six-sided dice and return their result.
    Arguments: none
    Return value: the result (an integer between 2 and 12).
    '''

    return random.randint(1, 6) + random.randint(1, 6)

def craps(verbose):
    '''
    Play one round of craps.

    Arguments:
      verbose: print out the progress of the game while playing

    Return value:
      True if the player wins, else False
    '''

    verboseStr = ''
    winBool = False
    init = roll()
    if(init == 7 or init == 11):
        verboseStr = 'You rolled {}.  You win!'.format(init)
        winBool = True
    elif(init == 2 or init == 3 or init == 12):
        verboseStr = 'You rolled {}.  You lose!'.format(init)
        winBool = False
    else:
        verboseStr = 'Your point is: {}\n'.format(init)
        pointRoll = roll()
        while(pointRoll != 7 and pointRoll != init):
            verboseStr += 'You rolled {}\n'.format(pointRoll)
            pointRoll = roll()
        if(pointRoll == 7):
            verboseStr += 'You missed your point! You lose!'
            winBool = False
        if(pointRoll == init):
            verboseStr += 'You hit your point! You win!'
            winBool = True

    if(verbose):
        print(verboseStr)
        return winBool
    else:
        return winBool



def craps_edge(n):
    '''
    Estimate and return the house edge for craps.
    See https://wizardofodds.com/games/craps/appendix/1/ for an
    analytical derivation.  The result is 1 41/99 % or 1.4141... %.

    Argument: n: the number of rounds played (>= 0)
    Return value: the house edge in percent
    '''

    assert n >= 0
    wins = 0
    losses = 0
    for i in range(n):
        if(craps(False)):
            wins += 1
        else:
            losses += 1
    total = wins + losses
    pwin = wins / total
    plose = losses / total
    return -1 * (pwin - plose) * 100

#
# Problem 2.3
#

def remove_indices(lst, indices):
    '''
    Return a copy of a list with the elements at the given indices removed.
    Valid negative indices (between -1 and -(length of list)+1) can be used.
    Out-of-bound indices are ignored.

    Argument:
      lst -- the input list
      indices -- a list of integers representing locations in the list to remove

    Return value:
      The new list.  The old list is not altered in any way.
    '''

    # Normalizes indices
    for i in range(len(indices)):
        if(indices[i] < 0):
            indices[i] += len(lst)

    # If index out of bounds, returns original list
    for i in range(len(indices)):
        if(indices[i] < 0 or indices[i] > len(lst) - 1):
            lst2 = lst
            return lst2

    # Removes indices and returns changed list
    lst2 = [None] * (len(lst) - len(indices))
    j = 0
    for i in range(len(lst)):
        if(i in indices):
            j += 1
        else:
            lst2[i - j] = lst[i]
    return lst2

def get_bet_info(bets, cwins):
    '''
    Select the next bet information for a gambling system.

    Arguments:
      bets  -- the list of bets set by the gambling system
      cwins -- the consecutive wins (0, 1) previously

    Result:
      a two tuple containing:
      -- the bet amount;
      -- the indices of the 'bets' array where the bet amount was taken from
    '''
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]

    if(cwins == 0):
        return (bets[0], [0])
    if(cwins == 1):
        if(len(bets) > 1):
            return (bets[0] + bets[len(bets)-1], [0, len(bets)-1])
        else:
            return (bets[0], [0])
    if(cwins == 2):
        if(len(bets) > 2):
            return (bets[0] + bets[1] + bets[len(bets)-1], [0, 1, len(bets)-1])
        elif(len(bets) > 1):
            return (bets[0] + bets[len(bets)-1], [0, len(bets)-1])
        else:
            return (bets[0], [0])

def make_one_bet(bankroll, bets, cwins, next_is_win):
    '''
    Play a gambling system for a single bet.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      cwins       -- the consecutive wins previously
      next_is_win -- the next result of the game being played

    Result:
       A tuple consisting of:
       1) the updated bankroll
       2) the updated bets list
       3) the updated consecutive wins (max 2)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]
    assert next_is_win in [True, False]

    betInfo = get_bet_info(bets, cwins)

    if(bankroll < betInfo[0]):
        return (bankroll, [], 0)

    if(next_is_win):
        if(cwins < 2):
            return (bankroll + betInfo[0], remove_indices(bets, betInfo[1]), cwins + 1)
        else:
            return (bankroll + betInfo[0], remove_indices(bets, betInfo[1]), cwins)
    else:
        bets.append(betInfo[0])
        if(cwins > 0):
            return (bankroll - betInfo[0], bets, 0)
        else:
            return (bankroll - betInfo[0], bets, cwins)

#
# Test code supplied to students.
#

def random_bool():
    '''Return a random True/False value.'''
    return random.choice([True, False])

def one_round(bankroll, bets, verbose):
    '''
    Play a gambling system for a single round.
    Halt if either the desired amount of money is made, or if
    the player's bankroll hits zero.  Return the final bankroll.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      verbose     -- if True, print out debugging information

    Return value: total profit (negative if there was a loss)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0

    orig_bankroll = bankroll
    cwins = 0

    if verbose:
        print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
            cwins))

    while True:
        # Test the gambling system on craps.
        #result = craps(False)
        # Alternatively, test it on a random uniformly-distributed boolean
        # result (like flipping heads or tails).
        result = random_bool()
        if verbose:
            print('result: {}'.format(result))
        (bankroll, bets, cwins) = make_one_bet(bankroll, bets, cwins, result)
        if verbose:
            print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
                cwins))
        if bets == []:
            break
    profit = bankroll - orig_bankroll
    return profit

def run_gambling_system(verbose):
    '''
    Run multiple iterations of the gambling system,
    carrying on the bankroll from one iteration to the next.
    '''

    niters = 1000
    bankroll = 700
    orig_bankroll = bankroll
    for _ in range(niters):
        bets = [10, 10, 15]
        profit = one_round(bankroll, bets, verbose)
        if verbose:
            print('PROFIT: {}\n'.format(profit))
        bankroll += profit
        if verbose:
            print('BANKROLL: {}'.format(bankroll))
        if bankroll <= 0:
            break
    total_profit = bankroll - orig_bankroll
    if verbose:
        print('TOTAL PROFIT: {}'.format(total_profit))
    return total_profit

def run_gambling_system_multiple_times(n, verbose):
    '''
    Run multiple independent iterations of the gambling system,
    estimating and printing the average profit.
    '''

    total_profit = 0
    for _ in range(n):
        net_profit = run_gambling_system(verbose)
        if verbose:
            print(net_profit)
        total_profit += net_profit
    avg_profit = total_profit / n
    print('AVERAGE PROFIT: {}'.format(avg_profit))

# Example of use:
# run_gambling_system_multiple_times(10000, False)

# ----------------------------------------------------------------------
# Miniproject: 2048 game.
# ----------------------------------------------------------------------

#
# Problem 3.1
#

def make_board():
    '''
    Create a game board in its initial state.
    The board is a dictionary mapping (row, column) coordinates
    (zero-indexed) to integers which are all powers of two (2, 4, ...).
    Exactly two locations are filled.
    Each contains either 2 or 4, with an 80% probability of it being 2.

    Arguments: none
    Return value: the board
    '''
    board = {}
    rand1 = random.randint(1, 10)
    rand2 = random.randint(1, 10)
    x1 = random.randint(0, 3)
    y1 = random.randint(0, 3)
    x2 = random.randint(0,3)
    if(x2 == x1):
        choices = [0, 1, 2, 3]
        choices.remove(y1)
        y2 = random.choice(choices)
    else:
        y2 = random.randint(0,3)

    if(rand1 > 2):
        board[(x1, y1)] = 2
    else:
        board[(x1, y1)] = 4

    if(rand2 > 2):
        board[(x2, y2)] = 2
    else:
        board[(x2, y2)] = 4
    return board

#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''

    assert 0 <= row_n < 4

    keys = list(board.keys())
    rowList = []
    if((row_n, 0) in keys):
        rowList.append(board[(row_n, 0)])
    else:
        rowList.append(0)
    if((row_n, 1) in keys):
        rowList.append(board[(row_n, 1)])
    else:
        rowList.append(0)
    if((row_n, 2) in keys):
        rowList.append(board[(row_n, 2)])
    else:
        rowList.append(0)
    if((row_n, 3) in keys):
        rowList.append(board[(row_n, 3)])
    else:
        rowList.append(0)
    return rowList

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4

    keys = list(board.keys())
    colList = []
    if((0, col_n) in keys):
        colList.append(board[(0, col_n)])
    else:
        colList.append(0)
    if((1, col_n) in keys):
        colList.append(board[(1, col_n)])
    else:
        colList.append(0)
    if((2, col_n) in keys):
        colList.append(board[(2, col_n)])
    else:
        colList.append(0)
    if((3, col_n) in keys):
        colList.append(board[(3, col_n)])
    else:
        colList.append(0)
    return colList

def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= row_n < 4
    assert len(row) == 4

    if(row[0] == 0 and (row_n, 0) in board):
        del board[(row_n, 0)]
    elif(row[0] != 0):
        board[(row_n, 0)] = row[0]

    if(row[1] == 0 and (row_n, 1) in board):
        del board[(row_n, 1)]
    elif(row[1] != 0):
        board[(row_n, 1)] = row[1]

    if(row[2] == 0 and (row_n, 2) in board):
        del board[(row_n, 2)]
    elif(row[2] != 0):
        board[(row_n, 2)] = row[2]

    if(row[3] == 0 and (row_n, 3) in board):
        del board[(row_n, 3)]
    elif(row[3] != 0):
        board[(row_n, 3)] = row[3]

def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= col_n < 4
    assert len(col) == 4

    if(col[0] == 0 and (0, col_n) in board):
        del board[(0, col_n)]
    elif(col[0] != 0):
        board[(0, col_n)] = col[0]

    if(col[1] == 0 and (1, col_n) in board):
        del board[(1, col_n)]
    elif(col[1] != 0):
        board[(1, col_n)] = col[1]

    if(col[2] == 0 and (2, col_n) in board):
        del board[(2, col_n)]
    elif(col[2] != 0):
        board[(2, col_n)] = col[2]

    if(col[3] == 0 and (3, col_n) in board):
        del board[(3, col_n)]
    elif(col[3] != 0):
        board[(3, col_n)] = col[3]

#
# Problem 3.3
#

def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    2048 game.

    Argument:
      numbers -- a list of 4 numbers

    Return value:
      The list after moving the numbers to the left.  The original list
      is not altered.
    '''

    assert len(numbers) == 4

    shiftedList = move_left(numbers)
    for i in range(3):
        if shiftedList[i] != 0 and shiftedList[i] == shiftedList[i+1]:
            shiftedList[i] = shiftedList[i] + shiftedList[i+1]
            shiftedList[i+1] = 0
    finalList = move_left(shiftedList)
    return finalList

def move_left(lst):
    '''
    Helper function for make_move_on_list. Shifts numbers to their
    leftmost possible position in a list.

    Argument:
      lst -- a list of 4 numbers

    Return value:
      The list after moving the position of the numbers without combining them.
      The original list is not altered.
    '''

    lst2 = lst[:]
    isLeft = False
    shiftCounter = 1
    while(shiftCounter != 0):
        shiftCounter = 0
        for i in range(3, 0, -1):
            if lst2[i] != 0 and lst2[i-1] == 0:
                lst2[i - 1] = lst2[i]
                lst2[i] = 0
                shiftCounter += 1
    return lst2

#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']

    if(cmd == 'w'):
        put_column(board, make_move_on_list(get_column(board, 0)), 0)
        put_column(board, make_move_on_list(get_column(board, 1)), 1)
        put_column(board, make_move_on_list(get_column(board, 2)), 2)
        put_column(board, make_move_on_list(get_column(board, 3)), 3)
    if(cmd == 'a'):
        put_row(board, make_move_on_list(get_row(board, 0)), 0)
        put_row(board, make_move_on_list(get_row(board, 1)), 1)
        put_row(board, make_move_on_list(get_row(board, 2)), 2)
        put_row(board, make_move_on_list(get_row(board, 3)), 3)
    if(cmd == 's'):
        put_column(board, make_move_on_list(get_column(board, 0)[::-1])[::-1], 0)
        put_column(board, make_move_on_list(get_column(board, 1)[::-1])[::-1], 1)
        put_column(board, make_move_on_list(get_column(board, 2)[::-1])[::-1], 2)
        put_column(board, make_move_on_list(get_column(board, 3)[::-1])[::-1], 3)
    if(cmd == 'd'):
        put_row(board, make_move_on_list(get_row(board, 0)[::-1])[::-1], 0)
        put_row(board, make_move_on_list(get_row(board, 1)[::-1])[::-1], 1)
        put_row(board, make_move_on_list(get_row(board, 2)[::-1])[::-1], 2)
        put_row(board, make_move_on_list(get_row(board, 3)[::-1])[::-1], 3)

#
# Problem 3.5
#

def game_over(board):
    '''
    Return True if the game is over i.e. if no moves can be made on the board.
    The board is not altered.

    Argument: board -- the game board
    Return value: True if the game is over, else False
    '''

    if(not (0 in get_column(board, 0) or 0 in get_column(board, 1)
    or 0 in get_column(board, 2) or 0 in get_column(board, 3))):
        return False

    boardCopy = board.copy()
    if(make_move(board, 'w') != boardCopy):
        return False
    if(make_move(board, 'a') != boardCopy):
        return False
    if(make_move(board, 's') != boardCopy):
        return False
    if(make_move(board, 'd') != boardCopy):
        return False

    return True

#
# Problem 3.6
#

def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board has changed,
    then add a new number (2 or 4, 90% probability it's a 2) on a
    randomly-chosen empty square on the board.  This function assumes that a
    move can be made on the board.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    boardCopy = board.copy()

    make_move(board, cmd)

    if(board != boardCopy):
        madeMove = True
    else:
        madeMove = False

    randInt = random.randint(1,10)
    emptyPosList = []
    if(madeMove):
        for i in range(4):
            for j in range(4):
                if (i, j) not in board:
                    emptyPosList.append((i, j))
        if(randInt > 1):
            board[random.choice(emptyPosList)] = 2
        else:
            board[random.choice(emptyPosList)] = 4

### Supplied to students:

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        if game_over(b):
            print('Game over!')
            break

        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        display(b)


#
# Useful for testing:
#

def list_to_board(lst):
    '''
    Convert a length-16 list into a board.
    '''
    board = {}
    k = 0
    for i in range(4):
        for j in range(4):
            if lst[k] != 0:
                board[(i, j)] = lst[k]
            k += 1
    return board

def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        print(move)
        display(board)
        if game_over(board):
            break
