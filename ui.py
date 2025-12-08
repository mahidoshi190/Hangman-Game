import tkinter as tk
from logic import HangmanGame
from wordlist import get_random_word
import random
import string

game = None

# UI Frames

def show_welcome_screen():
    welcome_frame.pack(fill="both", expand=True)
    category_frame.pack_forget()
    game_frame.pack_forget()

def show_category_screen():
    welcome_frame.pack_forget()
    category_frame.pack(fill="both", expand=True)
    game_frame.pack_forget()

def show_game_screen():
    welcome_frame.pack_forget()
    category_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

# Game setup

def start_new_game(difficulty=None, max_chances=6):
    global game
    chosen_category = category_var.get()
    if chosen_category == "random":
        chosen_category = random.choice(["fruits", "animals", "countries"])
    chosen_difficulty = difficulty_var.get()
    if chosen_difficulty == "random":
        chosen_difficulty = random.choice(["easy","medium","hard"])
    game = HangmanGame(get_random_word(category=chosen_category, difficulty=chosen_difficulty), max_chances)
    category_display_label.config(text=f"Category: {chosen_category.capitalize()}    |    Difficulty: {chosen_difficulty.capitalize()}")
    hangman_label.config(text=hangman(0))
    update_display()
    reset_buttons()
    message_label.config(text="Guess a letter!", fg="#ff69b4")
    play_again_button.pack_forget()
    show_game_screen()

def make_guess(letter):
    if game.game_over:
        return
    game.guess_letter(letter)
    update_display()
    letter_buttons[letter].config(state="disabled", bg="#d3d3d3")
    
    if game.game_over:
        if game.win:
            message_label.config(text=f"🥳 You guessed it! The word was '{game.word}'!", fg="#32cd32")
        else:
            message_label.config(text=f" Game over! The word was '{game.word}'", fg="#ff4500")
        play_again_button.pack(pady=10)


# UI

def update_display():
    for widget in word_frame.winfo_children():
        widget.destroy()
    for letter in game.word:
        if letter in game.correct_letters:
            lbl = tk.Label(word_frame, text=letter.upper(), width=2, height=1,
                           font=("Comic Sans MS", 36), bg="#ffb6c1", fg="white", relief="raised")
        else:
            lbl = tk.Label(word_frame, text="_", width=2, height=1,
                           font=("Comic Sans MS", 36), bg="#ffe4e1", fg="#ff69b4", relief="raised")
        lbl.pack(side="left", padx=5)
    guessed_label.config(text="Guessed: " + ", ".join(game.guessed_letters))
    wrong_guesses = game.max_chances - game.chances_left
    hangman_label.config(text=hangman(wrong_guesses))

def reset_buttons():
    for btn in letter_buttons.values():
        btn.config(state="normal", bg="#ffb6c1")

def hangman(stage):
    if stage == 0:
        return """
           ------
           |    |
                |
                |
                |
                |
        ============
        """
    elif stage == 1:
        return """
           ------
           |    |
           O    |
                |
                |
                |
        ============
        """
    elif stage == 2:
        return """
           ------
           |    |
           O    |
           |    |
                |
                |
        ============
        """
    elif stage == 3:
        return """
           ------
           |    |
           O    |
          /|    |
                |
                |
        ============
        """
    elif stage == 4:
        return """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ============
        """
    elif stage == 5:
        return """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        ============
        """
    elif stage == 6:
        return """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ============
        """

def show_difficulty_selection():
    tk.Label(category_frame, text="Choose Difficulty:", font=("Helvetica", 14), bg="#fff0f5", fg="#ff69b4").pack(pady=10)
    global difficulty_var, difficulty_menu
    difficulty_var = tk.StringVar()
    difficulty_var.set("random")
    difficulty_menu = tk.OptionMenu(category_frame, difficulty_var, "random", "easy", "medium", "hard")
    difficulty_menu.config(font=("Helvetica", 12), bg="#ffb6c1", fg="white", width=15)
    difficulty_menu["menu"].config(bg="#ffe4e1", fg="#ff69b4")
    difficulty_menu.pack(pady=5)


# Tkinter UI setup

root = tk.Tk()
root.title("Hangman game")
root.config(bg="#fff0f5")
root.geometry("700x600")

# Welcome Frame
welcome_frame = tk.Frame(root, bg="#fff0f5")
hango_label = tk.Label(welcome_frame, text="Hello! 👋\nLet's play Hangman together!", 
                       font=("Comic Sans MS", 24), bg="#fff0f5", fg="#ff69b4", wraplength=600, justify="center")
hango_label.pack(pady=50)
continue_button = tk.Button(welcome_frame, text="Continue", font=("Helvetica", 16), bg="#ff69b4", fg="white",
                            command=show_category_screen)
continue_button.pack(pady=20)

# Category Selection Frame
category_frame = tk.Frame(root, bg="#fff0f5")
tk.Label(category_frame, text="Choose Category:", font=("Helvetica", 14), bg="#fff0f5", fg="#ff69b4").pack(pady=10)
category_var = tk.StringVar()
category_var.set("random")
category_menu = tk.OptionMenu(category_frame, category_var, "random", "fruits", "animals", "countries")
category_menu.config(font=("Helvetica", 12), bg="#ffb6c1", fg="white", width=15)
category_menu["menu"].config(bg="#ffe4e1", fg="#ff69b4")
category_menu.pack(pady=5)
show_difficulty_selection()
start_game_button = tk.Button(category_frame, text="Start Game", font=("Helvetica", 16), bg="#ff69b4", fg="white",
                              command=start_new_game)
start_game_button.pack(pady=20)

# Game Frame
game_frame = tk.Frame(root, bg="#fff0f5")
category_display_label = tk.Label(game_frame, text="", font=("Helvetica", 16), bg="#fff0f5", fg="#ff69b4")
category_display_label.pack(pady=5)
hangman_label = tk.Label(game_frame, text="", font=("Courier", 12), bg="#fff0f5", fg="#ff69b4", justify="left")
hangman_label.pack(pady=10)
word_frame = tk.Frame(game_frame, bg="#fff0f5")
word_frame.pack(pady=20)
guessed_label = tk.Label(game_frame, text="", font=("Helvetica", 14), bg="#fff0f5", fg="#ff69b4")
guessed_label.pack(pady=5)
message_label = tk.Label(game_frame, text="", font=("Helvetica", 18, "bold"), bg="#fff0f5")
message_label.pack(pady=10)
buttons_frame = tk.Frame(game_frame, bg="#fff0f5")
buttons_frame.pack(pady=10)

letter_buttons = {}
for i, letter in enumerate(string.ascii_lowercase):
    btn = tk.Button(buttons_frame, text=letter.upper(), width=4, height=2,
                    bg="#ffb6c1", fg="white", font=("Helvetica", 12, "bold"),
                    command=lambda l=letter: make_guess(l))
    btn.grid(row=i//9, column=i%9, padx=5, pady=5)
    letter_buttons[letter] = btn

    # Hover effect
    def on_enter(e, b=btn):
        if b['state'] == "normal":
            b['bg'] = "#ff69b4"
    def on_leave(e, b=btn):
        if b['state'] == "normal":
            b['bg'] = "#ffb6c1"
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

play_again_button = tk.Button(game_frame, text="Play Again 💖", font=("Helvetica", 16), bg="#ff69b4", fg="white",
                              command=show_category_screen)

# Start with Welcome Screen
show_welcome_screen()
root.mainloop()


 
 

 
 
 