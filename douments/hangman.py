import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess!")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
