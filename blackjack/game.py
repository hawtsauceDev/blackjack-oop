from card import Card
from chips import Chips
from deck import Deck
from hand import Hand


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

player_chips = Chips()

while True:
    deck: Deck = Deck()
    deck.shuffle_deck()
    player_hand = Hand()
    dealer_hand = Hand()

    place_bet(player_chips)

    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    print("--- Player hand ---")
    for card in player_hand.cards:
        card:Card
        print(card.see_card())

    print(f"Player score: {player_hand.score}")
    if player_hand.score == 21:
        print("--- Blackjack!! ---")
        player_is_playing = False
    else:
        player_is_playing = True

    print(f"--- Dealer hand --- \n{dealer_hand.cards[0].see_card()}")

    while player_is_playing:
        player_is_playing = hit_or_stand(deck, player_hand)

        print("--- Player hand ---")
        for card in player_hand.cards:
            card:Card
            print(card.see_card())

        if player_hand.score > 21:
            print("--- Player busts ---")
            player_chips.lose_bet()
            print(f"--- Player chips: ${player_chips.total} ---")
            break

        if player_hand.score == 21:
            print("--- Auto Stand ---")
            break

    if player_hand.score <= 21:
        while dealer_hand.score < 17:
            dealer_hand.add_card(deck.deal_card())

        print("--- Dealer hand ---")
        for card in dealer_hand.cards:
            card:Card
            print(card.see_card())

        print(f"--- Dealer score: {dealer_hand.score} ---")

        if dealer_hand.score > 21:
            print("--- Dealer Busts! ---")
            player_chips.win_bet()
            print(f"--- Player chips: ${player_chips.total} ---")
        elif dealer_hand.score > player_hand.score:
            print("--- Dealer wins! ---")
            player_chips.lose_bet()
            print(f"--- Player chips: ${player_chips.total} ---")
        elif dealer_hand.score < player_hand.score:
            print("--- Player wins! ---")
            player_chips.win_bet()
            print(f"--- Player chips: ${player_chips.total} ---")
        else:
            print("Its a tie/push...")

    # print(f"--- Player Chips: {player_chips.total} ---")
    new_game = input("Play again: y/n: ")
    if new_game == "y":
        continue
    elif new_game == "n":
        print("--- Thanks for playing... ---")
        break

