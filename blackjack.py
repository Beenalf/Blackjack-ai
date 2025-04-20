"""
Implements an instance of a game of blackjack
"""

from constants import *

class Blackjack():

    def __init__(self, bet):
        self.bet = bet
        self.turn = players[0]
        self.dealerHand = []
        self.playerHand = []
        self.deck = [[rank, suite] for rank in ranks.keys() for suite in suites]

    def printBoard(showDealerCards = False):
        """
        Prints out the board with the current cards
        """
        pass

    def deal(self):
        """
        Deals out 2 cards each to the dealer and player
        """
        pass
    
    def stand(self):
        """
        The player stands
        """
        pass

    def hit(self):
        """
        The player hits
        """
        pass
    
    def hasEnded(self):
        """
        Checks if either the player or the dealer have reached 21 or busted
        """
        pass