
import random
from quiz_game import questions as q
import os
import platform

a = 10


def area(side):
    return side ** 2


def calcualtor(x, y):
    print("addition is ", x+y)


class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.total_questions = 0

    @staticmethod
    def clear_console():
        """Clears the console based on the platform."""
        command = "cls" if platform.system() == 'Windows' else "clear"
        os.system(command)

    def select_questions(self, num_questions=5):
        """Randomly selects a specified number of questions."""
        self.questions = random.sample(q, num_questions)
        self.total_questions = len(self.questions)

    def display_question(self, question, index):
        """Displays the current question and its options."""
        print(f"\nQuestion {
              index}/{self.total_questions}: {question['question']}")
        print(f"A: {question['A']}")
        print(f"B: {question['B']}")
        print(f"C: {question['C']}")
        print(f"D: {question['D']}")

    def get_user_answer(self):
        """Prompts the user for an answer and returns it."""
        return input("Enter your answer (A/B/C/D): ").upper()

    def check_answer(self, question, user_answer):
        """Checks if the user's answer is correct and updates the score."""
        if user_answer == question["answer"]:
            print("Correct answer!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is: {question['answer']}")

        print(f"Your current score is: {self.score}/{self.total_questions}")

    def play(self):
        """Runs the main game loop."""
        self.clear_console()
        print("****************************")
        print("Welcome to My Quiz Game")
        print("****************************")

        self.select_questions()  # Select random questions

        for i, question in enumerate(self.questions, start=1):
            self.display_question(question, i)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)

        # Final results
        print("\n****************************")
        print(f"You answered {self.score} out of {
              self.total_questions} questions correctly.")
        print(f"Your final score is: {
              (self.score / self.total_questions) * 100:.2f}%")
        print("****************************")


# Run the game
if __name__ == "__main__":
    game = QuizGame()
    game.play()
