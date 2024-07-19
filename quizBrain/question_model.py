class Question:
    """Initialize a Question object.

    Args:
        q_text (str): The text of the question.
        q_answer (str): The correct answer to the question.
    """
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer