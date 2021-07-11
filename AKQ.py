#!/usr/bin/env python3
import random
import time
import os

# AKQ Game

deck = [0, 1, 2]

computer_score = 0
your_score = 0

# BIG CARDS
big_queen = """
 ┌─────────┐
 │ Q       │
 │         │
 │         │
 │    Q    │
 │         │
 │         │
 │        Q│
 └─────────┘"""


big_king = """
 ┌─────────┐
 │ K       │
 │         │
 │         │
 │    K    │
 │         │
 │         │
 │        K│
 └─────────┘"""

big_ace = """
 ┌─────────┐
 │ A       │
 │         │
 │         │
 │    A    │
 │         │
 │         │
 │        A│
 └─────────┘"""

## TODO betting logic

def bet():
  pass


## TODO break down into logical functions and abstract certain logic aspects
def play(deck):
    "Deal the cards from the shuffled 3-card deck"
    global computer_score
    global your_score
    global big_queen
    global big_king
    global big_ace
    
    computer_hand = 0
    your_hand = 0

    computer_move = 0
    your_move = 0

    shuffled_deck = random.sample(deck, len(deck))
    first_card = shuffled_deck[0]
    second_card = shuffled_deck[1]

    computer_hand += int(first_card)
    your_hand += int(second_card)

    print("You are on the button")
    print("\n")
    time.sleep(1)

    print("--------")
    print("New Hand")
    print("--------")
    print("\n")
    
    # Show hand
    if your_hand == 0:
        print("Your card: ", big_queen)
    elif your_hand == 1:
        print("Your card: ", big_king)
    else:
        print("Your card: ", big_ace)
    time.sleep(2)

    # Moves for computer on the blind 
    if computer_hand == 0:
        i = random.randint(1, 3) # Randomize bluffing with queens 1/3 of the time 
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
