#
# CS 1 Final exam, 2017
#

'''
This module has functions and classes that augment the base FreeCell
object to produce a more full-featured FreeCell game.
'''

import random
from Card import *
from FreeCell import *

# Supplied to students:
def max_cards_to_move(nc, nf):
    '''
    Return the maximum number of cards that can be moved as a single sequence
    if the game has 'nc' empty cascades and 'nf' empty freecells.
    If the target cascade is empty then subtract 1 from 'nc'.

    Arguments:
      nc -- number of empty non-target cascades
      nf -- number of empty freecells

    Return value:
      the maximum number of cards that can be moved to the target
    '''

    assert type(nc) is int
    assert 0 <= nc <= 8
    assert type(nf) is int
    assert 0 <= nf <= 4

    return 1 + nf + sum(range(1, nc + 1))

def longest_movable_sequence(cards):
    '''
    Compute the length of the longest sequence of cards at the end of a
    list of cards that can be moved in a single move.  Cards in the sequence
    must be in strict descending order and alternate colors.

    Arguments:
      cards -- a list of cards

    Return value:
      the number of cards at the end of the list forming the longest
      sequence
    '''

    assert type(cards) is list
    for c in cards:
        assert isinstance(c, Card)

    if len(cards) == 0:
        return 0

    seqLen = 1
    cardsR = cards[::-1]
    for i in range(len(cardsR)-1):
        if cardsR[i].color != cardsR[i + 1].color and cardsR[i].goes_below(cardsR[i + 1]):
            seqLen += 1
        else:
            break

    return seqLen

def ok_to_automove(card, foundation):
    '''
    Return True if a card can be automoved to a foundation.

    Arguments:
      card       -- a Card object
      foundation -- a foundation dictionary (mapping suits to ranks)

    Return value:
      True if the card can be automoved, else False
    '''

    assert isinstance(card, Card)
    assert type(foundation) is dict

    if(card.rank == 'A'):
        return True
    else:
        if card.color == 'red':
            fClub = foundation['C']
            fSpade = foundation['S']
            fClubIndex = all_ranks.index(fClub.rank)
            fSpadeIndex = all_ranks.index(fSpade.rank)
            if fClubIndex > all_ranks.index(card) - 1 and fSpadeIndex > all_ranks.index(card) - 1:
                return True
            else:
                return False
        else:
            fDiamond = foundation['D']
            fHeart = foundation['H']
            fDiamondIndex = all_ranks.index(fDiamond.rank)
            fHeartIndex = all_ranks.index(fHeart.rank)
            if fHeartIndex > all_ranks.index(card) - 1 and fDiamondIndex > all_ranks.index(card) - 1:
                return True
            else:
                return False

class FreeCellFull(FreeCell):
    '''
    FreeCellFull is an enhanced version of FreeCell with extra useful
    features.
    '''

    def multi_move_cascade_to_cascade(self, m, n, p):
        '''
        Move a sequence of 'p' cards from cascade 'm' to cascade 'n'.
        Cascade 'm' must have at least 'p' cards.  The last 'p'
        cards of cascade 'm' must be in descending rank order and
        alternating colors.

        If the move can't be made, raise an IllegalMove exception.

        Arguments:
          m, n -- cascade indices (integers between 0 and 7)
          p    -- an integer >= 0

        Return value: none
        '''

        go = True
        if m > 7 or m < 0 or n > 7 or n < 0 or type(m) != int or type(n) != int:
            raise IllegalMove('IllegalMove: Bad cascade index')
        elif type(p) != int or p < 0:
            raise IllegalMove('IllegalMove: Bad sequence length')
        elif(longest_movable_sequence(cascade[m]) != p):
            raise IllegalMove('IllegalMove: No sequence of that length in cascade')
        elif len(cascade[m]) < p:
            raise IllegalMove('IllegalMove: Sequence length must be smaller than cascade length')
            go = False
        else:
            for item in self.freecell:
                nc = 0
                nf = 0
                if item == None:
                    nc += 1
            nf = 4 - len(self.foundation)
        if(p > max_cards_to_move(nc, nf) and go):
            raise IllegalMove('IllegalMove: Cannot move that number of cards')
        elif(not self.cascade[m][-p-1].goes_below(self.cascade[n][-1]) and self.cascade[m][-p-1].color != self.cascade[n][-1].color):
            raise IllegalMove('IllegalMove: Sequence cannot be moved onto that cascade.')
        else:
            for i in range(p):
                self.cascade[n].append(self.cascade[m][-i-1])
                del self.cascade[m][-i-1]


    def automove_to_foundation(self, verbose=True):
        '''
        Make as many moves as possible from the cascades/freecells to the
        foundations.

        Argument:
          verbose -- if True, print a message when each card is automoved

        Return value: none
        '''
        while True:
            for cascade in self.cascade:
                if(ok_to_automove(cascade[-1], self.foundation)):
                    self.move_cascade_to_foundation(self.cascade.index(cascade))
            for card in self.freecell:
                if(ok_to_automove(card, self.foundation)):
                    self.move_freecell_to_foundation(self.freecell.index(card))
