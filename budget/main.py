import expense_manager
import validate_input
import summary


def main():
    selections = {1: 'New expense', 2: 'Print summary'}
    budget = 2000
    expense_file_path = "expenses.csv"

    while True:
        prompt = f'What would you like to do today? \n 1. {selections[1]}\n 2. {selections[2]}\n'

        select = validate_input.validate_text_input(prompt,
            lambda x: (str(x).isdigit() and int(x) in [1, 2]) or str(x).strip().lower() in [option.lower() for option in selections.values()],
            'That is not a valid selection'
        )

        if str(select).isdigit():
            select = int(select)
        else:
            select = str(select).strip().lower()

        if select == 1 or select == 'new expense':
            print('Adding expense...')
            expense = expense_manager.get_user_expense()
            save_expense_to_file(expense, expense_file_path)
        elif select == 2 or select == 'print summary':
            print('Printing summary...')
            summary.summarize_expenses(expense_file_path, budget)
        else:
            print("Invalid selection. Please enter either '1' or '2'.")

def save_expense_to_file(expense, expense_file_path):
    print(f'Saving user expense: {expense} to {expense_file_path}')
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n")

if __name__ == "__main__":
    main()
