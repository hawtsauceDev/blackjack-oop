import os
import subprocess

from chips import Chips
from deck import Deck
from hand import Hand


def clear_screen():
    # subprocess.run is the modern standard for executing terminal commands
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True, check=False)


def place_bet(bank: Chips):

    while True:
        print(f"You currently have: ${bank.total}")
        try:
            bet = int(input("How much do you want to bet?: $"))
            if bet > bank.total:
                print("You don't have that much to bet...")
                continue
            else:
                bank.bet = bet
                break
        except ValueError:
            print("Value must be a number.")


def hit_or_stand(deck: Deck, hand: Hand):
    while True:
        choice = input("Hit or Stand. Enter 'h' or 's': ").lower()
        if choice == "h":
            hand.add_card(deck.deal_card())
            print("You hit!")
            return True
        elif choice == "s":
            print("You stand, Dealer's turn")
            return False
        else:
            print("Sorry, please try again.")