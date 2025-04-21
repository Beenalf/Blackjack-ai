"""
"I might make a blackjack ai agent"
"Why don't you do something that actually helps other 
people (10 second pause) ... like tracking Malaria"?

Plays a game of blackjack repeatedly
"""

from blackjack import Blackjack
from constants import *

def playBlackjack(bet):
    """
    Plays a single game of Blackjack
    """
    blackjack = Blackjack(bet)

    # Deal the cards and print the board
    blackjack.deal()
    # Take the player's turn
    blackjack.takePlayerTurn()
    # Take the dealer's turn
    blackjack.takeDealerTurn()
    # Show the results of the game
    blackjack.showResults()


def playGames():
    """
    Continuously plays a series of Blackjack games
    """
    playAgain = "Y"

    while playAgain.upper() == "Y":
        bet = DEFAULT_BET
        playBlackjack(bet=bet)
        playAgain = input("Do you want to play again? (Y/N)")


# Main entry point
if __name__ == "__main__":
    playGames()
