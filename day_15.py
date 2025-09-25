# Dictionary having Data
class Question:
    def __init__(self, q_text, q_answer):
        self.q_text = q_text
        self.q_answer = q_answer

question_data = [
    {"text": "The capital of France is Paris.", "answer": "True"},
    {"text": "The Sun is a planet.", "answer": "False"},
    {"text": "Python is a type of snake as well as a programming language.", "answer": "True"},
    {"text": "The Great Wall of China is visible from space.", "answer": "False"},
    {"text": "Water boils at 100°C under normal atmospheric pressure.", "answer": "True"},
    {"text": "Mount Everest is the tallest mountain in the world.", "answer": "True"},
    {"text": "Sharks are mammals.", "answer": "False"},
    {"text": "The human body has 206 bones.", "answer": "True"},
    {"text": "Venus is the closest planet to the Sun.", "answer": "False"},
    {"text": "Lightning never strikes the same place twice.", "answer": "False"}
]

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text} (True/False): ")
        self.check_answer(user_answer, current_question.q_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

# Create Question objects
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
