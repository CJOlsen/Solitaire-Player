# Name: Solitaire Player
# Language: Python 2.7.3
# Contact: github/cjolsen/solitaire-player
#
# License:
##
##    Copyright (C) 2012  Christopher Olsen
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##


import random

class Card(object):
    """ The card object has an index number which defines its value,
        as well as attributes for the rank, suit, and display.
        """
    def __init__(self, index=None):
        self.index = index
        if index >= 0 and index < 13:
            self.suit = 'D'
        elif index > 12 and index < 26:
            self.suit = 'C'
        elif index > 25 and index < 39:
            self.suit = 'H'
        else:
            self.suit = 'S'

        self.rank = str((index % 13) + 1)

        if self.rank == '1':
            self.rank = 'A'
        elif self.rank == '11':
            self.rank = 'J'
        elif self.rank == '12':
            self.rank = 'Q'
        elif self.rank == '13':
            self.rank = 'K'

        self.display = self.rank + self.suit


class Stack(object):
    """ The stack object is an ordered list of cards.  It is a parent class,
        the different board stacks all inherit from it.
        """
    def __init__(self, cards):
        assert type(cards) == list
        self.cards = cards

    def __add__(self, other):
        """ Overriding the + operator for custom addition of stacks
            """
        assert isinstance(other, Stack)
        return Stack(self.cards + other.cards)

    def take(self, number):
        """ This method takes a number
            Removes that number of cards from the stack
            Returns the removed cards as a stack
            """
        moving_cards = self.cards[-number:]
        self.cards = self.cards[:-number]
        return Stack(moving_cards)

    
class Deck(object):
    """ The deck is a list from 0 to 51 representing a deck of playing cards. 
        To facilitate math later on, diamonds are 0 through 12, clubs 13 through
        25, hearts 26 through 38, and spades 39 through 51.  The deck knows how
        to shuffle itself.
        """
    def __init__(self):
        self.cards = [Card(x) for x in range(52)]
    
    def shuffle(self):
        """ Takes nothing (self implied)
            This randomizes the order of the cards.
            Returns: nothing.
            """
        self.cards = random.shuffle(self.cards)

    def deal(self, number):
        """ Takes a number
            Returns: that number of cards
            """
        cards = self.cards[-number:]
        self.cards = self.cards[:-number]
        return Stack(cards)
        


class HiddenStack(object):
    """ The hidden stack is the representation of the 6 hidden stacks dealt
        to the board at the beginning of the game.  Includes a method to 
        flip the top card over to an empty showing stack, if there.
        """
    def __init__(self, cards=None):
        self.stack = Stack(cards)
        self.type = "Hidden"


class ShowingStack(object):
    """ The showing stack starts with one card at the beginning of the game.
        These can be moved, added to and split into two smaller stacks if the
        board permits.
        """
    def __init__(self, cards=None):
        self.stack = Stack(cards)
        self.type = "Showing"

class FoundationPile(object):
    """ The foundation piles start empty at the beginning of the game and then
        can be added to in ascending order with cards of the foundation pile's
        suit.  Cards can be removed one at a time if the board permits.
        """
    def __init__(self, cards=None):
        self.stack = Stack(cards)
        self.type = "Foundation"


class StockPile(object):
    """ The stock pile is the stack of cards yet to be played in a round of
        solitaire.  Cards can be pulled from it one at a time.
        """
    def __init__(self, cards=None):
        self.stack = Stack(cards)
        self.type = "Stock"

class DiscardPile(object):
    """ The discard pile is the stack of cards that have been played in a round
        of solitaire.  The top card of the discard pile is always available for
        play.
        """
    def __init__(self, cards=None):
        self.stack = Stack(cards)
        self.type = "Discard"


class Move(object):
    """ The move object is made up of the location of a card to be moved, and 
        the destination where it would move to.
        """
    def __init__(self, sending_stack=None, receiving_stack=None, 
                 moving_stack=None):
        x = y
    def execute(self):
        """actually make the move"""
        


# Should these just be move types within the Move class??? Have it be a
# required field?
##class FoundationToShowing(Move):
##    
##class ShowingToFoundation(Move):
##    
##class DiscardToFoundation(Move):
##    
##class DiscardToShowing(Move):
##    
##class DealToDiscard(Move):
##    
##class ShowingToShowing(Move):
##    

        
class Board(object):
    """ The board includes all that is needed for a game of solitaire: a deck,
        six hidden piles (plus one empty hidden pile) and seven showing piles, 
        four foundation piles, one stock pile initially comprised of all cards
        not dealt at the start of the game, and one discard pile initially 
        empty.
        """
    def __init__(self):
        self.deck = Deck().shuffle()

        
        

    def execute_move(move):
        """ This is the procedure that carries out a move after it has been
             chosen.
             """
        pass

    def game_status():
        """ Print the board to the screen
            """
        pass

class Table(object):
    """ The table is the environment for games of solitaire.
        A table may instantiate one board for one game, or many boards
        for many games.
        """
    def __init__(self):
        board = None
        boards = []

    def play_game():
        """ Plays one game of solitaire
            Returns a score for the game
            """
        pass

    def play_multiple_games(number):
        """ Plays multiple games
            """
        score = 0
        for i in range(number):
            score += play_game()

        return score
            
        

        
    
