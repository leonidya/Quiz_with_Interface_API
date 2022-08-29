THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
# TODO: Create a label SCORE in the right up corner
        score = 0
        self.label_score = Label(text=f"Score: {score}", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1, pady=20)
# TODO: Create Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Welcome to Quizzler",
            font=FONT,
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

# TODO: Create a button X
        x_image = PhotoImage(file="images/false.png")
        self.button_x = Button(image=x_image, highlightthickness=0, command=self.false_pressed)
        self.button_x.grid(row=2, column=1, pady=50)
# TODO: Create a button V
        v_image = PhotoImage(file="images/true.png")
        self.button_v = Button(image=v_image, highlightthickness=0, command=self.true_pressed)
        self.button_v.grid(row=2, column=0)
        self.get_next_question()

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You reach the end of the Quiz, the score is: {self.quiz.score}")
            self.button_v.config(state="disabled")
            self.button_x.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="pink")
        self.window.after(1000, self.get_next_question)