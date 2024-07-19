import validate_input
import format_data


class QuizBrain:
    """A class representing a quiz game engine."""
    def __init__(self, q_list, number_of_questions):
        """Initialize the QuizBrain instance.

        Args:
            q_list (list): List of Question objects.
            number_of_questions (int): Number of questions to ask in the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.number_of_questions = number_of_questions

    def next_question(self):
        """Display and handle the next question in the quiz."""
        print(format_data.display_score(self.score, self.number_of_questions))
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = f'Q.{self.question_number}. {current_question.text}\n True or False? \n'
        user_answer = validate_input.validate_text_input(question,
                                                         lambda x: x in ['true', 'false', 't', 'f'],
                                                         "Please, write 'true' or 'false'")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Check the user's answer against the correct answer and update the score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            if correct_answer.lower() == 'true':
                print("No, it was actually true.")
            else:
                print("Unfortunately, the answer is false.")
        input('Press enter for next question...')
        format_data.clear()
