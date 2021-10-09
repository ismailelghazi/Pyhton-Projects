class QuizBrain:
    def __init__(self, Q_list):
        self.question_number = 0
        self.question_list = Q_list

    def sill_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_jawab = input(f"Q.{self.question_number}:{current_question.text} (TRUE/FALSE):")
        self.check_answer(user_jawab, current_question.jawab)
    # def check_answer(self, user_jawab,):
