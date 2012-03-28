# Name: Solitaire Player
# Language: Python 3.2
# Author: Christopher Olsen
# Email: co_devaccount@yahoo.com
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

# Solitaire Player
#
# This program will deal and play many successive hands
# of solitaire to explore the effectiveness of different
# strategies in Las Vegas scoring/Deal One (Klondike)
#
# in its current state this program does not practice good encapsulation
# or modularity techniques, the important variables are Globals and can
# be accessed by any method at any time.
# if it makes you feel better I'll say it's modeled after the open
# circulatory system of an invertabrate, it's totally not because I didn't
# understand basic design principles when I wrote the bulk of the code.
#
#


import math
import random
import copy

score = 0
deck = []

# global variables
hiddenStack0,hiddenStack1,hiddenStack2,hiddenStack3,hiddenStack4,hiddenStack5,\
 hiddenStack6 = [],[],[],[],[],[],[]

showingStack0,showingStack1,showingStack2,showingStack3,showingStack4,\
 showingStack5,showingStack6 = [],[],[],[],[],[],[]

dealtPile,stockPile,foundationPile1,foundationPile2,foundationPile3,\
 foundationPile4 = [],[],[],[],[],[]

hiddenStacks,showingStacks = [],[]


def dealStack(stackHeight):
    # deals the starting stacks for the game, takes the stack height as
    # an argument and returns the stack itself, dealt from the "deck"
    global deck
    stack = []
    if stackHeight == 0:
        return []
    for i in range(0,stackHeight):
        stack.append(deck.pop(-1))
    return stack


# this program was originally going to be more heavily object oriented
# though it didn't turn out that way, there are still these two classes
# they could possibly be removed to make things purely functional
class hiddenStack(list):
    def __init__(self,number):
        self.name="hiddenStack"+str(number+1)
        self.stack = dealStack(number)

class showingStack(list):
    def __init__(self,number):
        self.name="showingStack"+str(number)
        self.stack = dealStack(number)
        

def dealHand():
    # 0-12 Diamonds
    # 13-25 Clubs
    # 26-38 Hearts
    # 39-51 Spades
    # these card definitions, with alternating suit color allow the later
    # modular arithmetic
    
    # according to the rules of Klondike solitaire every game costs $52 to play
    global score
    score = score - 52
    
    global deck
    deck = []
    for i in range(0,52):
        deck.append(i)

    random.shuffle(deck)


    # what follows is the business of setting up the board.
    # (for a better understanding calling playGame() and then gameStatus()
    # in the shell a few times will show the final boards for a few games)
    # (I would like to find a better way of declaring these variables)
    global hiddenStack0,hiddenStack1,hiddenStack2,hiddenStack3,hiddenStack4
    global hiddenStack5,hiddenStack6
    
    hiddenStack0 = hiddenStack(0)
    hiddenStack1 = hiddenStack(1)
    hiddenStack2 = hiddenStack(2)
    hiddenStack3 = hiddenStack(3)
    hiddenStack4 = hiddenStack(4)
    hiddenStack5 = hiddenStack(5)
    hiddenStack6 = hiddenStack(6)
    
    global hiddenStacks
    hiddenStacks = [hiddenStack0,hiddenStack1,hiddenStack2,hiddenStack3,
                    hiddenStack4,hiddenStack5,hiddenStack6]
    
    global showingStack0,showingStack1,showingStack2,showingStack3
    global showingStack4,showingStack5,showingStack6
    
    showingStack0 = showingStack(1)
    showingStack1 = showingStack(1)
    showingStack2 = showingStack(1)
    showingStack3 = showingStack(1)
    showingStack4 = showingStack(1)
    showingStack5 = showingStack(1)
    showingStack6 = showingStack(1)

    global showingStacks
    showingStacks = [showingStack0,showingStack1,showingStack2,showingStack3,
                     showingStack4,showingStack5,showingStack6]


    global dealtPile, stockPile
    dealtPile = []
    stockPile = dealStack(24)

    global foundationPile1,foundationPile2,foundationPile3,foundationPile4
    foundationPile1 = []
    foundationPile2 = []
    foundationPile3 = []
    foundationPile4 = []

def convertToPlayingCard(cardNumber):
    # this converts card numbers for display purposes
    # takes a card number between 0 and 51 and returns
    # a card number with a suit (like Ks for king of spades
    # or 10d for ten of diamonds)
    cardValue = (cardNumber % 13) + 1

    if cardValue == 13:
        cardValue = "K"
    elif cardValue == 12:
        cardValue == "Q"
    elif cardValue == 11:
        cardValue = "J"
    elif cardValue == 1:
        cardValue == "A"
    

    if 0 <= cardNumber < 13:
        cardSuit = "d"
    elif 12 < cardNumber < 26:
        cardSuit = "c"
    elif 25 < cardNumber < 39:
        cardSuit = "h"
    elif 38 < cardNumber < 52:
        cardSuit = "s"

    playingCard = str(cardValue) + cardSuit
    
    return playingCard


def convertListToPlayingCards(listOfCards):
    #this takes a list of cards (like a hidden stack) and
    #and converts the card values (0-51) to traditional card
    #values (like Ks or 10d), returns a list of the new values
    tempList = listOfCards
    
    if len(tempList) == 0:
        return
    
    for i in range(0,len(tempList)):
        tempList[i] = convertToPlayingCard(tempList[i])

    return tempList


def stackOfXs(stack):
    # this is for displaying hidden cards (possibly for interactive play)
    # 
    Xs=[]
    for i in range(len(stack)):
        Xs.append("X")

    ##Xs = ['X']*(len(stack)+1) may be better
    return Xs
    


def gameStatus():
    # gameStatus prints the board (hidden stacks, showing stacks,
    # foundation piles) to the screen along with the current score
    print("Maneuvering Board:")

    # this shows the hidden cards on the board (Uncomment this and
    # and comment the next section to show hidden cards on the board)
##    print("Location #0","showing-->",
##          convertListToPlayingCards(copy.copy(showingStack0.stack)))
##    print("Location #1",
##          convertListToPlayingCards(copy.copy(hiddenStack1.stack)),
##          "showing-->",
##          convertListToPlayingCards(copy.copy(showingStack1.stack)))
##    print("Location #2",
##          convertListToPlayingCards(copy.copy(hiddenStack2.stack)),
##          "showing-->",
##          convertListToPlayingCards(copy.copy(showingStack2.stack)))
##    print("Location #3",
##          convertListToPlayingCards(copy.copy(hiddenStack3.stack)),
##          "showing-->",
##          convertListToPlayingCards(copy.copy(showingStack3.stack)))
##    print("Location #5",
##          convertListToPlayingCards(copy.copy(hiddenStack5.stack)),
##          "showing-->",
##          convertListToPlayingCards(copy.copy(showingStack5.stack)))
##    print("Location #6",
##          convertListToPlayingCards(copy.copy(hiddenStack6.stack)),
##          "showing-->",
##          convertListToPlayingCards(copy.copy(showingStack6.stack)))
##    print()

    #this shows X's instead of the hidden card values on the board
    print("Location #0",
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack0.stack)))
    print("Location #1",
          stackOfXs(hiddenStack1.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack1.stack)))
    print("Location #2",
          stackOfXs(hiddenStack2.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack2.stack)))
    print("Location #3",
          stackOfXs(hiddenStack3.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack3.stack)))
    print("Location #4",
          stackOfXs(hiddenStack4.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack4.stack)))
    print("Location #5",
          stackOfXs(hiddenStack5.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack5.stack)))
    print("Location #6",
          stackOfXs(hiddenStack6.stack),
          "showing-->",
          convertListToPlayingCards(copy.copy(showingStack6.stack)))
    print()

    print("DealtCards:")
    if len(dealtPile) == 0:
        print ("dealt pile stack is empty")
    else:
        print("stacked",
              convertListToPlayingCards(dealtPile[:-1]),
              "showing-->",
              convertToPlayingCard(dealtPile[-1]))

    print()
    print("Foundation Piles:")
    print("Foundation1=",convertListToPlayingCards(copy.copy(foundationPile1)))
    print("Foundation2=",convertListToPlayingCards(copy.copy(foundationPile2)))
    print("Foundation3=",convertListToPlayingCards(copy.copy(foundationPile3)))
    print("Foundation4=",convertListToPlayingCards(copy.copy(foundationPile4)))
    print()
    global score
    print("score = ",score)
    print("__________________________________________________________________")
    print()



def updateHidden():
    #updates the global |hiddenStacks| list
    global hiddenStacks,hiddenStack1,hiddenStack2,hiddenStack3,hiddenStack4
    global hiddenStack5,hiddenStack6
            
    hiddenStacks = [hiddenStack1,hiddenStack2,hiddenStack3,hiddenStack4,
                    hiddenStack5,hiddenStack6]

def updateShowing():
    #updates the global |showingStacks| list
    global showingStacks,showingStack0,showingStack1,showingStack2
    global showingStack3,showingStack4,showingStack5,showingStack6
            
    showingStacks = [showingStack0,showingStack1,showingStack2,showingStack3,
                     showingStack4,showingStack5,showingStack6]

        
def isStackMoveLegal(movingStackLocation,numberCardsMoving,
                     destinationStackLocation):
    # if a move is legal, the the stationary card's number(0-51) minus the
    # moving card's number mod26 will equal 14 this is because the deck is
    # built with alternating color: diamonds then clubs...
    #
    # takes movingStackLocation (a number between 1 and 7 for the seven stacks
    # on the board and 8 if the card is coming from the dealtPile),
    # numberCardsMoving (the size of the stack to be moved, should 12 or less)
    # and destinationStackLocation (a number between 1 and 7 of where the card
    # would move to)
    #
    # this method DOES NOT MUTATE ANYTHING!  it only returns True/False based
    # on legality of a move
    #
    # this method is called 8 or less times per card move right now, this could
    # easily grow to several dozen times per card move for a more advanced
    # playing algorithm
    global hiddenStacks, showingStacks, dealtPile

    #the order of these ifs is crucial to avoid errors
    if numberCardsMoving == 0:
        return False
    
    elif movingStackLocation == 8:
        #stack location 8 is the dealtPile
        if len(showingStacks[destinationStackLocation].stack) > 0:
            if ((showingStacks[destinationStackLocation].stack[-1]
                 - dealtPile[-1])%26 == 14):
                return True
            else:
                return False
        else:
            #if the destination stack is empty a king can move there
            if dealtPile[-1] % 13 == 12:
                return True
            else:
                return False

    elif len(showingStacks[destinationStackLocation].stack) == 0:
        #if the destination stack is empty a king can move there
        if len(showingStacks[movingStackLocation].stack) > 0:
            #this needs to bedouble-checked for logic
            if (showingStacks[movingStackLocation].stack[0] % 13 == 12
                and len(hiddenStacks[movingStackLocation].stack) != 0):
                return True
        else:
            return False

    elif (showingStacks[destinationStackLocation].stack[-1] % 13 == 0):
        #if the last card on the destination pile is an ace
        return False
        
    elif ((showingStacks[destinationStackLocation].stack[-1]
           - showingStacks[movingStackLocation].stack[-numberCardsMoving])%26
          == 14):
        # this checks the basic solitaire move, opposite color and one less can
        # be placed. This is where the alternating deal pays off
        return True
    
    else:
        return False

    
def flipHiddenCard(stackNumber):
    # this method is called when a showing stack is successfully moved from on
    # top of a hidden stack, the top card of the hidden stack is removed and
    # becomes the new showing stack
    global showingStacks,hiddenStacks
    if len(hiddenStacks[stackNumber].stack) > 0:
        showingStacks[stackNumber].stack =\
         [hiddenStacks[stackNumber].stack.pop()]


def moveStack(movingStackLocation,numberCardsMoving,stationaryStackLocation):
    # this method MOST DEFINITELY DOES MUTATE THINGS OUTSIDE ITS SCOPE!
    #
    # all legality should have already been checked by isStackMoveLegal()
    # so this method assumes it can do what it's doing
    # (it's no good to perform the legality checks in here because there
    # are so many legality checks for each actual move, plus the results of
    # those legality checks must be processed to choose the best move. If you
    # want you can call isStackMoveLegal again here and throw an exception if
    # it isn't, if that's happening there are much bigger problems afoot.)
    #
    #
    # takes |movingStackLocation|     (1-7 for showing stacks on the board and
    #                                  8 for deal pile)
    #       |numberCardsMoving|       (how many cards to pop)
    #       |stationaryStackLocation| (where to put them, a number 1-7 for
    #                                  showing stacks on the board)
    #
    # returns nothing

    global showingStacks
    global dealtPile
    global showingStack0,showingStack1,showingStack2,showingStack3
    global showingStack4,showingStack5,showingStack6
    
    movingLoc,numberMov,stayingLoc=(movingStackLocation,numberCardsMoving,
                                    stationaryStackLocation)

    if movingLoc == 8:
        #movingLoc == 8  means showing dealtPile card
        showingStacks[stayingLoc].stack = (showingStacks[stayingLoc].stack
                                           + [dealtPile.pop()])
        return
    
    #add card(s) to stationary pile
    showingStacks[stayingLoc].stack = (showingStacks[stayingLoc].stack
                                + showingStacks[movingLoc].stack[-numberMov:])
    
    #remove card(s) that were just moved
    showingStacks[movingLoc].stack=showingStacks[movingLoc].stack[0:-numberMov]
        
    #if necessary flip a hidden card over
    if len(showingStacks[movingLoc].stack) == 0:
        flipHiddenCard(movingLoc)

        
def newCard():
    # this method mutates dealtPile
    # (this deals the next card from the deck and adds it to the dealt pile)
    global dealtPile
    dealtPile.append(stockPile.pop(-1))


def isCardMoveToFoundationPileLegal(card):
    # this method takes a |card| and uses modular math to check if that card
    # can be legally placed on a foundation pile
    # returns True/False based on legality

    global foundationPile1,foundationPile2,foundationPile3,foundationPile4
    foundationPiles = [foundationPile1,foundationPile2,foundationPile3,
                       foundationPile4]

    # the aces in the deck are located at 0,13,26 and 39, so they will all = 0
    if (card % 13 == 0):
        return True
    
    # for cards 2 and above they need the card one below them (of their suit)
    # to be showing
    for pile in foundationPiles:
        if len(pile) > 0:
            if card - pile[-1] == 1:
                return True
            
    return False
        

def moveCardToFoundationPile(card):
    # THIS METHOD MUTATES THINGS OUTSIDE OF ITS SCOPE!!!
    #
    # takes a |card| and returns nothing
    # this method takes a card from either a showing pile or the deal pile
    # and moves it to the proper foundation pile
    #
    # the legality if the move should have already been determined by
    # isCardMoveToFoundationPileLegal(), but some exception handling would
    # probably be prudent here
    
    global foundationPile1,foundationPile2,foundationPile3,foundationPile4
    global score
    foundationPiles = [foundationPile1,foundationPile2,foundationPile3,
                       foundationPile4]

    if (card % 13 == 0):
        # an ace can be placed on an empty pile,if there is an ace to be placed
        # there should ALWAYS be an empty pile
        for pile in foundationPiles:
            if (len(pile) == 0):
                pile.append(card)
                break
    else:
        #any other card can only be placed on the same suit card below it
        didPlaceCard=False
        for pile in foundationPiles:
            if (len(pile) > 0):
                if card - pile[-1] == 1:
                    pile.append(card)
                    didPlaceCard=True
        if didPlaceCard==False:
            print("Error: Foundation card not placed")

    score = score + 5
    
    return


def moveCardFromFoundationPile(pile,card,stack):
    # not yet implemented in strategy, but could be useful in the future
    # this would be where you pull a card off the foundation pile and place
    # it on a showing stack so you can move another showing stack under it,
    # exposing a hidden card
    score = score - 5
    return

def bubbleSortHiddenStacks():
    # THIS METHOD DOES NOT MUTATE |hiddenStacks|
    #
    # this method takes nothing but returns(!) the order of stacks
    #
    # this method sorts the hidden stacks by length.
    #
    # this is a basic implementation of bubble sort
    # the hidden stacks are few in number and usually ordered already
    # so the performance hit vs. other sorting algorithms isn't prohibitive(?)

    global hiddenStacks

    hiddenStacksCopy = hiddenStacks
    swapped = True
    
    while swapped:
        swapped = False

        numberOfStacks = len(hiddenStacksCopy)
        if int(numberOfStacks) <= 1:
            break
        
        for i in range (0,len(hiddenStacksCopy) - 1):
            length1 = len(hiddenStacks[i].stack)
            if len(hiddenStacksCopy[i].stack) >\
                len(hiddenStacksCopy[i+1].stack):
                
                hiddenStacksCopy[i], hiddenStacksCopy[i+1] =\
                 hiddenStacksCopy[i+1],hiddenStacksCopy[i]
                swapped = True

    stackSizeOrder = [stack.name[-1] for stack in hiddenStacksCopy]
    stackSizeOrder.reverse()
    
    return stackSizeOrder

def makeBestMove():
    # THIS METHOD MUTATES THINGS OUTSIDE ITS SCOPE!!!
    #
    # this method takes no arguments and returns True/False
    # True signifies a move was made
    # False means there were no legal moves(generally triggers a new card deal
    # elsewhere)
    #
    # The actual logic is in the order the moves are attempted, what is assumed
    # to be the best move is tried first (based on the idea that you want to
    # move cards off of the largest hidden piles first)
    #
    # This is where new strategy ideas can be implemented
    # 
    
    global showingStacks, hiddenStacks, dealtPile

    hiddenStacksOrderedBySize = bubbleSortHiddenStacks()
    
    for i in range(len(hiddenStacks)):
        # try all showing cards in descending order of the size of the hidden
        # pile they are on
        stackNumber = hiddenStacksOrderedBySize[i]

        for j in range(0,6):
            #check the possible destinations on the board
            if isStackMoveLegal(i,len(showingStacks[i].stack),j):
                moveStack(i,len(showingStacks[i].stack),j)
                return True

        if len(showingStacks[i].stack) > 0:
            #check possible destinations in the foundation piles
            if isCardMoveToFoundationPileLegal(showingStacks[i].stack[-1]):
                moveCardToFoundationPile(showingStacks[i].stack[-1])
                showingStacks[i].stack.pop()
                if len(hiddenStacks[i].stack) > 0:
                    flipHiddenCard(i)
                return True

    if len(dealtPile) > 0:
        #move deal card to foundation or maneuver pile if possible
        if isCardMoveToFoundationPileLegal(dealtPile[-1]):
            moveCardToFoundationPile(dealtPile.pop())
            return True

        for i in range(0,6):
                if isStackMoveLegal(8,1,i):
                    #moveStack(8,...) means card is coming from the dealt pile
                    moveStack(8,1,i)
                    return True

    return False

def resetScore():
    global score
    score = 0

def playGame():
    # this deals and plays one game
    # returns True if the game was won (all cards moved to foundation piles)
    #         False if the game was not won
    global stockPile,dealtPile,numberOfGames,numberOfGamesWon

    dealHand()
    
    # gameStatus()
    i = 0
    while True:
        #checks for a win
        if len(foundationPile1) == 13 and len(foundationPile2) == 13 and\
             len(foundationPile3) == 13 and len(foundationPile4) == 13:
            print("Congratulations!  You are in the presence of \
                              a computer that just dealt and won a game of \
                              solitaire!")
            numberOfGamesWon += 1
            return True

        # checks for a win (alternate implementation)
##        if len(foundationPile1) == 13:
##            if len(foundationPile2) == 13:
##                if len(foundationPile3) == 13:
##                    if len(foundationPile4) == 13:
##                        print("Congratulations!  You are in the presence of \
##                              a computer that just dealt and won a game of \
##                              solitaire!")
##                        numberOfGamesWon += 1
##                        return True

                    
        # This might be confusing style.  makeBestMove() mutates the heck out
        # of things. It's being called here for exactly that reason, to
        # actually make a move, the fact that it's in an |if| statement may be
        # misleading.  makeBestMove() will return False if it failed to make a
        # move, which means a new card needs to be dealt.
        if makeBestMove() == False:
            # if no possible moves, deal a card
            if len(stockPile) > 0:
                newCard()
            # if no possible moves, and no cards left to deal, the game is over
            else:
                return False
            
 
        if i == 10000:
            # breaks out of infinite loops, primitive error handling, should
            # never happen
            print()
            print("This game failed to finish within 10,000 loops of the \
                  main routine")
            print("Final game status for debugging is:")
            gameStatus()
            return False
        i=i+1

    # this is here in case the |while| loop was somehow broken out of
    return False


    

# this can be placed in playGame(), but for *many* games it just slows things
# down and clutters the screen
##    print()
##    print("The game is over, the final status is:")
##    print()
##    gameStatus()
##
##    print("___________________________________________________________\
##          ___________")
##    print("***********************************************************\
##          ***********")
##    print("***********************************************************\
##          ***********")



###############################################################################


# this (below) is the method to call when you want to play a whole bunch of
# games of solitaire - I've gone as high as a million games but the average
# winnings starts to calm down before five thousand games.  You'll need to
# change the |fileName| destination to where you'd like the data to be stored,
# unless you're on a Mac and your account happens to be named |christopher|,
# then it will be saved to your desktop.  The .csv file can be opened by
# OpenOffice and I would assume Excel should be at least as competent.  

import time
numberOfGames = 0
numberOfGamesWon = 0

def playMultipleGames(number):
    global numberOfGames,numberOfGamesWon
    numberOfGames = number
    
    #this creates a .csv file for data
    fileName = input("Please enter a name for data file:  ")

    # this will save into the same directory that the program is in
    fileName = fileName + ".csv"
    dataFile = open(fileName,'w')
    start = time.time()
    dataFile.write("Start time:"+","+str(time.asctime(time.localtime(start)))+
                   "\n")
    dataFile.write("Game Number"+","+"Total Winnings"+","+"Game Winnings"+","+
                   "Game Won"+"\n")
    print("Running...")
    
    #main loop
    lastScore = score
    for i in range(0,number):
        won = playGame()
        dataFile.write(str(i+1)+","+str(score)+","+str(score-lastScore)+","+
                       str(won)+"\n")
        lastScore=score
    
    stop = time.asctime(time.localtime(time.time()))
    dataFile.write("End time:"+","+
                   str(time.asctime(time.localtime(time.time())))+
                   ",Time elapsed:, %s seconds"%str(start-time.time())+"\n")           
    print ()
    print ("Final score for",number,"games is",score)
    print (numberOfGamesWon,"games were won out of",numberOfGames,
           "for an average win rate of",float(numberOfGamesWon)/numberOfGames)
    print ("average amount lost per game was",float(score)/numberOfGames)
    print ()
    print ("View ",fileName,"for more data")
    print ()

