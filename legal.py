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
##
## This file is where all the legality checks are stored to keep them
## seperate from the strategy section
##

def is_legal(board, move):
    """ This procedure takes a board object and a move object and checks the
        legality of the move.
        Returns: a True of False value.
        """

####    Will be replacing:
####
####    def isStackMoveLegal(movingStackLocation,numberCardsMoving,
####                     destinationStackLocation):
####    # if a move is legal, the the stationary card's number(0-51) minus the
####    # moving card's number mod26 will equal 14 this is because the deck is
####    # built with alternating color: diamonds then clubs...
####    #
####    # takes movingStackLocation (a number between 1 and 7 for the seven stacks
####    # on the board and 8 if the card is coming from the dealtPile),
####    # numberCardsMoving (the size of the stack to be moved, should 12 or less)
####    # and destinationStackLocation (a number between 1 and 7 of where the card
####    # would move to)
####    #
####    # this method DOES NOT MUTATE ANYTHING!  it only returns True/False based
####    # on legality of a move
####    #
####    # this method is called 8 or less times per card move right now, this could
####    # easily grow to several dozen times per card move for a more advanced
####    # playing algorithm
####    global hiddenStacks, showingStacks, dealtPile
####
####    #the order of these ifs is crucial to avoid errors
####    if numberCardsMoving == 0:
####        return False
####    
####    elif movingStackLocation == 8:
####        #stack location 8 is the dealtPile
####        if len(showingStacks[destinationStackLocation].stack) > 0:
####            if ((showingStacks[destinationStackLocation].stack[-1]
####                 - dealtPile[-1])%26 == 14):
####                return True
####            else:
####                return False
####        else:
####            #if the destination stack is empty a king can move there
####            if dealtPile[-1] % 13 == 12:
####                return True
####            else:
####                return False
####
####    elif len(showingStacks[destinationStackLocation].stack) == 0:
####        #if the destination stack is empty a king can move there
####        if len(showingStacks[movingStackLocation].stack) > 0:
####            #this needs to bedouble-checked for logic
####            if (showingStacks[movingStackLocation].stack[0] % 13 == 12
####                and len(hiddenStacks[movingStackLocation].stack) != 0):
####                return True
####        else:
####            return False
####
####    elif (showingStacks[destinationStackLocation].stack[-1] % 13 == 0):
####        #if the last card on the destination pile is an ace
####        return False
####        
####    elif ((showingStacks[destinationStackLocation].stack[-1]
####           - showingStacks[movingStackLocation].stack[-numberCardsMoving])%26
####          == 14):
####        # this checks the basic solitaire move, opposite color and one less can
####        # be placed. This is where the alternating deal pays off
####        return True
####    
####    else:
####        return False
    pass


