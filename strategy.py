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


class MovesGetter(object):
    """ This class is a wrapper for all of the different 'get moves'
        procedures.  It allows the syntax GetMoves.all_moves(board).
        
        """
    # could use a better name?
    def __init__():
        self.moves = []
        
    def showing_to_foundation(board):
        """ Given a board, this procedure returns a list of all
            moves from the showing stacks on the board to the 
            foundation piles
            """

    def showing_to_showing(board):


    def discard_to_foundation(board):

    def discard_to_showing(board):

    def foundation_to_showing(board):

    def deal_to_discard(board):


    def all_moves(board):
        """ Given a board, this procedure returns a list of all 
            possible moves 
            """
        
class BestMoveChooser(object):
    """ This is a wrapper for all of the move choosing logic.
        will be replacing:

        ##def makeBestMove():
        ##    # THIS METHOD MUTATES THINGS OUTSIDE ITS SCOPE!!!
        ##    #
        ##    # this method takes no arguments and returns True/False
        ##    # True signifies a move was made
        ##    # False means there were no legal moves(generally triggers a new card deal
        ##    # elsewhere)
        ##    #
        ##    # The actual logic is in the order the moves are attempted, what is assumed
        ##    # to be the best move is tried first (based on the idea that you want to
        ##    # move cards off of the largest hidden piles first)
        ##    #
        ##    # This is where new strategy ideas can be implemented
        ##    # 
        ##    
        ##    global showingStacks, hiddenStacks, dealtPile
        ##
        ##    hiddenStacksOrderedBySize = bubbleSortHiddenStacks()
        ##    
        ##    for i in range(len(hiddenStacks)):
        ##        # try all showing cards in descending order of the size of the hidden
        ##        # pile they are on
        ##        stackNumber = hiddenStacksOrderedBySize[i]
        ##
        ##        for j in range(0,6):
        ##            #check the possible destinations on the board
        ##            if isStackMoveLegal(i,len(showingStacks[i].stack),j):
        ##                moveStack(i,len(showingStacks[i].stack),j)
        ##                return True
        ##
        ##        if len(showingStacks[i].stack) > 0:
        ##            #check possible destinations in the foundation piles
        ##            if isCardMoveToFoundationPileLegal(showingStacks[i].stack[-1]):
        ##                moveCardToFoundationPile(showingStacks[i].stack[-1])
        ##                showingStacks[i].stack.pop()
        ##                if len(hiddenStacks[i].stack) > 0:
        ##                    flipHiddenCard(i)
        ##                return True
        ##
        ##    if len(dealtPile) > 0:
        ##        #move deal card to foundation or maneuver pile if possible
        ##        if isCardMoveToFoundationPileLegal(dealtPile[-1]):
        ##            moveCardToFoundationPile(dealtPile.pop())
        ##            return True
        ##
        ##        for i in range(0,6):
        ##                if isStackMoveLegal(8,1,i):
        ##                    #moveStack(8,...) means card is coming from the dealt pile
        ##                    moveStack(8,1,i)
        ##                    return True
        ##
        ##    return False

        """
    def __init__(self):
        pass
