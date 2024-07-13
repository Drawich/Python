import game_data


def menu():
    current_menu = ['off', 'report', 'help']
    for item_name, item_info in game_data.MENU.items():
        current_menu.append(item_name)
    return current_menu
