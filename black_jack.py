import random

suits = ('Heart','Spade','Club','Diamond')
ranks= ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values= {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}


class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))

    def __str__(self):
        deck_comp = ""
        for c in self.deck:
            deck_comp += '\n' + c.__str__()
        return "The Deck has:" + deck_comp

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        single_card= self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        #Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Enter Number of Chips you want to play"))
        except:
            print ("Enter only Integer")
        else:
            if chips.bet > chips.total:
                print ("You dont have enough chips to bet. You have {} chips available.".format(chips.total))


def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


def hit_or_stand(deck,hand):
    global player
    while True:
        x = input ("Hit or Stand?? h or s")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print ("Player Decided to Stand. Dealer's Turn")
            playing = False
        else:
            print ("sorry I could not understand that!!!")
            continue
        break


