from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     width=280,
                                                     text="Test", 
                                                     font=("Arial", 20, "italic"), 
                                                     fill=THEME_COLOR)  
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)  
        
        
        cross_image = PhotoImage(file='Day 34/quizzler-app/images/false.png')
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.false_check)
        self.false_button.grid(column=1, row=2)
        
        check_image = PhotoImage(file='Day 34/quizzler-app/images/true.png')
        self.true_button = Button(image=check_image, highlightthickness=0, command=self.true_check)
        self.true_button.grid(column=0, row=2)        
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_check(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)
        
    def false_check(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)
        
    def give_feedback(self, result):
        if result:
            backgrnd = 'green'
        else:
            backgrnd = 'red'                
        self.canvas.config(bg=backgrnd)
        
        self.window.after(1000, self.get_next_question) 
  