"""
Constants for the blackjack games
"""

# Card types
players = ["PLAYER", "DEALER"]
suites = ["hearts", "diamonds", "clubs", "spades"]
suiteSymbols = {
    "spades": '\u2660', 
    "hearts": '\u2665',
    "diamonds": '\u2666',
    "clubs": '\u2663',
    "???": '???'
}
ranks = {"2": 2, "3": 3, "4":4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
ranksAceOne = {"2": 2, "3": 3, "4":4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 1}
ace = "A"

# Betting settings
LOWER_BETTING_LIMIT = 2
UPPER_BETTING_LIMIT = 500
NATURAL_BLACKJACK_MULTIPLIER = 1.5
DEFAULT_BET = 10
DEFAULT_BANK_AMOUNT = 1000
BETTING_MSG = "How much would you like to bet on this game? $"
BETTING_ERROR_MSG = f"Try again. Please enter an integer between "\
    f"${LOWER_BETTING_LIMIT} and ${UPPER_BETTING_LIMIT}, and below your bank balance. $"

# Gameplay settings
MAX_CARD_HAND = 5
BLACKJACK = 21 # The maximum score a player can achieve
BUST_THRESHOLD = 22 # A player busts if their card values exceed this number
DEALER_STAND_THRESHOLD = 17 # The dealer must stand if their cards are >= 17
DOUBLE_VALUES = [9, 10, 11]
MYSTERY_CARD = ["?", "???"]
VALID_ACTIONS = ["stand", "STAND", "hit", "HIT", "s", "S", "h", "H"]
STANDS = ["stand", "STAND", "s", "S"]
HITS = ["hit", "HIT", "h", "H"]
DEALER_WON = "The dealer won this round. You lost {bet}."
TIE = "This round is a tie."
PLAYER_WON = "You won this round. You make a {bet} profit."
PLAYER_WON_NATURAL = "You won this round with a natural blackjack. You make a {bet} profit."

# Advanced action messages
PURCHASE_INSURANCE = "You purchased insurance for ${amount}."
DONT_PURHCASE_INSURANCE = "You chose not to purchase insurance."
DOUBLE_BET = "You have doubled your bet. It is now ${amount}."
DONT_DOUBLE_BET = "You chose not to double your bet."
SPLIT_DECK = "You have split your deck."
DONT_SPLIT_DECK = "You chose not to split your deck."