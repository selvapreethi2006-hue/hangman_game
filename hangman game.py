import random

def hangman():
    # Predefined list of words
    word_list = ["python", "hangman", "computer", "programming", "developer"]
    secret_word = random.choice(word_list).lower()
    word_length = len(secret_word)

    # Game variables
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    print("You have 6 incorrect guesses allowed.")

    # Game loop
    while True:
        # Display current progress
        current_display = []
        for letter in secret_word:
            if letter in guessed_letters:
                current_display.append(letter)
            else:
                current_display.append("_")
        print("\nWord: " + " ".join(current_display))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print("You win!")
            break

        # Check loss condition
        if incorrect_guesses >= max_incorrect:
            print(f"\nSorry, you've run out of guesses. The word was: {secret_word}")
            print("Better luck next time!")
            break

        # Get player's guess
        guess = input("\nGuess a letter: ").strip().lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        # Add to guessed letters
        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. {max_incorrect - incorrect_guesses} incorrect guesses remaining.")

if __name__ == "__main__":
    hangman()