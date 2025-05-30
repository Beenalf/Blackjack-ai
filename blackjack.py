"""
Implements an instance of a game of blackjack
"""

from constants import *
import random

class Blackjack():

    def __init__(self, bet):
        # Deck, hand, and bet variables
        self.bet = bet
        self.profit = 0 # Tracks changes to the player's balance during the game (e.g. insurance)
        self.dealerHand = []
        self.playerHand = []
        self.playerHand2 = [] # For when the player splits their hand
        self.deck = [[rank, suite] for rank in ranks.keys() for suite in suites]

        # Game state
        self.gameEnded = False
        self.naturalBlackjack = False
        self.hasSplit = False
        self.hasDoubled = False
        self.hasInsurance = False

    def printBoard(self, showDealerCards = False):
        """
        Prints out the board with the current cards
        """
        print("+-------------------------------------+")
        print("|            Dealer's hand            |")
        if showDealerCards:
            print("| " + ", ".join(f"{rank} of {suiteSymbols[suite]}" for rank, suite in self.dealerHand).center(35) + " |")
        else:
            temp = self.dealerHand[0]
            self.dealerHand[0] = MYSTERY_CARD
            print("| " + ", ".join(f"{rank} of {suiteSymbols[suite]}" for rank, suite in self.dealerHand).center(35) + " |")
            self.dealerHand[0] = temp
        print("|                                     |")
        print("|                                     |")
        print("| " + ", ".join(f"{rank} of {suiteSymbols[suite]}" for rank, suite in self.playerHand).center(35) + " |")
        print("|            Player's hand            |")
        if self.hasSplit:
            print("|                                     |")
            print("| " + ", ".join(f"{rank} of {suiteSymbols[suite]}" for rank, suite in self.playerHand2).center(35) + " |")
            print("|         Player's second hand        |")
        print("+-------------------------------------+\n")


    def getHandValue(self, hand):
        """
        Returns the numerical value of a hand
        """
        total = sum(ranks[card[0]] for card in hand)
        aceOneTotal = sum(ranksAceOne[card[0]] for card in hand)
        # print(f"Sum for {hand}: {total}")
        if total > aceOneTotal and total > 21:
            return aceOneTotal
        return total


    def deal(self):
        """
        Deals out 2 cards each to the player and dealer. Then,
        shows the board and checks if the player can purchase
        insurance, double their bet, or split their cards. Finally, it
        checks if the player has a natural blackjack.
        """
        # Deal out the first 4 cards
        iteration = 0
        while iteration < 4:
            cardNumber = random.randint(0, len(self.deck) - 1)
            randomCard = self.deck.pop(cardNumber)
            if iteration % 2 == 0:
                self.playerHand.append(randomCard)
            else:
                self.dealerHand.append(randomCard)
            iteration += 1

        print(f"\n~~~~~ Starting blackjack game! ~~~~~")
        print(f"You are playing for ${self.bet}.")
        self.printBoard(showDealerCards=False)

        # Handle advanced first-round actions (insurance, doubling, splitting)
        if self.canPurchaseInsurance():
            purchase = input(f"Would you like to purchase insurace for ${self.bet // 2}? (Y/N)")
            self.purchaseInsurance(purchase)
        elif self.canDouble():
            double = input(f"Would you like to double your bet of ${self.bet}? (Y/N)")
            self.double(double)
        elif self.canSplit():
            split = input(f"Would you like to split your deck? (Y/N)")
            self.split(split)

        # Check if the player or dealer has a natural blackjack
        if self.getHandValue(self.playerHand) == BLACKJACK:
            self.gameEnded = True
            self.naturalBlackjack = True
        elif self.getHandValue(self.dealerHand) == BLACKJACK:
            # self.gameEnded = True
            if self.hasInsurance:
                self.profit = self.bet # The player wins back the value of their original bet

        
    def takePlayerTurn(self):
        """
        Takes the player's turn (By hitting until the player chooses to
        stand or reaches 5 cards in their hand).
        """
        if self.hasSplit:
            print(FIRST_HAND_MSG)

        while len(self.playerHand) <= MAX_CARD_HAND:
            if self.gameEnded:
                return

            action = input("Would you like to stand or hit? (stand/hit) ")
            while action not in VALID_ACTIONS:
                action = input("Would you like to stand or hit? (stand/hit) ")
        
            if action in HITS:
                self.hit(self.playerHand)
                self.printBoard(showDealerCards=False)
            else:
                self.stand()
                return
            

    def takePlayerSecondTurn(self):
        """
        Takes the player's second turn (for their second hand after splitting).
        If the player has not split this hand, nothing will happen.
        """
        if not self.hasSplit:
            return
        
        print(SECOND_HAND_MSG)

        while len(self.playerHand2) <= MAX_CARD_HAND:
            if self.getHandValue(self.playerHand2) > BLACKJACK:
                return

            action = input("Would you like to stand or hit? (stand/hit) ")
            while action not in VALID_ACTIONS:
                action = input("Would you like to stand or hit? (stand/hit) ")
        
            if action in HITS:
                self.hit(self.playerHand2)
                self.printBoard(showDealerCards=False)
            else:
                self.stand()
                return


    def takeDealerTurn(self):
        """
        Takes the dealer's turn (hitting until their hand is worth >= 17)
        """
        #if self.gameEnded:
        #    return
        
        while self.getHandValue(self.dealerHand) < DEALER_STAND_THRESHOLD:
            self.hit(self.dealerHand)


    def stand(self):
        """
        The player stands
        """
        pass


    def hit(self, targetDeck):
        """
        The player hits (gets a new card)

        targetDeck: The deck of the player/dealer who is hitting
        """
        cardNumber = random.randint(0, len(self.deck) - 1)
        newCard = self.deck.pop(cardNumber)
        targetDeck.append(newCard)

        # Check if the player/dealer hitting has busted
        if self.getHandValue(targetDeck) >= BUST_THRESHOLD:
            self.gameEnded = True

    
    def getHandResults(self, hand):
        """
        Returns the amount of money the hand has won/lost against
        the dealer. This function also prints out the winner.
        """
        # The player busts
        if self.getHandValue(hand) >= BUST_THRESHOLD:
            print(DEALER_WON.format(bet=self.bet))
            return -1 * self.bet + self.profit
        # There is a tie
        elif self.getHandValue(hand) == self.getHandValue(self.dealerHand):
            print(TIE)
            return 0 + self.profit
        # The player wins
        elif self.getHandValue(self.dealerHand) < self.getHandValue(hand) or \
                self.getHandValue(self.dealerHand) >= BUST_THRESHOLD:
            if self.naturalBlackjack:
                print(PLAYER_WON_NATURAL.format(bet=self.bet * NATURAL_BLACKJACK_MULTIPLIER))
                return self.bet * NATURAL_BLACKJACK_MULTIPLIER + self.profit
            else:
                print(PLAYER_WON.format(bet=self.bet))
                return self.bet + self.profit
        # The dealer wins
        else:
            print(DEALER_WON.format(bet=self.bet))
            return -1 * self.bet + self.profit
    

    def showResults(self):
        """
        Shows the results of the blackjack game. This function should only be
        called once the game has ended.

        Returns the amount of money the player has made in this blackjack game. A
        positive amount means they made money, while a negative amount means they
        lost money to the dealer.
        """
        # First, print the board out
        print("\nThe game has ended!")
        self.printBoard(showDealerCards=True)

        # Print out the winner and return the monetary change
        result = self.getHandResults(self.playerHand)
        if self.hasSplit:
            result += self.getHandResults(self.playerHand2)

        return result
        

    def canSplit(self):
        """
        Checks if the player is allowed to split their deck.

        Returns True if they can split, and False otherwise.
        """
        if len(self.playerHand) != 2:
            return False
        if ranks[self.playerHand[0][0]] == ranks[self.playerHand[1][0]]:
            return True
        return False
    

    def split(self, action):
        """
        Split the player's hand
        """
        if action.upper() == "Y":
            print(SPLIT_DECK)
            self.hasSplit = True
            secondCard = self.playerHand.pop(1)
            self.playerHand2.append(secondCard)
        else:
            print(DONT_SPLIT_DECK)


    def canDouble(self):
        """
        Checks if the player is allowed to double their bet

        Returns True if they can double, and False otherwise.
        """
        if len(self.playerHand) != 2:
            return False
        if self.getHandValue(self.playerHand) in DOUBLE_VALUES:
            return True
        return False


    def double(self, action):
        """
        Doubles the player's bet
        """
        if action.upper() == "Y":
            print(DOUBLE_BET.format(amount = self.bet * 2))
            self.hasDoubled = True
            self.bet *= 2
        else:
            print(DONT_DOUBLE_BET)


    def canPurchaseInsurance(self):
        """
        Checks if the player can purchase insurance

        Returns True if they can purchase insurance, and False otherwise
        """
        if len(self.playerHand) != 2:
            return False
        if ace == self.dealerHand[1][0]:
            return True
        return False


    def purchaseInsurance(self, action):
        """
        Purchases insurance against the dealer's natural blackjack
        """
        if action.upper() == "Y":
            print(PURCHASE_INSURANCE.format(amount = self.bet / 2))
            self.hasInsurance = True
            self.profit = -1 * self.bet / 2
        else:
            print(DONT_PURHCASE_INSURANCE)

