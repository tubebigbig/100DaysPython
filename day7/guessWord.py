import random

WORD_LIST = ["apple", "paper", "glass"]


def get_word():
    word = random.choice(WORD_LIST)
    return word.upper()


def get_guess():
    return input("Guess a letter: ").upper()


def main():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(
            f"You have {lives} lives left and you have guessed: {' '.join(guessed_letters)}"
        )

        word_list = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        guess = get_guess()
        if guess in guessed_letters:
            print(f"You have already guessed {guess}")
            continue

        if guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
        else:
            lives -= 1

    if lives == 0:
        print(f"You died, the word was {word}")
    else:
        print(f"You guessed the word {word}!")


if __name__ == "__main__":
    main()
