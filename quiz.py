import tkinter as tk
from tkinter import messagebox

class Question:
    def _init_(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()


class QuizApp:
    def _init_(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        self.label = tk.Label(master, text=self.questions[self.current_question_index].text)
        self.label.pack()

        self.radio_var = tk.StringVar()
        for index, option in enumerate(self.questions[self.current_question_index].options, start=1):
            radio_button = tk.Radiobutton(master, text=option, variable=self.radio_var, value=option)
            radio_button.pack()

        self.next_button = tk.Button(master, text="Next", command=self.check_answer)
        self.next_button.pack()

    def check_answer(self):
        user_answer = self.radio_var.get()
        correct_option = self.questions[self.current_question_index].correct_option

        if user_answer.lower() == correct_option.lower():
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.update_question()
        else:
            self.show_score()

    def update_question(self):
        self.label.config(text=self.questions[self.current_question_index].text)
        self.radio_var.set('')
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        for index, option in enumerate(self.questions[self.current_question_index].options, start=1):
            radio_button = tk.Radiobutton(self.master, text=option, variable=self.radio_var, value=option)
            radio_button.pack()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.questions)}")
        self.master.destroy()


# Sample quiz questions
question1 = Question("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], "Paris")
question2 = Question("Which programming language is this quiz written in?", ["Java", "Python", "C++", "JavaScript"], "Python")
question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale")

# Create the root window
root = tk.Tk()
root.title("Quiz App")

# Create a quiz app with the sample questions
quiz_app = QuizApp(root, [question1, question2, question3])

# Run the GUI app
root.mainloop()
