class QuizBrain:
    def __init__(self, q_list):
        self.quetion_numebr = 0
        self.score = 0
        self.quetion_list = q_list

    def still_has_question(self):
        return self.quetion_numebr < len(self.quetion_list)

    def next_quetion(self):
        current_question = self.quetion_list[self.quetion_numebr]
        self.quetion_numebr += 1
        user_answer = input(f"Q. {self.quetion_numebr}: {current_question.text} (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"You current score is {self.score}/{self.quetion_numebr}")
        print("\n")