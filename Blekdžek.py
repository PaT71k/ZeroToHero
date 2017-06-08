import random

# Player
class Player(object):

    def __init__(self, bankroll=100):
        self.bankroll=bankroll

    def add_bankroll(self, amount):
        self.bankroll += amount

# Debug code------------------------------------------------------------------------
sam = Player(bankroll=1000)
print(sam.bankroll)

sam.add_bankroll(12000)
print(sam.bankroll)
# Debug end-------------------------------------------------------------------------

# Cards (H hearts, D diamonds, C clubs, S spades)
type = ['H','D','C','S']
rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}


class Card:
    def __init__(self, type, rank):
        self.type = type
        self.rank = rank
        return self.type + self.rank

    def grab_type(self):
        return self.type

    def grab_rank(self):
        return self.rank

# Debug code------------------------------------------------------------------------
Karta = Card('H',10)
print(Karta)
# Debug end-------------------------------------------------------------------------
