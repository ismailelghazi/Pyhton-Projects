from question_model import  Question
from data import *
from quiz_brain import *
question_banck = []
for question in question_data :
     question_text = question["text"]
     question_answer = question["answer"]
     new_question = Question(question_text,question_answer)
     question_banck.append(new_question)

Quiz =QuizBrain(question_banck)
while Quiz.sill_has_question():
     Quiz.next_question()