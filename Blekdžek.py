import random
playing = False
bet = 1
chip_pool = 250
restart_phrase = "Stisni 'd' za ponovno dijeljenje karata ili stisni 'q' za izlaz."

# Player
class Player(object):

    def __init__(self, bankroll=250):
        self.bankroll=bankroll

    def add_bankroll(self, amount):
        self.bankroll += amount

# Cards (H hearts, D diamonds, C clubs, S spades)
suits = ['H', 'D', 'C', 'S']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#Karta
class Card:
    def __init__(self, type, rank):
        self.type = type
        self.rank = rank

    def card(self):
        return self.type + self.rank

    def grab_type(self):
        return self.type

    def grab_rank(self):
        return self.rank

# Hand
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = []

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'U ruci imaš' % hand_comp

    def card_add(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

# Deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "U deku su:" + deck_comp

#Hit
def hit():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

        print (  "U ruci imaš" % player_hand)

        if player_hand.calc_val() > 21:
            result = 'Busted! ' + restart_phrase

            chip_pool -= bet
            playing = False

    else:
        result = "Nemoguče je hitati trenutno." + restart_phrase

    game_step()

#Stand
def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Nemoguče je standati trenutno."
    else:

        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 21:
            result = 'Pobjeda!' + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'Pobjeda!' + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Izjednačeno!' + restart_phrase
            playing = False

        else:
            result = 'Izgubio si!' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()


def game_step():
    print('U ruci imaš: ',player_hand)

    print('Ukupna vrijedonst tvojih karata: ' + str(player_hand.calc_val()))

    print('Kuča u ruci ima: ',dealer_hand)

    if playing == False:
        print(" --- za" + str(dealer_hand.calc_val()))

        print( "Ukupni žetoni: " + str(chip_pool))

    else:
        print ("još jedna karta je naopačke")

    print (result)

    player_input()

def make_bet():

    global bet
    bet = 0

    print (' Koliko chipova želis dati? (Unesi cijeli broj) ')

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)
        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print ("Nemoguča oklada, imaš samo " + str(chip_pool) + " chipova.")

def deal_cards():

    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()

    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Unesi h ili s: "

    if playing == True:
        print ('Preklopljeno!')
        chip_pool -= bet

    playing = True
    game_step()

def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print ("Nemoguć unos! Molim te unesi h, s, d, ili q: ")
        player_input()

def game_exit():
    print ('Hvala što is igrao!')
    exit()

deck = Deck()
deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()
deal_cards()