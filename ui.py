from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)
        self.canvas= Canvas(width=300,height=250, bg="white")
        self.question_text= self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Something",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)






        self.true_button = PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.true_button, highlightthickness=0, command=self.true)
        self.button1.grid(row=2, column=1)
        self.false_button = PhotoImage(file="images/false.png")
        self.button2 = Button(image=self.false_button, highlightthickness=0, command=self.false)
        self.button2.grid(row=2, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of your quiz!")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true(self):
        is_right = self.give_feedback(self.quiz.check_answer("True"))

    def false(self):

        is_right = self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)








