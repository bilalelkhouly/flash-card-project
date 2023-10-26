from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/flashcards_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/original_flashcards.csv").to_dict(orient="records")
word_pair = {}


def generate_next_card():
    global word_pair, flip_timer
    window.after_cancel(flip_timer)
    word_pair = random.choice(data)
    french_word = word_pair["French"]
    canvas.itemconfig(flashcard_image, image=flashcard_front)
    canvas.itemconfig(flashcard_title, text="French", fill="black")
    canvas.itemconfig(flashcard_word, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_word = word_pair["English"]
    canvas.itemconfig(flashcard_image, image=flashcard_back)
    canvas.itemconfig(flashcard_title, text="English", fill="white")
    canvas.itemconfig(flashcard_word, text=english_word, fill="white")


def card_is_known():
    data.remove(word_pair)
    pandas.DataFrame(data).to_csv("data/flashcards_to_learn.csv", index=False)
    generate_next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas
flashcard_front = PhotoImage(file="./images/card_front.png")
flashcard_back = PhotoImage(file="./images/card_back.png")
check_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

flashcard_image = canvas.create_image(400, 263, image=flashcard_front)
flashcard_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
flashcard_word = canvas.create_text(400, 262, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=card_is_known)
check_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=generate_next_card)
wrong_button.grid(row=1, column=0)

generate_next_card()

window.mainloop()
