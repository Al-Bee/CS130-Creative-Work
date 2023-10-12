import random

class Card:
    def __init__(self, value):
        self.value = value
        self.type = self.value[0]
        self.suit = self.value[1]
        if value[1] == 0 or value[1] == 2:
            self.colour = 0 # RED
        else:
            self.colour = 1 # BLACK

    def get_type(self):
        return self.type

    def get_colour(self):
        return self.colour
    
    def get_suit(self):
        return self.suit

    def __str__(self):
        if self.type == 0:
            disp = 'A'
        elif self.type == 10:
            disp = 'J'
        elif self.type == 11:
            disp = 'Q'
        elif self.type == 12:
            disp = 'K'
        else:
            disp = self.type + 1
        if self.suit == 0:
            return f"{disp}♥"
        elif self.suit == 1:
            return f"{disp}♤"
        elif self.suit == 2:
            return f"{disp}♦"
        elif self.suit == 3:
            return f"{disp}♧"

class CardDeck:
    def __init__(self, size=4):
        suits = [0, 1, 2, 3] # H S D C
        cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # 0 = A, 10, 11, 12 = J Q K
        deck = [[j, i] for j in cards for i in suits[0:size]]
        self.deck = [Card(i) for i in deck]
        random.shuffle(self.deck)

    def flip_top(self):
        return self.deck.pop()
    
    def size(self):
        return len(self.deck)
    
    def peek(self):
        print(self.deck[-1])