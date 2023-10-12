from Card import CardDeck
from Banner import play_banner

class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.suits = int(self.num_cards / 13)
        self.num_piles = int(self.num_cards / 13 + (self.suits * 2))
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]
    
    def display(self):
        for i in range(0, self.suits * 2):
            print(f"{i}: ",end='')
            print(f"{self.piles[i].print_all(i) if self.piles[i].print_all(i) != None else ''}", end='')
            if i == 0:
                print()
        print("--------------------")
        for i in range(self.suits * 2, self.num_piles):
            print(f"{i}(A): ",end='')
            print(f"{self.piles[i].print_all(i) if self.piles[i].print_all(i) != None else ''}", end='')
        print()

    def valid_move(self, p1, p2):
        return (self.piles[p2].peek_bottom().get_type() == self.piles[p1].peek_top().get_type() + 1 and
                    self.piles[p2].peek_bottom().get_colour() != self.piles[p1].peek_top().get_colour())

    def move(self, p1, p2):
        if p1 == p2 == 0 and self.piles[p1].size() > 0: # Main pile -> Main pile
            self.piles[p1].add_bottom(self.piles[p1].remove_top())
        elif p1 == 0 and self.piles[p1].size() > 0 and p2 > 0:
            if p2 > self.suits * 2 - 1: # Main pile -> Ace pile
                if self.piles[p2].size() == 0 and self.piles[p1].peek_top().get_type() == 0:
                    self.piles[p2].add_bottom(self.piles[p1].remove_top())
                elif (self.piles[p2].size() > 0 and 
                    self.piles[p2].peek_bottom().get_type() == self.piles[p1].peek_top().get_type() - 1 and
                    self.piles[p2].peek_bottom().get_suit() == self.piles[p1].peek_top().get_suit()):
                    self.piles[p2].add_bottom(self.piles[p1].remove_top())
            elif (self.piles[p2].size() == 0 or # Main pile - > Sub pile
                  self.piles[p2].peek_bottom().get_type() == self.piles[p1].peek_top().get_type() + 1 and
                    self.piles[p2].peek_bottom().get_colour() != self.piles[p1].peek_top().get_colour()):
                    self.piles[p2].add_bottom(self.piles[p1].remove_top())
        elif p1 > 0 and p2 > 0:
            if p2 > self.suits * 2 - 1: #Sub pile -> Ace pile
                if (self.piles[p2].peek_bottom().get_type() == self.piles[p1].peek_top().get_type() - 1 and
                    self.piles[p2].peek_bottom().get_suit() == self.piles[p1].peek_top().get_suit()):
                    self.piles[p1].add_bottom(self.piles[p2].remove_bottom())
                elif (self.piles[p1].size() > 0 and self.piles[p2].size() > 0 and # Sub pile -> Sub pile
                    self.piles[p2].peek_bottom().get_type() == self.piles[p1].peek_top().get_type() + 1 and
                    self.piles[p2].peek_bottom().get_colour() != self.piles[p1].peek_top().get_colour()):
                    while self.piles[p1].size() > 0:
                        self.piles[p2].add_bottom(self.piles[p1].remove_top())
        else:
            pass

    def is_complete(self):
        if self.piles[0].size() == 0:
            return True
        return False

    def play(self):
        print("********************** NEW GAME *****************************\n")
        move_number = 1
        while move_number <= self.max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            while True:
                try:
                    pile1 = int(input("Move from pile no.: "))
                except ValueError:
                    pile1 = int(input(f"Please enter a value from 0 to {self.num_piles - 1}!\n Move from pile no.: "))
                else:
                    break
            print("Round", move_number, "out of", self.max_num_moves, end = ": ")
            while True:
                try:
                    pile2 = int(input("Move to pile no.: "))
                except ValueError:
                    pile1 = int(input(f"Please enter a value from 0 to {self.num_piles - 1}!\n Move from pile no.: "))
                else:
                    break
            if pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles and pile2 < self.num_piles:
                self.move(pile1, pile2)
            move_number += 1
            print()
        if self.is_complete():
            print("You won in", move_number - 1, "steps!\n")
            play_banner()
        else:
            print("You Lose!\n")

class CardPile:
    def __init__(self):
        self.items = []

    def add_top(self, item):
        self.items.insert(0, item)

    def add_bottom(self, item):
        self.items.append(item)

    def remove_top(self):
        try:
            return self.items.pop(0)
        except IndexError:
            pass

    def remove_bottom(self):
        try:
            return self.items.pop()
        except IndexError:
            pass

    def size(self):
            return len(self.items)
    
    def peek_top(self):
        try:
            return self.items[0]
        except IndexError:
            pass
    
    def peek_bottom(self):
        try:
            return self.items[-1]
        except IndexError:
            pass
    
    def print_all(self, index=0):
        self.index = index
        if self.index == 0 and self.size() > 0:
            print(f"{self.items[0]}{' *' * (self.size() - 1)}")
        else:
            print(' '.join([str(i) for i in self.items]))