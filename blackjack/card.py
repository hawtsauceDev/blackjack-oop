from dataclasses import dataclass

suit = ("Hearts", "Diamonds", "Spades", "Clubs")
rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace":11
}


@dataclass
class Card:
    suit: str
    rank: str

    def see_card(self):
        return f"{self.rank} of {self.suit}"
