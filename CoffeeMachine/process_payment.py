import validate_input


def is_transaction_successful(payment, cost, register):
    """Checks if payment is enough and calculates change if necessary."""
    if payment >= cost:
        change = payment - cost
        print(f"\nHere is ${change:.2f} in change.")
        register += cost
        return True, register
    else:
        print("\nSorry, that's not enough money. Refunding your coins.")
        return False, register


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins to proceed with your order.\n")
    error_message = 'Please, write the number of coins as a positive number.'
    quarters = int(validate_input.validate_float_input('How many quarters?: ', error_message))
    dimes = int(validate_input.validate_float_input('How many dimes?: ', error_message))
    nickels = int(validate_input.validate_float_input('How many nickels?: ', error_message))
    pennies = int(validate_input.validate_float_input('How many pennies?: ', error_message))

    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
