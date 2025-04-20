"""
Constants for the blackjack games
"""

# Card types
players = ["PLAYER", "DEALER"]
suites = ["hearts", "diamonds", "clubs", "spades"]
ranks = {"2": 2, "3": 3, "4":4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "jack": 10, "queen": 10, "king": 10, "ace": [1, 11]}

# Betting settings
LOWER_BETTING_LIMIT = 2
UPPER_BETTING_LIMIT = 500
NATURAL_BLACKJACK_MULTIPLIER = 1.5
DEFAULT_BET = 10

# Gameplay settings
MAX_CARD_HAND = 5
DEALER_STAND_THRESHOLD = 17 # The dealer must stand if their cards are >= 17