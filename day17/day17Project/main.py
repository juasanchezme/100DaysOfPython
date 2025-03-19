from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []    
for dictionary in question_data:
    question = dictionary["text"]
    answer = dictionary["answer"]


    question = Question(question, answer)
    question_bank.append(question)

new_quiz = QuizzBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print(f"You've completed the quiz, your final score is {new_quiz.score}/{len(new_quiz.question_list)}")