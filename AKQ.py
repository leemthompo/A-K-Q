#!/usr/bin/env python3
import random
import time
import os

# AKQ Game

deck = [0, 1, 2]

computer_score = 0
your_score = 0

# BIG CARDS
QUEEN = """
 ┌─────────┐
 │ Q       │
 │         │
 │         │
 │    Q    │
 │         │
 │         │
 │        Q│
 └─────────┘"""


KING = """
 ┌─────────┐
 │ K       │
 │         │
 │         │
 │    K    │
 │         │
 │         │
 │        K│
 └─────────┘"""

ACE = """
 ┌─────────┐
 │ A       │
 │         │
 │         │
 │    A    │
 │         │
 │         │
 │        A│
 └─────────┘"""

# TODO betting logic


def ante():
    """Take one chip from each players chipstack as the ante"""
    pass


def button_or_blind():
    """Determines which player is on button and which is on blind.
    The opening positions are determined by a coin-toss.
    If the human wins the cointoss they go on button for first round."""
    toss = random.randint(0, 1)
    decision = input("Heads or Tails? (Respond H or T)")

    print("You picked", decision)
    print("Flipping coin...")
    time.sleep(2)

    if toss == 0:
        print("Heads")
        if decision.upper() == "H":
            print("You won the cointoss. You are on the button in the first round")
            button = 0
            blind = 1
        else:
            print("You lost the cointoss. You are the blind in the first round")
            button = 1
            blind = 0
    else:
        print("Tails")
        if decision.upper() == "T":
            print("You won the cointoss. You are on the button in the first round")
            button = 0
            blind = 1
        else:
            print("You lost the cointoss. You are the blind in the first round")
            button = 1
            blind = 0

    return button, blind


def deal(deck):
    """Deal the cards from the shuffled 3-card deck
    and return each players hand."""

    computer_hand = 0
    your_hand = 0

    shuffled_deck = random.sample(deck, len(deck))
    blind_card = shuffled_deck[0]
    button_card = shuffled_deck[1]

    computer_hand += int(blind_card)
    your_hand += int(button_card)

    return computer_hand, your_hand

# TODO break down into logical functions and abstract certain logic aspects


def play(deck):
    global computer_score
    global your_score
    global QUEEN
    global KING
    global ACE
    global your_hand
    global computer_hand

    print("You are on the button")
    print("\n")
    time.sleep(1)

    print("--------")
    print("New Hand")
    print("--------")
    print("\n")


def show_card(your_hand):
    """Print the hand to the console."""
    print("\n" * 40)
    if your_hand == 0:
        print("Your card: ", QUEEN)
    elif your_hand == 1:
        print("Your card: ", KING)
    else:
        print("Your card: ", ACE)
    time.sleep(2)

# TODO Here you need to break out your_move into a separate function
# and return that move to be assessed in showdown logic


def blind_moves(computer_hand, your_hand):
    """Move for computer on the blind."""

    global computer_score
    global your_score

    computer_move = 0
    # your_move = 0

    if computer_hand == 0:
        i = random.randint(1, 3)  # Randomize bluffing with Q 1/3 of the time
        if i == 3:
            computer_move += 2
        else:
            pass
    elif computer_hand == 1:
        computer_move += 1
    else:
        computer_move += 2

    # Prompts for human player following computer move
    if computer_move == 0:
        print("Computer checks. Let's see them cards!")
        print("\n")
        if computer_hand > your_hand:
            computer_score += 1
            print("You lose this hand :(")
            print("\n")
        else:
            your_score += 1
            print("You win this hand!")
            print("\n")
    elif computer_move == 1:
        print("Computer checks. Let's see them cards!")
        print("\n")
        time.sleep(2)
        if computer_hand > your_hand:
            computer_score += 1
            print("You lose this hand :(")
            print("\n")
        else:
            your_score += 1
            print("You win this hand")
            print("\n")
    else:
        print("Computer raises. Call or fold?")
        print("\n")
        decision = input("Call or fold: ")
        print("\n")
        time.sleep(1)

        ## Showdown logic
        if decision.upper() == ("CALL") and your_hand > computer_hand:
            your_score += 1
            print("Computer has a Queen. You win this hand!")
            print("\n")
        elif decision.upper() == ("CALL") and your_hand < computer_hand:
            if computer_hand == 1:
                computer_score += 1
                print("Computer has a King. You lost this hand")
                print("\n")
            else:
                computer_score += 1
                print("Computer has the Ace. You lost this hand.")
                print("\n")
        else:
            computer_score += 1
            print("You fold")
            print("\n")


while your_score < 5 and computer_score < 5:
    play(deck)
    medeal = deal(deck)
    computer_hand = (medeal[0])
    your_hand = (medeal[1])
    show_card(your_hand)
    blind_moves(computer_hand, your_hand)

    print("-------------------")
    print("Your score: ", your_score)
    print("Computer score: ", computer_score)
    print("-------------------")
    time.sleep(2)
    print("\n")

else:
    if computer_score == 5:
        os.system("cowsay COMPUTER WINS!")
    else:
        os.system("cowsay YOU WIN!")
