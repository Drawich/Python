import random
import sys
import os


# Utility functions
def is_running_in_terminal():
    """Check if the script is running in a terminal."""
    return sys.stdin.isatty()


def clear():
    """Clears the screen if running in a terminal; otherwise, inserts default number of new lines."""
    windows_clear_command = 'cls'
    unix_clear_command = 'clear'

    if is_running_in_terminal():
        if os.name == 'nt':  # For Windows
            _ = os.system(windows_clear_command)
        else:  # For Unix/Linux/Mac
            _ = os.system(unix_clear_command)
    else:
        print('\n' * 50)


def is_valid_yes_no(x):
    """Validate yes/no input."""
    return x.lower() in ['yes', 'y', 'no', 'n']


def get_yes_no_input(question):
    """Prompt user for yes/no input."""
    while True:
        response = input(question).strip().lower()
        if not is_valid_yes_no(response):
            print('Invalid input. Please enter "yes" or "no".')
        else:
            return response


# Card dealing functions
def initialize_cards():
    """Initialize dealer and user cards."""
    return [], []


def deal_cards(number_of_cards):
    """Deal a specific number of cards."""
    cards = []
    for _ in range(number_of_cards):
        cards.append(new_card())
    return cards


def new_card():
    """Generate a new card."""
    top_cards = ['Knight', 'King', 'Queen']
    new_card = random.randint(1, 11)
    if new_card == 1:
        return 'Ace'
    elif new_card == 11:
        return random.choice(top_cards)
    else:
        return new_card


# Game logic functions
def initial_deal(dealer_cards, user_cards):
    """Deal initial cards to dealer and user."""
    dealer_cards.extend(deal_cards(2))
    user_cards.extend(deal_cards(2))


def user_turn(user_cards):
    """Handle user's turn."""
    another_card = get_yes_no_input('Do you want another card? (yes/no) \n')
    if another_card in ('yes', 'y'):
        user_cards.extend(deal_cards(1))
        print(f'You got a {user_cards[-1]}')
        input('Press enter to continue...')
        clear()
        return user_cards, True
    else:
        clear()
        return user_cards, False


def dealer_turn(dealer_cards):
    """Handle dealer's turn."""
    if calculate_total_score(dealer_cards) <= 16:
        dealer_cards.extend(deal_cards(1))
    return dealer_cards


def taking_turns(user_cards, dealer_cards):
    """Handle turns for user and dealer."""
    user_cards, draw_new_card = user_turn(user_cards)
    if not draw_new_card:
        return user_cards, draw_new_card, dealer_cards
    dealer_cards = dealer_turn(dealer_cards)
    return user_cards, draw_new_card, dealer_cards

# Scores and winners
def calculate_total_score(cards):
    """Calculate total score of cards."""
    sum_cards = 0
    ace_count = 0
    for card in cards:
        value = calculate_card_value(card)
        sum_cards += value
        if card == 'Ace':
            ace_count += 1
    if ace_count > 0:
        sum_cards = handle_aces(sum_cards, ace_count)
    return sum_cards


def calculate_card_value(card):
    """Calculate value of individual card."""
    if card in ('Knight', 'King', 'Queen'):
        return int(10)
    elif card == 'Ace':
        return int(1)
    else:
        return int(card)


def handle_aces(score, ace_count):
    """Handle Aces in card calculation."""
    for _ in range(ace_count):
        if score + 10 <= 21:
            score += 10
    return score


def check_blackjack(dealer_cards, user_cards):
    """Check for Blackjack."""
    if is_blackjack(dealer_cards):
        return 'dealer'
    elif is_blackjack(user_cards):
        return 'user'
    return False


def is_blackjack(cards):
    """Check if a hand is Blackjack."""
    return len(cards) == 2 and 'Ace' in cards and any(card in ['10', 10, 'Knight', 'King', 'Queen'] for card in cards)


def winner(dealer_sum, user_sum):
    """Determine winner based on scores."""
    if user_sum > 21:
        return False  # User busts, dealer wins
    elif dealer_sum > 21:
        return True  # Dealer busts, user wins
    elif user_sum == dealer_sum:
        return "draw"
    elif user_sum > dealer_sum:
        return True
    else:
        return False


# Display functions
def display_current_cards_user(cards):
    """Display user's cards."""
    formatted_cards = ', '.join(map(str, cards[:-1])) + f' and {cards[-1]}' if len(cards) > 1 else str(cards[0])
    return f'Your cards: {formatted_cards}'


def display_current_cards_dealer(cards, reveal_all=False):
    """Display the dealer's cards with the option to reveal all or keep the first card hidden"""
    if reveal_all:
        formatted_cards = ', '.join(map(str, cards[:-1])) + f' and {cards[-1]}'
    else:
        if len(cards) == 2:
            formatted_cards = f"Hidden and {cards[1]}"
        else:
            formatted_cards = 'Hidden, ' + ', '.join(map(str, cards[1:-1])) + f' and {cards[-1]}'
    return f"Dealer's cards: {formatted_cards}"


def display_sum_final_hands(user_cards, dealer_cards):
    """Display final hands."""
    final_sum_user = calculate_total_score(user_cards)
    final_sum_dealer = calculate_total_score(dealer_cards)
    print(f"Sum of your final hand: {final_sum_user}")
    print(f"Sum of dealer's final hand: {final_sum_dealer}")


# Game control functions
def start_game():
    """Starts the Blackjack game."""
    while True:
        dealer_cards, user_cards = initialize_cards()
        initial_deal(dealer_cards, user_cards)

        print(display_current_cards_dealer(dealer_cards))
        print(display_current_cards_user(user_cards))

        the_blackjack_winner = check_blackjack(dealer_cards, user_cards)
        if the_blackjack_winner:
            is_blackjack(the_blackjack_winner)
            break

        while True:
            user_cards, draw_new_card, dealer_cards = taking_turns(user_cards, dealer_cards)

            if draw_new_card is False:  # User chose not to take another card
                break

            user_sum = calculate_total_score(user_cards)
            if user_sum > 21:
                print('You bust!')
                break
            else:
                print(display_current_cards_dealer(dealer_cards))
                print(display_current_cards_user(user_cards))

        if user_cards:
            dealer_cards = dealer_turn(dealer_cards)

        if user_cards is not False:
            game_winner = winner(calculate_total_score(dealer_cards), calculate_total_score(user_cards))
            if game_winner == "draw":
                print("It's a draw!")
            elif game_winner:
                print("Congratulations! You win!")
            else:
                print("Dealer wins!\n")
            print(display_current_cards_dealer(dealer_cards, reveal_all=True))
            display_sum_final_hands(user_cards, dealer_cards)

        again = get_yes_no_input('\nDo you want to play another game of Blackjack? (yes/no) \n')
        clear()
        if again in ('no', 'n'):
            print('Exiting game...')
            return False


def main():
    """Main entry point of the program."""
    while True:
        if not start_game():
            break
    print("Thank you for playing! Goodbye")


if __name__ == "__main__":
    main()
