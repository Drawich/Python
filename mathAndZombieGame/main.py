from collections import Counter
import random
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


# Validating user input
def input_valid_str(question, error_message, validation):
    """Validates user input for string values"""
    answer = input(question).strip().lower()
    while answer not in validation:
        answer = input(f'{error_message}\n{question}')
    return answer


def input_valid_int(question, error_message, min_val, max_val):
    """Validates user input for integer values"""
    while True:
        str_answer = input(question).strip()
        if str_answer.isdigit() and min_val <= int(str_answer) <= max_val:
            return int(str_answer)
        print(error_message)


# intro
def print_intro():
    """Prints the game introduction."""
    print("En häxa har förhäxat vårt land där fel svar på mattetal förvandlar oss till zombies.")
    print("Du behöver samla ingredienser från varje rum för att skapa ett botemedel.")
    print("Var försiktig så att du inte öppnar fel dörr och blir uppäten av zombierna som bor här.")
    print("Vårat öde vilar på dina axlar!\nLycka till!\n")


# Set starting values
def zombie_doors(door_count):
    """Randomly selects one door for zombies to hide behind by marking it with 1."""
    doors = [0] * door_count
    random_index = random.randint(0, door_count - 1)
    doors[random_index] = 1
    return doors


def get_question_count():
    """Gets the number of questions the player wants to play with."""
    return input_valid_int("Hur många frågor vill du spela med? Välj mellan 12-39\n",
                           "Du har angivit ett ogiltigt antal frågor!", 12, 39)


def get_math_operation():
    """Gets the math operation the player wants to use."""
    return input_valid_str("Vilket räknesätt vill du använda? Välj mellan *, //, % och 'slumpa'\n".lower(),
                           "Du har angivit ett ogiltigt tecken!", ('*', '//', "%", "slumpa")).lower()


# Create questions
def list_math_questions(question_count, sign, number_2):
    """Generates a list of math questions for the game play"""
    questions = []
    if sign == "slumpa":
        return list_questions_random_sign(question_count)
    while len(questions) < question_count:
        number_1 = random.randint(0, 12)
        new_question = [number_1, sign, number_2]
        if not check_for_duplicates(questions, question_count, new_question):
            questions.append(new_question)
    return questions


def list_questions_random_sign(question_count):
    """Creates a list of math questions where both numbers and sign are randomized."""
    randomized_math_question_list = []
    while len(randomized_math_question_list) < question_count:
        num_1 = random.randint(0, 12)
        sign = random.choice(["*", "%", "//"])
        num_2 = random.randint(2, 12) if sign == "*" else random.randint(2, 5)
        new_question = [num_1, sign, num_2]
        if not check_for_duplicates(randomized_math_question_list, question_count, new_question):
            randomized_math_question_list.append(new_question)
    return randomized_math_question_list


def assign_second_number(math_sign):
    """Assigns second number for the math equation based on sign."""
    if math_sign == "*":
        return input_valid_int("Välj ett nummer mellan 2-12\n", "Du har angivit ett ogiltigt nummer!", 2, 12)
    elif math_sign in ("//", "%"):
        return input_valid_int("Välj ett nummer mellan 2-5\n", "Du har angivit ett ogiltigt nummer!", 2, 5)
    else:
        return 0


def check_for_duplicates(completed_question_list, question_range,
                         test_question):
    """Checks if a question is duplicate and adds it based on logic."""
    existing_question_count = completed_question_list.count(test_question)
    if (question_range < 14 and existing_question_count == 1) or \
       (14 <= question_range <= 26 and existing_question_count >= 2) or \
       (question_range >= 27 and existing_question_count >= 3):
        return True

    return False


# Corrects user's response to questions
def correct_math_question(question, answer):
    """Comparing user's answer and correct answer for the math question"""
    if question[1] == "//":
        calculated_answer = question[0] // question[2]
    elif question[1] == "%":
        calculated_answer = question[0] % question[2]
    else:
        calculated_answer = question[0] * question[2]
    return calculated_answer == answer


def correct_zombie_door(chosen_door, list_of_doors):
    """Checks if there are zombies behind the chosen door. """
    list_of_doors.insert(0, 3)
    wrong_door = list_of_doors.index(1)
    if list_of_doors[chosen_door] == 1:
        return handle_incorrect_answer()
    else:
        return handle_correct_zombie_answer(wrong_door)


def handle_correct_zombie_answer(door_with_zombies):
    """Handles the scenario when the user answers a question correctly."""
    responses = [
        f"Puh, inga zombies här. De var bakom dörr nummer {door_with_zombies}. Vi tar ingrediensen i detta rummet. Kom så fortsätter vi!",
        f"Rätt val! Inga zombies här. De gömde sig bakom dörr nummer {door_with_zombies}. Nu kan vi gå vidare med ingrediensen från detta rum.",
        f"Bra jobbat! Zombiesarna var bakom dörr nummer {door_with_zombies}. Nu kan vi säkra ingrediensen från detta rum.",
        f"Du gissade rätt! Inga zombies här. De lurade bakom dörr nummer {door_with_zombies}. Låt oss ta vad vi behöver och gå vidare!",
        f"Bra gjort! Inga zombies här. De gömde sig bakom dörr nummer {door_with_zombies}. Nu kan vi fortsätta med nästa steg.",
        f"Du valde rätt! Inga zombies här. Dörr nummer {door_with_zombies} var den med zombies. Vi har säkrat ingrediensen från detta rum.",
        f"Rätt val! Zombies lurade bakom dörr nummer {door_with_zombies}. Nu kan vi gå vidare med vad vi letade efter.",
        f"Fantastiskt! Inga zombies här. De var faktiskt bakom dörr nummer {door_with_zombies}. Låt oss ta vad vi behöver och gå vidare!",
        f"Duktigt jobbat! Zombies var gömda bakom dörr nummer {door_with_zombies}. Nu kan vi fortsätta vår resa."
    ]
    print(random.choice(responses))
    return True


def handle_correct_math_answer(count):
    """Handles the scenario when the user answers a question correctly."""
    responses = [
        "Bra jobbat!",
        "Fantastiskt!",
        "Korrekt!",
        "Perfekt svar!",
        "Rätt svar!",
        "Ypperligt!",
        "Du har helt rätt!",
        "Du är på rätt spår!",
        "Utmärkt jobbat!",
        "Du är grym på det här!",
        "Du är fantastisk!",
        "Du har hängt med riktigt bra!"
    ]
    print(random.choice(responses))
    count += 1
    return count


def handle_incorrect_answer():
    """Handles the scenario when the user answers a question incorrectly."""
    responses = [
        "Det är fel. Du har förlorat och blivit förvandlad till en zombie.",
        "Fel! Zombies attackerar! Fly medan du kan! Spelet är slut.",
        "Oj! Det var inte rätt. Du har förlorat!",
        "Fel svar! Nu har du råkat störa zombisarna. Fly långt härifrån!",
        "Tyvärr, det är inte rätt. En flock av zombies anfaller!",
        "Tyvärr, det var inte rätt. Zombies har samlats och är redo att attackera.",
        "Oh nej! Du har rört upp en hel zombienäste med det svaret."
        "Fel svar! Zombiehorden är på väg mot din position nu.",
        "Oops! Zombies har fått vittring på dig efter det felaktiga svaret."
    ]
    print(random.choice(responses))
    return False


def congratulate_player():
    """Congratulates the player upon winning the game."""
    return ("Grattis du har vunnit spelet och räddat hela världen!")


# To restart level or game
def restart_level_again():
    """Asks the user to restart the level with the same settings if user has answered wrong"""
    restart_level_question = input_valid_str(
        "Vill du spela denna nivån igen? (j/n)\n",
        "Du har angivit en ogiltig input!",
        ("j", "ja", "n", "nej"),
    )
    return restart_level_question.lower() in ["j", "ja"]


def play_again():
    """Asks the user to restart the level with the same settings if user has answered wrong"""
    play_again_question = input_valid_str(
        "Vill du spela ett nytt spel? (j/n)\n",
        "Du har angivit en ogiltig input!",
        ("j", "ja", "n", "nej"),
    )
    return play_again_question.lower() in ["j", "ja"]


# Goes over one question at the time and test out the responses
def play_questions_and_doors(math_questions, answer_question_count, zombie_door_list):
    """Generates questions from question list"""
    correct_count = 0
    zombie_doors_left = answer_question_count - correct_count
    while correct_count < answer_question_count:
        for question in math_questions:
            clear()
            print(f"Du har svarat korrekt på: {correct_count} utav {len(math_questions)} frågor.")
            # print(Counter(map(tuple, math_questions))) #tests for duplicates to verify logic

            # Ask the user to solve the math question one at the time
            user_answer = input_valid_int(f"Vad blir {question[0]} {question[1]} {question[2]}?\n",
                                          "Du har angivit ett ogiltigt svar!", 0, 1000000)
            if correct_math_question(question, user_answer):
                handle_correct_math_answer(correct_count)
                correct_count += 1
                if zombie_doors_left != 1:
                    if not zombie_quiz(zombie_door_list, zombie_doors_left):
                        return False
                    zombie_doors_left -= 1
                    zombie_door_list = zombie_doors(zombie_doors_left)
                    if zombie_doors_left == 1:
                        print("Vi har alla ingredienserna! Vi behöver bara lösa det sista mattetalet")
                    input('Tryck på Enter för att fortsätta...')
            else:
                return False, handle_incorrect_answer()
        return True


def zombie_quiz(zombie_door_list, zombie_doors_left):
    """Check if the chosen door contains zombies"""
    # print(zombie_door_list)  # For testing purposes
    print(f"Du har {zombie_doors_left} dörrar kvar att öppna.")
    door_number = input_valid_int(
        f"Välj en dörr mellan 1 och {zombie_doors_left}\n",
        "Den här dörren existerar inte.", 1, zombie_doors_left)
    return correct_zombie_door(door_number, zombie_door_list)


def play_level(answer_question_count, math_questions, zombie_door_list):
    """Starts or restarts the level with chosen settings"""
    while True:
        won_game = play_questions_and_doors(math_questions, answer_question_count, zombie_door_list)
        if won_game:
            print(congratulate_player())
            return None
        else:
            if not restart_level_again():
                return False


def main():
    """Is starting the game by collecting settings based on user input and executes the game_level based on settings"""
    print_intro()
    while True:
        answer_question_count = get_question_count()
        sign_answer = get_math_operation()
        second_number = assign_second_number(sign_answer)

        # Generate the list of math questions based on user's input
        math_questions = list_math_questions(answer_question_count,
                                             sign_answer, second_number)

        # Generates a list of doors with zombies hiding behind one of them
        zombie_door_list = zombie_doors(answer_question_count)

        # Start game level
        play_level(answer_question_count, math_questions,
                             zombie_door_list)

        # Ask if the player wants to play again if winning the game
        if not play_again():
            return  # Exit the function if the user chooses not to replay the game


# Start game
main()
print("Stänger av spelet!")
