from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

CARD_BACK = 'Day 31\\flash-card-project\\images\\card_back.png'
CARD_FRONT = 'Day 31\\flash-card-project\\images\\card_front.png'
RIGHT = 'Day 31\\flash-card-project\\images\\right.png'
WRONG = 'Day 31\\flash-card-project\\images\\wrong.png'
FRENCH_WORDS = 'Day 31\\flash-card-project\\data\\french_words.csv'

data = pandas.read_csv(FRENCH_WORDS)
to_learn = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

def flip_card():
    code=0 #CONTINUE

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2) 

cross_image = PhotoImage(file=WRONG)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file=RIGHT)
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

window.after(3000)

next_card()
window.mainloop()