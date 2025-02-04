#Blackjack
import os
import random as ran
from art import logo

def is_playing_blackjack():
    keep_playing = False
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if response == 'y' or response == 'yes':
        keep_playing = True
    return keep_playing

def game_setup():
    os.system('cls')
    print(logo)

# def draw_cards(player_cards):
#     for index in range(0, 2):
#         player_cards.append(deal_card())

def deal_cards(player_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for index in range(0, 2):
        player_cards.append(ran.choice(cards))
    # first_card = ran.choice(cards)
    # second_card = ran.choice(cards)
    # return first_card + second_card
    ran_card = ran.choice(cards)
    return ran_card

def has_blackjack(score):
    return score == 21

def is_over_21(score, hand):
    bust = False
    if score > 21:
        # hand is modified because it's passed as a reference to has_ace
        # and as a mutable list is changed outside the function as well
        if has_ace(hand):   # changes each occurrence of 11 to 1 upon call to has_ace
            is_over_21(score, hand)
        else:
            bust = True
    return bust

def has_ace(hand):
    ace = False
    for card in range(len(hand)):
        if hand[card] == 11:
            hand[card] = 1
            ace = True
            break
    return ace



# Main
in_game = True
user_cards = []
computer_cards = []
while in_game:
    if not is_playing_blackjack():
        in_game = False
        print("Exiting game")
    else:
        game_setup()
        draw_cards(user_cards)
        draw_cards(computer_cards)
        user_score = user_cards[0] + user_cards[1]
        print(user_score)
        computer_score = computer_cards[0] + computer_cards[1]
        print(computer_score)
        if has_blackjack(user_score) and has_blackjack(computer_score):
            print("It's a draw.")
        elif has_blackjack(user_score):
            print("You win!")
        elif has_blackjack(computer_score):
            print("You lose.")
        else:
            if is_over_21(user_score, user_cards) and is_over_21(computer_score, computer_cards):
                print("You both lose.")
                in_game = False
                print("Exiting game")
            elif is_over_21(user_score, user_cards):
                print("Bust. You lose.")
                in_game = False
                print("Exiting game")
            elif is_over_21(computer_score, computer_cards):
                print("Computer bust. You win!")
                in_game = False
                print("Exiting game")
            else:   # Neither is over 21
                # Ask if user wants to draw again. Automate computer behavior.
                print(f"Computer's first card: {computer_cards[0]}")


