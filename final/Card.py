#
# CS 1 Final exam, 2017
#

'''
This module has functions and classes representing playing cards
and decks of cards.
'''

import random

class InvalidRank(Exception):
    pass

class InvalidSuit(Exception):
    pass

all_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
all_suits = ['S', 'H', 'D', 'C']


class Card:
    '''
    Instances of this class represent a single card in a deck of 52.
    '''

    def __init__(self, rank, suit):
        '''
        Create a card given a valid rank and suit.

        Arguments:
          rank: the card rank (an integer between 2 and 10, or 'A', 'J', 'Q',
                or 'K')
          suit: either 'S' (spades), 'H' (hearts), 'D' (diamonds), 'C' (clubs)
        '''

        self.rank = rank
        self.suit = suit
        if self.suit == 'S' or self.suit == 'C':
            self.color = 'black'
        else:
            self.color = 'red'


    def __str__(self):
        '''
        Return the string representation of the card.
        '''

        return f'{self.rank}{self.suit.lower()}'

    def goes_above(self, card):
        '''
        Return True if this card can go above 'card' on the foundations.

        Arguments:
          card -- another Card object

        Return value:
          True if this card can go above 'card' on the foundations i.e.
          if it has the same suit as 'card' and is one rank higher,
          otherwise False
        '''
        assert isinstance(card, Card)

        thisIndex = all_ranks.index(self.rank)
        otherIndex = all_ranks.index(card.rank)
        thisSuit = self.suit
        otherSuit = card.suit

        if thisIndex == otherIndex + 1 and thisSuit == otherSuit:
            return True
        else:
            return False

    def goes_below(self, card):
        '''
        Return True if this card can go below 'card' on a cascade.

        Arguments:
          card -- another Card object

        Return value:
          True if this card can go below 'card' on a cascade i.e.
          if it has the opposite color than 'card' and is one rank lower,
          otherwise False
        '''

        assert isinstance(card, Card)

        thisCardIndex = all_ranks.index(self.rank)
        otherCardIndex = all_ranks.index(card.rank)
        thisColor = self.color
        otherColor = card.color

        if thisCardIndex == otherCardIndex - 1 and thisColor != otherColor:
            return True
        else:
            return False


class Deck:
    '''
    Instances of this class represent a deck of 52 cards, 13 in each
    of four suits (spades (S), hearts (H), diamonds (D), and clubs (C).
    Ranks are 'A', 2 .. 10, 'J', 'Q', 'K'.
    '''

    def __init__(self):
        '''
        Initialize the Deck object.
        '''
        self.cards = []
        for rank in all_ranks:
            for suit in all_suits:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        '''
        Return the next card in the Deck, if there is one.
        '''
        if self.current > 51:
            raise StopIteration()
        current = self.current
        self.current += 1
        return self.cards[current]
