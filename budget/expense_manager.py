from expenses import Expense
import validate_input


def get_expense_details():
    expense_name = validate_input.validate_text_input('Enter expense name: \n',
                                       lambda x: any(char.isalnum() for char in x) and len(x) > 0,
                                       "Enter the name of the item or expense, for example 'Mcdonald's'")
    expense_amount = validate_input.validate_float_input('Enter expense amount: \n',
                                                         'Please, enter the amount in digits')
    return expense_name, expense_amount


def select_expense_category():
    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc"
    ]
    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f'  {i+1}. {category_name}')

        value_range = f'[1- {len(expense_categories)}]'
        selected_index = int(
            validate_input.validate_text_input(f'Enter a category number {value_range}: ',
                                               lambda x: x.isdigit() and 1 <= int(x) <= len(expense_categories),
                                               "Please, write the number on the category you'd like to use")) - 1
        selected_category = expense_categories[selected_index]
        return selected_category


def get_user_expense():
    expense_name, expense_amount = get_expense_details()
    selected_category = select_expense_category()
    new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
    return new_expense
