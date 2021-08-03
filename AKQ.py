#!/usr/bin/env python3
import random
import time
import os

# AKQ Game

deck = [0, 1, 2]

computer_score = 0
your_score = 0

# Initial player on button determined by `button_or_blind()`
# After each rounds the button and blinds alternate
# 0 = Human, 1 = Computer


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
    print("Welcome to AKQ, a simple poker game by Liam Thompson.")
    print("\n")
    print("It's you versus the computer where each player gets one card from the 3-card deck.")
    time.sleep(2)
    print("\n" * 3)
    print("We start by flipping a coin to see who is on the button first.")
    print("\n" * 2)
    decision = input("Heads or Tails? (Respond H or T): ")
    print("\n")

    print("Flipping coin...")
    print("\n")
    time.sleep(2)

    if toss == 0:
        print("Heads")
        print("\n")
        if decision.upper() == "H":
            print("You won the cointoss. You are on the button in the first round.")

            print("\n")
            time.sleep(2)
            button = 0
            blind = 1
        else:
            print("\n")
            print("You lost the cointoss. You are the blind in the first round.")
            print("\n")
            time.sleep(2)
            button = 1
            blind = 0
    else:
        print("\n")
        print("Tails")
        print("\n")
        if decision.upper() == "T":
            print("You won the cointoss. You are on the button in the first round.")
            time.sleep(2)
            button = 0
            blind = 1
        else:
            print("\n")
            print("You lost the cointoss. You are the blind in the first round.")
            time.sleep(2)
            button = 1
            blind = 0

    return button, blind


def deal(deck):
    """Deal the cards from the shuffled 3-card deck
    and return each players hand."""

    shuffled_deck = random.sample(deck, len(deck))

    if button == 0:
        your_hand = shuffled_deck[0]
        computer_hand = shuffled_deck[1]
    elif button == 1:
        your_hand = shuffled_deck[1]
        computer_hand = shuffled_deck[0]

    return computer_hand, your_hand



def show_card(your_hand):
    """Print the hand to the console."""
    print("\n" * 20)
    if button == 0:
        print("You are on the button.")
    else:
        print("You are on the blind.")
    print("\n")
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
        decision = input("Call (1 chip) or fold: ")
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


def button_moves(computer_hand, your_hand):
    """Move for computer on the button. Prompts for human."""

    global your_score
    global computer_score

    your_move = 0
    computer_move = 0

    decision = input("Check or [r]aise?: ")
    if decision.upper() == "R" or "RAISE":
        your_move += 1
    else:
        your_move = 0

    # Prompts for human player
    if your_move == 0:
        print("You check. Let's see them cards!")
        print("\n")
    else:
        print("You raised.")
        print("\n")
        time.sleep(2)
        if computer_hand == 0:
            print("Computer folds")
            print("You win this hand!")
            print("\n")
        elif computer_hand == 1:
            i = random.randint(1, 3)  # Randomize calling with K 1/3 of the time
            if i == 3:
                computer_move += 1
            else:
                print("Computer folds")
                print("You win this hand!")
                print("\n")
                computer_move = 0
        elif computer_hand == 2:
            print("Computer calls. Computer has Ace!")
            print("\n")

            computer_move += 1
        # Showdown logic
        if computer_hand > your_hand and computer_move == 1:
            computer_score += 1
            if computer_hand == 2:
                print("Computer has Ace. You lost this hand.")
            else:
                print("Computer has King. You lost this hand.")
        else:
            your_score += 1


print("\n" * 10)
print("""       d8888 888    d8P   .d88888b.
      d88888 888   d8P   d88P" "Y88b
     d88P888 888  d8P    888     888
    d88P 888 888d88K     888     888
   d88P  888 8888888b    888     888
  d88P   888 888  Y88b   888 Y8b 888
 d8888888888 888   Y88b  Y88b.Y8b88P
d88P     888 888    Y88b  "Y888888"
                                Y8b


      """)

time.sleep(3)

button, blind = button_or_blind()  # Cointoss to determine button

if __name__ == "__main__":
    while your_score < 5 and computer_score < 5:  # Main game loop

        computer_hand, your_hand = deal(deck)
        show_card(your_hand)

        if button == 0:
            print("You are on the button. Computer acts first.")
            blind_moves(computer_hand, your_hand)
        else:
            print("You are on the blind. You act first.")
            button_moves(computer_hand, your_hand)

        print("-------------------")
        print("Your score: ", your_score)
        print("Computer score: ", computer_score)
        print("-------------------")
        time.sleep(2)
        print("\n")
        print("--------")
        print("New Hand")
        print("--------")
        button, blind = blind, button  # Flip the button and blinds to alternate

    else:
        if computer_score == 5:
            os.system("cowsay COMPUTER WINS!")
            os.system("say computer wins")
        else:
            os.system("cowsay YOU WIN!")
            os.system("say you win")
