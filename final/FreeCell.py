#
# CS 1 Final exam, 2017
#

'''
This module has classes that implement a FreeCell game.
'''

import random
from Card import *

class IllegalMove(Exception):
    '''
    Exception class representing illegal moves in a FreeCell game.
    '''
    pass

class FreeCell:
    '''
    A FreeCell game is represented by the following data structures:
      -- the foundation: a dictionary mapping suits to ranks
         e.g. { 'S' : 'A', 'D': 2 }  # other two suits (H, C) empty
      -- the freecells: a list four cards (or None if no card)
      -- the "cascades": a list of eight lists of cards
    '''

    def __init__(self):
        self.foundation = {}   # suit -> number map
        self.freecell   = [None] * 4
        self.cascade    = [None] * 8

        # Deal cards from a full deck to the cascades.
        i = 0   # current cascade #
        for card in Deck():
            if self.cascade[i] == None:
                self.cascade[i] = []
            self.cascade[i].append(card)
            i = (i + 1) % 8

    def game_is_won(self):
        '''
        Return True if the game is won.
        '''

        for key in self.foundation:
            if self.foundation[key] != 'K':
                return False
        for cell in self.freecell:
            if cell != None:
                return False
        for cascade in self.cascade:
            if len(cascade) != 0:
                return False
        return True


    #
    # Movement-related functions.
    #

    def move_cascade_to_freecell(self, n):
        '''
        Move the bottom card of cascade 'n' to the freecells.
        Raise an IllegalMove exception if the move can't be made.
        '''

        if type(n) != int or n > 7 or n < 0:
            raise IllegalMove('IllegalMove: Cascade number must be between 0 and 7')
        elif len(self.cascade[n]) == 0:
            raise IllegalMove('IllegalMove: \
            Cannot move a card from an empty cascade')

        illegal = True
        for i in range(4):
            if self.freecell[i] == None:
                illegal = False
                self.freecell[i] = self.cascade[n].pop()
                break

        if(illegal):
            raise IllegalMove('IllegalMove: Cannot move card into full freecells')



    def move_freecell_to_cascade(self, m, n):
        '''
        Move freecell card 'm' to cascade 'n'.
        Raise an IllegalMove exception if the move can't be made.
        '''
        if type(n) != int or n > 7 or n < 0:
            raise IllegalMove('IllegalMove: Bad cascade number')

        if type(m) != int or m > 3 or m < 0:
            raise IllegalMove('IllegalMove: Bad freecell number')

        if self.freecell[m] == None:
            raise IllegalMove('IllegalMove: No card at specified freecell')

        if len(self.cascade[n]) == 0 or self.freecell[m].goes_below(self.cascade[n][-1]):
            self.cascade[n].append(self.freecell[m])
            self.freecell[m] = None
        else:
            raise IllegalMove('IllegalMove: Cannot place card on that cascade')

    def move_cascade_to_cascade(self, m, n):
        '''
        Move a single card from one cascade to another.
        Raise an IllegalMove exception if the move can't be made.
        '''

        if type(n) != int or type(m) != int or n > 7 or n < 0 or m > 7 or m < 0:
            raise IllegalMove('IllegalMove: Bad cascade number')
        elif len(self.cascade[m]) == 0:
            raise IllegalMove('IllegalMove: No card in specified cascade')
        elif len(self.cascade[n]) == 0 or self.cascade[m][-1].goes_below(self.cascade[n][-1]):
            self.cascade[n].append(self.cascade[m].pop())
        else:
            raise IllegalMove('IllegalMove: Cannot place card on that cascade')

    def move_cascade_to_foundation(self, n):
        '''
        Move the bottom card of cascade 'n' to the foundation.
        If there is no card, or if the bottom card can't go to the foundation,
        raise an IllegalMove exception.
        '''

        if type(n) != int or n > 7 or n < 0:
            raise IllegalMove('IllegalMove: Bad cascade number')
        elif len(self.cascade[n]) == 0:
            raise IllegalMove('IllegalMove: No card in specified cascade')
        elif self.cascade[n][-1].rank == 'A':
            self.foundation[self.cascade[n][-1].suit] = 'A'
            self.cascade[n].pop()
        elif self.cascade[n][-1].suit not in self.foundation:
            raise IllegalMove('IllegalMove: This card cannot be placed in the foundation')
        elif self.cascade[n][-1].goes_above(Card(self.foundation[self.freecell[n].suit], self.freecell[n].suit)):
            self.foundation[self.cascade[n][-1].suit] = self.cascade[n][-1].rank
            self.cascade[n].pop()
        else:
            raise IllegalMove('IllegalMove: This card cannot be placed in the foundation')

    def move_freecell_to_foundation(self, n):
        '''
        Move the card at index 'n' of the freecells to the foundation.
        If there is no card there, or if the card can't go to the foundation,
        raise an IllegalMove exception.
        '''
        if type(n) != int or n > 3 or n < 0:
            raise IllegalMove('IllegalMove: Freecell number \
            must be between 0 and 3')
        elif self.freecell[n] == None:
            raise IllegalMove('IllegalMove: No card in specified freecell')
        elif self.freecell[n].rank == 'A':
            self.foundation[self.freecell[n].suit] = 'A'
            self.freecell[n] = None
        elif self.freecell[n].suit not in self.foundation:
            raise IllegalMove('IllegalMove: Card cannot be placed in the foundation')
        elif self.freecell[n].goes_above(Card(self.foundation[self.freecell[n].suit], self.freecell[n].suit)):
            self.foundation[self.freecell[n].suit] = self.freecell[n].rank
            self.freecell[n] = None
        else:
            raise IllegalMove('IllegalMove: This card cannot be placed in the foundation')
