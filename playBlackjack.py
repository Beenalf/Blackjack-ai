"""
"I might make a blackjack ai agent"
"Why don't you do something that actually helps other 
people (10 second pause) ... like tracking Malaria"?

Plays a game of blackjack repeatedly
"""

from blackjack import Blackjack
from constants import *

def playBlackjack(bet, bank):
    """
    Plays a single game of Blackjack

    Bet: The amount of money the player wishes to bet on this game
    Bank: The total amount of cash the player has
    """
    blackjack = Blackjack(bet)

    # Deal the cards and print the board
    blackjack.deal()
    # Take the player's turn
    blackjack.takePlayerTurn()
    blackjack.takePlayerSecondTurn()
    # Take the dealer's turn
    blackjack.takeDealerTurn()
    # Show the results of the game
    result = blackjack.showResults()

    print(f"After that game, you have ${bank + result}.\n")
    return bank + result


def playGames():
    """
    Continuously plays a series of Blackjack games
    """
    playAgain = "Y"
    bank = DEFAULT_BANK_AMOUNT # The amount of money you have to bet
    print(f"\nYour starting bank balance is ${bank}.")

    while playAgain.upper() == "Y":
        bet = input(BETTING_MSG)
        bet = int(bet)
        while (bet > bank or bet < LOWER_BETTING_LIMIT or bet > UPPER_BETTING_LIMIT):
            bet = int(input(BETTING_ERROR_MSG))

        bank = playBlackjack(bet=bet, bank=bank)

        playAgain = input("Do you want to play again? (Y/N) ")
    print(f"Your ending bank balance is ${bank}.")


# Main entry point
if __name__ == "__main__":
    playGames()
