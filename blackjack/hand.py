from dataclasses import dataclass, field

from card import Card, value


@dataclass
class Hand:
    cards: list = field(default_factory=list)
    score: int = 0
    aces: int = 0

    def add_card(self, new_card:Card):
        self.cards.append(new_card)
        self.score += value[new_card.rank]
        if new_card.rank == "Ace":
            self.aces += 1
        return self.aces

    def ace_adjust(self):
        while self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1

        



