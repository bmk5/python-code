from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


questions = []
for item in question_data:
    questions.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(questions)

while quiz.has_next_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.index}")