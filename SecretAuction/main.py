import info
import sys
import os


# To clear screen
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


# Validates responses
def validate_input(question, validation, error_message):
    """Prompts user for input and validates it against a validation function or list of valid values."""
    while True:
        response = input(f'{question} \n')
        if callable(validation):
            if validation(response):
                return response
            else:
                print(error_message)
        elif response in validation:
            return response
        else:
            print(error_message)


def is_valid_name(x):
    """Validate name input: must be alphabetical and non-empty."""
    return all(char.isalpha() or char.isspace() for char in x) and x.strip() != ""


def is_valid_bid(x):
    """Validate bid input: must be numeric or start with '$' followed by floating digits."""
    x = x.replace(',', '').strip()
    x = x.replace('$', '').strip()
    if x.isdigit():
        return round(float(x), 2)
    if x.startswith('$') and all(char.isalpha() or char.isspace() for char in x[1:]):
        x = x[1:]
        return round(float(x), 2)
    if '.' in x:
        parts = x.split('.')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return round(float(x), 2)  # Convert to float and round to 2 decimal places
    return False


def is_valid_yes_no(x):
    """Validate more bidders input: must be 'yes', 'no', 'y', or 'n'."""
    return x.lower() in ['yes', 'y', 'no', 'n']


# Arrange list
def prepare_and_validate_auction_list(items):
    """Processes and validates the list of items for auction."""
    if items == 'test':
        return 'test'
    elif ',' in items:
        items_list = [item.strip().lower() for part in items.split(',') for item in part.split()]
        return items_list
    elif items.strip() != "" and items.isalnum() and any(char.isalpha() for char in items):
        items_list = [items.strip().lower()]
        return items_list
    else:
        return False


# Get input from user
def get_auction_list():
    """Gets all the items for the auction."""
    return validate_input(
        'Please add all the items separated with a comma or type "test": \n',
        prepare_and_validate_auction_list,
        'Invalid entry.'
    )


def get_name():
    """Gets bidder's name."""
    return validate_input("What is your name? If no one wants to bid, please write 'None'.",
                          is_valid_name,
                          'Invalid name. Please enter a valid name consisting of alphabetical characters.')


def get_bid():
    """Gets bidder's bid."""
    bid = validate_input('What is your bid?',
                          is_valid_bid,
                          'Invalid bid format. Please enter a bid as a number, optionally starting with "$".')
    formatted_bid = bid.replace(',', '').replace('$', '').strip()
    done_bid = float(formatted_bid)
    return (float(done_bid))


def get_more_bidders():
    """Asks if there are more bidders."""
    return validate_input('Are there any other bidders? (yes/no)',
                          is_valid_yes_no,
                          'Invalid input. Please enter "yes" or "no".').lower()


def restart(width):
    """Asks if user wants to restart."""
    prompt = 'Do you want to start another auction? (yes/no)'
    validation = is_valid_yes_no
    error_message = 'Invalid input. Please enter "yes" or "no".'
    return validate_input(align_text(prompt, 'center', width),
                          validation,
                          error_message.lower().strip())

# Calculate bidders
def max_bidder(bidders):
    """Determines the highest bidder."""
    if not bidders:
        return None, None

    highest_value = 0.00
    name_of_bidder = ""
    for name, bid in bidders.items():
        formatted_bid = "{:.2f}".format(float(bid))
        if float(formatted_bid) > float(highest_value):
            highest_value = formatted_bid
            name_of_bidder = name
    return highest_value, name_of_bidder


# Handle formatting of text
def linebreak_at_char(text, break_at_character, characters_per_line):
    """Inserts line breaks in text after characters_per_line characters from the last occurrence of break_at_character."""
    lines = []
    current_line = []
    current_length = 0

    for char in text:
        if char == break_at_character and current_length >= characters_per_line:
            lines.append(''.join(current_line))
            current_line = [char]
            current_length = 1
        else:
            current_line.append(char)
            current_length += 1

    lines.append(''.join(current_line))
    return '\n'.join(lines)


def align_text(text, align, width):
    if align == 'center':
        centered_text = linebreak_at_char(text, ' ', width)
        return centered_text.center(width)
    elif align == 'list_left_aligned':
        max_offset = width//4
        whole_list = []
        for item in text:
            parts = item.split(maxsplit=1)
            if len(parts) >= 2:
                first_word, remainder = parts
            else:
                first_word, remainder = parts[0], ''

            offset = max_offset - len(first_word)
            aligned_line = f'{' ' * (width//6 + (width//8))} {first_word.ljust(len(first_word) + offset)} {remainder}'
            whole_list.append(aligned_line)

        return '\n'.join(whole_list)


# Introduction
def intro(objects_for_auction, full_width):
    """Introduction to the auction"""
    print(art.logo)
    print(align_text(art.intro.format(num_items=len(objects_for_auction)), 'center', full_width))
    print()
    item_text = align_text(objects_for_auction, 'list_left_aligned', full_width)
    print(f'\n {item_text} \n')
    print('Press enter to get started!\n'.center(full_width))
    input('')


def auction_item_intro(item, number, number_of_items, width):
    """Informs user of what item they are bidding on"""
    intro_text = f"For item number {number} out of {number_of_items} items, we are conducting an auction for a/an {item}. " \
                 "If you would like to place a bid on this item, please fill out the questions below: \n"
    print(art.logo)
    print(align_text(intro_text, 'center', width))


# Outro
def print_winners(sold_items, width):
    """Gives a list of all the winners of today, only displays sold items"""
    print(align_text('Congratulations to all our winners!\n','center', width))
    for key, list_of_value in sold_items.items():
        for value in list_of_value:
            name = value[0]
            bid = value[1]
        print(align_text(f'{name.title()} won a/an {key} for ${bid}.', 'center', width))
    print(align_text('Thank you for joining us today!\n', 'center', width))


def auction_item(item, number_of_items, number, width):
    """Runs the auction program for each item and sends back the winning bid."""
    bidders = {}
    while True:
        auction_item_intro(item, number, number_of_items, width)
        name = get_name()
        if name.lower() == 'none' and len(bidders) == 0:
            return 'not sold'
        elif name.lower() == 'none':
            break
        else:
            bid = get_bid()
            formatted_bid = float("{:.2f}".format(bid))
            bidders[name] = formatted_bid
            more_bidders = get_more_bidders()
        if more_bidders.lower() in ['no', 'n']:
            break
        clear()
    max_bid, name_of_max_bidder = max_bidder(bidders)
    clear()
    print(align_text(f'Highest bid was ${max_bid} by {name_of_max_bidder.title()}\n','center', width))
    print(align_text(f'Congratulations, {name_of_max_bidder.title()}!','center', width))
    sold_item = [name_of_max_bidder, max_bid]
    if number == number_of_items:
        print(align_text('Press enter to end auction.', 'center', width))
        input('')
        clear()
        return sold_item
    else:
        print(align_text('Press enter for the next item.\n', 'center', width))
        input('')
        clear()
        return sold_item


def auction_program(width):
    """Will manage each auction with a list of items"""
    print("We're about to start the auction. Let's set up all the items you're selling today!")
    items_input = get_auction_list()  # sets up the list of item being sold
    if items_input.lower().strip() == 'test':  # Uses a pre-made list for 7 items
        objects_for_auction = list(art.objects_for_auction)
    else:
        objects_for_auction = items_input.split(',').strip().lower()
    clear()  # will remove the previous text prior to the start of the auction

    iteration = 1
    sold_items = {}
    number_of_items = len(objects_for_auction)
    intro(objects_for_auction, width)
    for item in objects_for_auction: # iterate through each item on the list
        clear()
        result = auction_item(item, number_of_items, iteration, width)
        if result == 'not sold':
            continue
        else:
            sold_items[item] = [result]
        iteration += 1
    print_winners(sold_items, width)


# Start program
if __name__ == "__main__":
    width = 80  # width of screen is used to center text
    while True:
        auction_program(width)
        play_again = restart(width)
        if play_again.lower() in ['no', 'n']:
            break
        clear()

#TODO 1 list when presenting all items in intro does not allow 2 items on the first row
#TODO 2 list when presenting all items in intro contain whitespace prior to first item
#TODO 3 list item at end contains additional whitespaces prior to items
