import game_data
import format_data
import game_setup
import display_text_input
import process_coffee
import process_payment

our_menu = game_setup.menu()
display_text_input.display_menu_and_intro()
profit = game_data.profit

while True:
    order = display_text_input.get_order(our_menu)
    if order == 'off':
        break
    elif order == 'help':
        display_text_input.display_help()
    elif order == 'report':
        display_text_input.display_report()
    else:
        drink = game_data.MENU[order]
        if process_coffee.is_resource_sufficient(drink["ingredients"]):
            payment = process_payment.process_coins()
            payment_accepted, profit = process_payment.is_transaction_successful(payment, drink["cost"], profit)
            game_data.profit = profit
            if payment_accepted:
                process_coffee.make_coffee(order, drink["ingredients"])
                print(f'Enjoy your {order}!')
    input('Press enter to continue..')
    format_data.clear()
    display_text_input.display_menu_and_intro()
