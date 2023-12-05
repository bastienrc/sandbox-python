import tkinter as tk
from tkinter import messagebox
import random


class Pendu:
    def __init__(self, window):
        self.window = window
        self.window.title("Le jeux du Pendu")

        self.words = [
            "ENTERPRISE",
            "DESTINY",
            "SERENITY",
            "ROCINANTE",
            "DISCOVERY",
            "VOYAGER",
            "PROMETHEUS",
            "ORVILLE"
        ]
        self.word_to_guess = ""
        self.displayed_word = ""
        self.used_letters = []
        self.remaining_lives = 6

        self.word_label = tk.Label(
            self.window, text=self.displayed_word, font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.keyboard_frame = tk.Frame(self.window)
        self.keyboard_frame.pack()

        self.canvas = tk.Canvas(self.window, width=300, height=300)
        self.canvas.pack()

        self.letter_buttons = {}
        self.create_keyboard()
        self.new_game()

    def new_game(self):
        """Start a new game."""
        self.word_to_guess = random.choice(self.words).upper()
        self.displayed_word = "_" * len(self.word_to_guess)
        self.used_letters = []
        self.remaining_lives = 6
        self.letter_buttons = {}
        self.update_hangman_display()
        self.update_word_display()
        self.enable_all_buttons()

    def create_keyboard(self):
        """Create the virtual keyboard."""
        # alphabet = "BÉPOÈVDLJZWAUIECTSRNMÀYXKQGHFÇ"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            letter_button = tk.Button(self.keyboard_frame, text=letter,
                                      command=lambda l=letter: self.guess_letter(l), font=("Arial", 12))
            letter_button.grid(row=(ord(letter) - ord('A')) // 7,
                               column=(ord(letter) - ord('A')) % 7, padx=5, pady=5)
            self.letter_buttons[letter] = letter_button

    def guess_letter(self, letter):
        """Handle the player's letter guess."""
        if letter not in self.used_letters:
            self.used_letters.append(letter)
            if letter not in self.word_to_guess:
                self.remaining_lives -= 1
                self.update_hangman_display()

            self.update_word_display()
            self.check_victory()

            if self.remaining_lives == 0:
                self.end_game("Perud ! il fallait trouver: " + self.word_to_guess)
                # self.end_game("You lost. The word was: " + self.word_to_guess)
                self.disable_all_buttons()

            self.disable_button(letter)

    def disable_button(self, letter):
        """Disable the guessed letter button."""
        letter = letter.upper()
        button = self.letter_buttons.get(letter)
        if button:
            button.config(state="disabled")

    def enable_all_buttons(self):
        """Enable all virtual keyboard buttons."""
        for button in self.letter_buttons.values():
            button.config(state="normal")

    def disable_all_buttons(self):
        """Disable all virtual keyboard buttons."""
        for button in self.letter_buttons.values():
            button.config(state="disabled")

    def update_hangman_display(self):
        """Update the hangman display based on remaining lives."""
        self.canvas.delete("all")

        if self.remaining_lives < 6:
            # Base of the gallows
            self.canvas.create_line(50, 250, 250, 250, width=2)

        if self.remaining_lives < 5:
            self.canvas.create_line(
                150, 250, 150, 50, width=2)  # Vertical post

        if self.remaining_lives < 4:
            self.canvas.create_line(
                150, 50, 250, 50, width=2)  # Horizontal post

        if self.remaining_lives < 3:
            self.canvas.create_line(250, 50, 250, 100, width=2)  # Rope

        if self.remaining_lives < 2:
            self.canvas.create_oval(225, 100, 275, 150, width=2)  # Head

        if self.remaining_lives < 1:
            self.canvas.create_line(250, 150, 250, 200, width=2)  # Body

    def update_word_display(self):
        """Update the displayed word based on guessed letters."""
        new_displayed_word = ""
        for letter in self.word_to_guess:
            if letter.upper() in self.used_letters:
                new_displayed_word += letter
            else:
                new_displayed_word += "_"
        self.displayed_word = new_displayed_word
        self.word_label.config(text=self.displayed_word)

    def check_victory(self):
        """Check if the player has guessed the entire word."""
        if "_" not in self.displayed_word:
            self.end_game(
                "Félicitations! Tu as deviné le mot: " + self.word_to_guess)
                # "Congratulations! You guessed the word: " + self.word_to_guess)
            self.disable_all_buttons()
            self.new_game()

    def end_game(self, message):
        """Display a message at the end of the game."""
        messagebox.showinfo("Game Over", message)


if __name__ == "__main__":
    root = tk.Tk()
    game = Pendu(root)
    root.mainloop()
