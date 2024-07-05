from tkinter import *
import pandas as pd
import random
import time
import os

try:
    vocabulary = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    vocabulary = pd.read_csv("data/french_words.csv")
    vocabulary = vocabulary.to_dict(orient="records")
else:
    vocabulary = vocabulary.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
current_word = None


def create_current_word():
    global current_word
    current_word = random.choice(vocabulary)

create_current_word()
def is_known():
    create_current_word()
    global current_word
    canvas.itemconfig(current_image, image=front_image)
    canvas.itemconfig(word, text= current_word['French'])
    canvas.itemconfig(title, text="french")
    window.after(3000, func=flip_card)
    global vocabulary
    vocabulary.remove(current_word)
    vocabulary_df = pd.DataFrame(vocabulary)
    vocabulary_df.to_csv('data/words_to_learn.csv')
    next_card()




def next_card():
        create_current_word()
        global current_word
        canvas.itemconfig(current_image, image=front_image)
        canvas.itemconfig(word, text=current_word['French'])
        canvas.itemconfig(title, text="french")
        window.after(3000, func=flip_card)



def flip_card():
    global current_word
    english_translation = current_word['English']
    canvas.itemconfig(current_image, image=back_image)
    canvas.itemconfig(title, text="english")
    canvas.itemconfig(word, text=english_translation)






#window setup
window = Tk()
window.title("Flashcard app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas setup
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
current_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 100, text="french", font=("Arial", 40, "italic"), fill= "Black")
word = canvas.create_text(400, 300, text=current_word['French'], font=("Arial", 60, "bold"),  fill= "Black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column= 0, row= 0, columnspan = 2)

#button setup
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')
right_button = Button(image=right_img, highlightbackground= BACKGROUND_COLOR, command=is_known)
wrong_button = Button(image=wrong_img, highlightbackground= BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column= 0, row= 1)
right_button.grid(column= 1, row= 1)
























window.mainloop()