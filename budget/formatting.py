def offset_formatting(max_category_length):
    offset = ' ' * 5
    offset_between_columns = 20 + max_category_length
    return offset, offset_between_columns


def apply_budget_color(amount):
    if float(amount) > 0:
        formatted_amount = green(amount)
    else:
        formatted_amount = red(amount)
    return formatted_amount


def green(text):
    return f"\033[92m{text}\033[0m"


def red(text):
    return f"\033[91m{text}\033[0m"
