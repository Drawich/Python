import validate_input
import game_data


def display_menu_and_intro():
    offset = ' ' * 80
    offset_sign = ' ' * 26
    max_item_length = max(len(item_name) for item_name in game_data.MENU.keys())
    line_length = 100
    print("(write 'help' for options)\n")
    print(f"{offset_sign} WELCOME TO OUR COFFEE SHOP {offset_sign} MENU")

    for item_name, item_details in game_data.MENU.items():
        price = f"${item_details['cost']:.2f}"
        spaces_needed = max_item_length - len(item_name) + 2
        print(f"{offset}{item_name.capitalize()}{' ' * spaces_needed}   {price}")
    print('=' * line_length)


def get_order(current_menu):
    return validate_input.validate_text_input(
        "What would you like to order today? \n",
        current_menu,
        'That is not currently on our menu')


def display_help():
    indented = ' ' * 5
    offset = len(' [drink_name] ')
    print("You can write:")
    print(f"{indented}report {(offset - len('report')) * ' '}- how many resources you have left")
    print(f"{indented}off {(offset - len('off')) * ' '}- turns off the coffee maker")
    print(f"{indented}[drink_name] {(offset - len('[drink_name]')) * ' '}- chose a drink from our menu to order")


def display_report():
    print(f"Water: {game_data.resources['water']}ml")
    print(f"Milk: {game_data.resources['milk']}ml")
    print(f"Coffee: {game_data.resources['coffee']}g")
    print(f"Money: ${game_data.profit}")
