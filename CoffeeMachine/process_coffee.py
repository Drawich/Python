import game_data


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    if is_resource_sufficient(order_ingredients):
        for item in order_ingredients:
            game_data.resources[item] -= order_ingredients[item]
        return True
    else:
        return False


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if item not in game_data.resources:
            print(f"Sorry, {item} is not available.")
            return False
        elif order_ingredients[item] > game_data.resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
