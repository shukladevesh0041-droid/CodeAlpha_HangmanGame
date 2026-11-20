
import random

# Predefined list of five words
words = ["PYTHON", "COMPUTER", "PROGRAM", "KEYBOARD", "CODING"]

# Main game function
def play_game():

    # Select a random word
    secret_word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6

    print("\n================================")
    print("       HANGMAN GAME")
    print("================================")
    print("Guess the hidden word!")
    print("You have only 6 wrong guesses.")

    # Game loop
    while wrong_guesses < max_guesses:

        # Display guessed and hidden letters
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_guesses)

        # Check winning condition
        if "_" not in display_word:
            print("\nCongratulations! You Won!")
            break

        # Get letter from player
        guess = input("Enter a letter: ").strip().upper()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet!")
            continue

        # Check repeated letter
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        # Store guessed letter
        guessed_letters.append(guess)

        # Check answer
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    # Losing condition
    if wrong_guesses == max_guesses:
        print("\nGAME OVER!")
        print("The correct word was:", secret_word)


# Main program
while True:

    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for playing!")
        print("Goodbye!")
        break
