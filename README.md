# Python OOP Blackjack

A completely functional, command-line Blackjack game built to demonstrate Object-Oriented Programming (OOP) principles in Python.

## Description
This project simulates a classic casino Blackjack experience. The player starts with a bankroll, places bets, and plays against a computer dealer. The game handles deck shuffling, card dealing, score calculation (including dynamic Ace values), and win/loss betting conditions. 

## Features
* **Full Betting System:** Start with $100, place custom bets, and track your bankroll across multiple hands.
* **Smart Dealer Logic:** The dealer automatically plays according to standard casino rules (hits until 17 or higher).
* **Dynamic Aces:** Aces automatically adjust their value from 11 to 1 to prevent busting.
* **Input Validation:** Built-in error handling prevents the game from crashing if a player enters invalid bets or commands.

## Object-Oriented Architecture
The game is built using modular, encapsulated Python classes (leveraging `@dataclass`):
* `Card`: Represents a single playing card with a suit, rank, and visual representation.
* `Deck`: Builds, stores, and shuffles the 52-card deck, handling the `deal_card()` logic.
* `Hand`: Manages the cards currently held by a player/dealer, calculating the live score and tracking Aces.
* `Chips`: Manages the player's betting bankroll and state across multiple rounds.

## Prerequisites
* Python 3.7 or higher (required for `dataclasses`).

## How to Play
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the main game file:
   ```bash
   python game.py