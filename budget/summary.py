import datetime
import calendar
from formatting import offset_formatting, apply_budget_color
from expenses import Expense


def read_expenses_from_file(expense_file_path):
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_category, expense_name, expense_amount = line.strip().split(',')
            expense_category = expense_category.capitalize().strip()
            expense_name = expense_name.capitalize().strip()
            expense_amount = float(expense_amount)
            expenses.append(Expense(name=expense_name, amount=expense_amount, category=expense_category))
    return expenses


def calculate_max_category_length(expenses):
    return max(len(expense.category) for expense in expenses)


def print_expenses_by_category(amount_by_category, max_category_length):
    offset, offset_between_columns = offset_formatting(max_category_length)
    for key, amount in amount_by_category.items():
        amount_str = "{:.2f}".format(amount)
        print(f'{offset}{key}: $ {amount_str}')


def print_total_and_remaining_budget(total_spent, remaining_budget, max_category_length):
    offset, offset_between_columns = offset_formatting(max_category_length)

    remaining_budget_str = apply_budget_color(remaining_budget)

    print()
    print(f'{offset}Total expenses:{(offset_between_columns - len("Total expenses:")) * " "}$ {total_spent:.2f}')
    print(f'{offset}Budget remaining:{(offset_between_columns - len("Budget remaining:")) * " "}$ {remaining_budget_str}')


def print_budget_per_day(budget, total_spent, max_category_length):
    offset, offset_between_columns = offset_formatting(max_category_length)
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    remaining_budget = budget - total_spent
    daily_budget = remaining_budget / remaining_days
    daily_budget_str = "{:.2f}".format(daily_budget)
    daily_budget_formatted = apply_budget_color(daily_budget_str)
    print(f'{offset}Budget per day:{(offset_between_columns - len('Budget per day:')) * " "}$ {daily_budget_formatted}')


def summarize_expenses(expense_file_path, budget):
    expenses = read_expenses_from_file(expense_file_path)
    max_category_length = calculate_max_category_length(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print('Expenses by category:')
    print_expenses_by_category(amount_by_category, max_category_length)

    total_spent = sum([x.amount for x in expenses])
    remaining_budget = budget - total_spent

    print_total_and_remaining_budget(total_spent, remaining_budget, max_category_length)
    print_budget_per_day(budget, total_spent, max_category_length)
