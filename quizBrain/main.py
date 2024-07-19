from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import validate_input
import format_data


def quiz_game(quiz, number_of_questions):
    """Runs the quiz game with the specified number of questions.

        Args:
            quiz (QuizBrain): The QuizBrain object containing the quiz questions.
            number_of_questions (int): The number of questions to ask in the quiz.

        Returns:
            None
        """
    format_data.clear()
    for _ in range(number_of_questions):
        quiz.next_question()

    print(f"You've completed the quiz \nYour final score was {quiz.score}/{number_of_questions}")


def main():
    """Sets up and starts the quiz game."""
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    print(format_data.center_text('WELCOME TO QUIZ BRAIN!'))
    number_of_questions = validate_input.validate_int_input(
        f'Choose a number of questions you\'d like between 1 and {len(question_data)}: \n',
        lambda x: 1 <= x <= len(question_data))

    quiz = QuizBrain(question_bank, number_of_questions)
    quiz_game(quiz, number_of_questions)


if __name__ == "__main__":
    main()

