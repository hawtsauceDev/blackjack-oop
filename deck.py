import random

from card import Card, rank, suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for s in suit:
            for r in rank:
                new_card = Card(suit=s, rank=r)
                self.all_cards.append(new_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()


