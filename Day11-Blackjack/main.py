#Blackjack
import os
import random as ran
from art import logo

def keep_playing_blackjack():
    keep_playing = False
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if response == 'y':
        keep_playing = True
    return keep_playing

def game_setup():
    os.system('clear')
    print(logo)

def deal_cards(cards, player_cards):
    for index in range(0, 2):
        player_cards.append(ran.choice(cards))
    return sum(player_cards)

def has_blackjack(score):
    return score == 21

def is_over_21(score, hand):
    if score > 21:
        # hand is modified because it's passed as a reference to has_ace
        # and as a mutable list is changed outside the function as well
        if has_ace(hand):   # changes each occurrence of 11 to 1 upon call to has_ace
            score -= 10
            return is_over_21(score, hand)
    return score

def has_ace(hand):
    ace = False
    for card in range(len(hand)):
        if hand[card] == 11:
            hand[card] = 1
            ace = True
            break
    return ace

def deal_single_card(cards, player_cards):
    player_cards.append(ran.choice(cards))
    return sum(player_cards)

def print_score(user_score, user_cards, computer_score, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
def play_game():
    # Initialize deck, user and computer hand
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []

    # Clear screen and print logo
    game_setup()

    # Deal user and computer cards and add them up
    user_score = deal_cards(cards, user_cards)
    computer_score = deal_cards(cards, computer_cards)

    # First check for Blackjack
    if has_blackjack(user_score) and has_blackjack(computer_score):
        print("It's a draw. You both have blackjacks.")
        print_score(user_score, user_cards, computer_score, computer_cards)
        return keep_playing_blackjack()
    elif has_blackjack(user_score):
        print("You have a blackjack. You win!")
        print_score(user_score, user_cards, computer_score, computer_cards)
        return keep_playing_blackjack()
    elif has_blackjack(computer_score):
        print("Computer has a blackjack. You lose.")
        print_score(user_score, user_cards, computer_score, computer_cards)
        return keep_playing_blackjack()
    else:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

    # Next check if anyone is over 21
    draw_again = True
    while draw_again:
        if user_score > 21 and computer_score > 21:
            print("You both lose.")
            print_score(user_score, user_cards, computer_score, computer_cards)
            return keep_playing_blackjack()
        elif user_score > 21:
            print("Bust. You lose.")
            print_score(user_score, user_cards, computer_score, computer_cards)
            return keep_playing_blackjack()
        elif computer_score > 21:
            print("Computer bust. You win!")
            print_score(user_score, user_cards, computer_score, computer_cards)
            return keep_playing_blackjack()
        else:   # neither is over 21
            # Ask if user wants to draw again. Automate computer behavior.
            if computer_score < 17:
                computer_score = deal_single_card(cards, computer_cards)
                computer_score = is_over_21(computer_score, computer_cards)
            if input("Type 'y' to get another card. Type 'n' to pass: ").lower() == 'y':
                user_score = deal_single_card(cards, user_cards)
                user_score = is_over_21(user_score, user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
            else:
                draw_again = False

    # Calculate winner
    print_score(user_score, user_cards, computer_score, computer_cards)
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        if is_over_21(computer_score, computer_cards):
            print("Computer bust. You win!")
        else:
            print("You lose.")
    else:
        print("It's a draw.")

    # Ask if user wants to play again
    return keep_playing_blackjack()
        
# Main
in_game = False
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    in_game = True
    
while in_game:
    in_game = play_game()


                

