import unittest
from tkinter import Tk
from unittest.mock import patch
from Pendu import Pendu


class TestPendu(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.game = Pendu(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch("Pendu.messagebox.showinfo")  # Replace showinfo with a mock
    def test_end_game(self, mock_showinfo):
        self.game.end_game("Game over")
        mock_showinfo.assert_called_once_with("Game Over", "Game over")

    def test_new_game_starts_correctly(self):
        self.assertEqual(self.game.word_to_guess, "")
        self.assertEqual(self.game.displayed_word, "")
        self.assertEqual(self.game.used_letters, [])
        self.assertEqual(self.game.remaining_lives, 6)

    def test_update_hangman_display(self):
        self.game.remaining_lives = 3
        self.game.update_hangman_display()
        self.assertEqual(list(self.game.canvas.find_all()), [])

    def test_update_word_display(self):
        self.game.word_to_guess = "PYTHON"
        self.game.used_letters = ["P", "Y"]
        self.game.update_word_display()
        self.assertEqual(self.game.displayed_word, "PY___N")

    def test_new_game_creates_valid_word(self):
        self.game.new_game()
        self.assertIn(self.game.word_to_guess, self.game.words)
        self.assertEqual(self.game.displayed_word, "_" *
                         len(self.game.word_to_guess))
        self.assertEqual(self.game.used_letters, [])
        self.assertEqual(self.game.remaining_lives, 6)

    def test_disable_button(self):
        self.game.disable_button("a")
        self.assertEqual(
            self.game.letter_buttons["A"].cget('state'), "disabled")

    def test_enable_all_buttons(self):
        self.game.enable_all_buttons()
        for button in self.game.letter_buttons.values():
            self.assertEqual(button.cget('state'), "normal")

    def test_disable_all_buttons(self):
        self.game.disable_all_buttons()
        for button in self.game.letter_buttons.values():
            self.assertEqual(button.cget('state'), "disabled")

    def test_check_victory(self):
        self.game.word_to_guess = "PYTHON"
        self.game.used_letters = ["P", "Y", "T", "H", "O", "N"]
        self.game.check_victory()
        # self.assertEqual(self.game.displayed_word, "PYTHON")
        self.assertTrue(self.game.check_victory_condition())


if __name__ == "__main__":
    unittest.main()
