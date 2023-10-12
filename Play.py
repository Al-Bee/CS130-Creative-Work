from Solitaire import Solitaire
from Card import CardDeck

def main():
    print('Welcome to Solitaire!\n')
    suits = input('Would you like to play with 2 suits or 4?: ')
    while suits not in ['2', '4']:
        suits = input('Please enter 2 or 4: ')
    game = Solitaire(CardDeck(int(suits)).deck).play()

main()