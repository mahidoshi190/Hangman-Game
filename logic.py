class HangmanGame:
    def __init__(self, word, max_chances=6):
        self.word = word.lower()
        self.max_chances = max_chances
        self.chances_left = max_chances
        self.guessed_letters = []
        self.correct_letters = set()
        self.game_over = False
        self.win = False

    def guess_letter(self, letter):
        letter = letter.lower()

        if self.game_over:
            return "Game already over."

        if not letter.isalpha() or len(letter) != 1:
            return "Please enter a single valid letter."

        if letter in self.guessed_letters:
            return f"You already guessed '{letter}'."

        self.guessed_letters.append(letter)

        if letter in self.word:
            self.correct_letters.add(letter)

            if self._check_win():
                self.game_over = True
                self.win = True
                return "Correct! You won the game!"
            
            return f"Correct guess: {letter}"
        else:
            self.chances_left -= 1

            if self.chances_left <= 0:
                self.game_over = True
                return f"Wrong! No chances left. You lost! The word was '{self.word}'."

            return f"Wrong guess: {letter}. Chances left: {self.chances_left}"

    def get_display_word(self):
        return " ".join([letter if letter in self.correct_letters else "_" for letter in self.word])

    def _check_win(self):
        return all(letter in self.correct_letters for letter in self.word)

    def get_game_status(self):
        return {
            "display_word": self.get_display_word(),
            "guessed_letters": self.guessed_letters,
            "chances_left": self.chances_left,
            "game_over": self.game_over,
            "win": self.win
        }

         
 