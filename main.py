
from wordlist import get_random_word
from logic import HangmanGame

def start_new_game(category=None, difficulty=None, max_chances=6):
    word = get_random_word(category, difficulty)
    game = HangmanGame(word, max_chances)
    return game

def main():
    print("Welcome to Hangman!")
    
    category = input("Choose category (fruits/animals/countries or leave blank for random): ").strip().lower()
    difficulty = input("Choose difficulty (easy/medium/hard or leave blank for random): ").strip().lower()

    game = start_new_game(category if category else None, difficulty if difficulty else None)
    
    while not game.game_over:
        print("\nWord:", game.get_display_word())
        print("Guessed letters:", ", ".join(game.guessed_letters))
        print("Chances left:", game.chances_left)

        guess = input("Enter a letter: ").strip().lower()
        result = game.guess_letter(guess)
        print(result)

    if game.win:
        print("\nCongratulations! You guessed the word:", game.word)
    else:
        print("\nGame over! The word was:", game.word)

if __name__ == "__main__":
    main()
