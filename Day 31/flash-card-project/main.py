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
WORDS_TO_LEARN = 'Day 31\\flash-card-project\\data\\words_to_learn .csv'

current_card = {}
to_learn     = {}

try:
    data = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    original_data = pandas.read_csv(FRENCH_WORDS)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black" )
    canvas.itemconfig(card_background, image=card_front)    
    
    flip_timer = window.after(3000, func=flip_card)

def flip_card():   
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    
    data = pandas.DataFrame(to_learn)
    data.to_csv(WORDS_TO_LEARN, index=False)
    
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=CARD_FRONT)
card_back = PhotoImage(file=CARD_BACK)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2) 

cross_image = PhotoImage(file=WRONG)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file=RIGHT)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

flip_timer = window.after(3000, func=flip_card)


next_card()
window.mainloop()