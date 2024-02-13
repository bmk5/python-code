class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.index = 0
        self.score = 0

    def add_index(self):
        self.index += 1

    def has_next_question(self):
        return not (self.index == len(self.questions))

    def add_score(self):
        self.score += 1

    def check_answer(self, answer, response):
        if response == answer:
            print("You got it right!")
            self.add_score()
        else:
            print("You got it wrong!")

        print(f"The correct answer was {answer.capitalize()}")

    def next_question(self):
        question = self.questions[self.index]
        self.add_index()

        response = input(f"Q{self.index}: {question.get_text()} (True/False)?: ").lower()
        self.check_answer(question.get_answer(), response)
        print(f"Your current score was: {self.score}/{self.index}\n\n")

