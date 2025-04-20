"""
"I might make a blackjack ai agent"
"Why don't you do something that actually helps other 
people (10 second pause) ... like tracking Malaria"?

Plays a game of blackjack repeatedly
"""

from blackjack import Blackjack
from constants import *

def playBlackjack(bet=10):
    """
    Plays a single game of Blackjack
    """
    pass


def playGames():
    """
    Continuously plays a series of Blackjack games
    """
    playAgain = "Y"

    while playAgain == "Y":
        bet = DEFAULT_BET
        blackjack = Blackjack(bet=bet)
        playAgain = input("Do you want to play again? (Y/N)")


# Main entry point
if __name__ == "__main__":
    playGames()
