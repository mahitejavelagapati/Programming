"""Hangman - console game (Task 1)
Uses words.txt (one word per line) if present, else a built-in list.
"""
import os
import random

MAX_MISTAKES = 6

FALLBACK_WORDS = [
    "python", "computer", "network", "software", "program", "system",
    "internet", "keyboard", "database", "project", "university",
    "education", "library", "science", "journey", "balance", "freedom",
    "package", "history", "teacher", "student", "monitor", "browser",
    "security", "research", "culture", "pattern", "digital", "mission",
]

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def load_words():
    """Load words from words.txt (same folder). Keep only 5-10 letter words."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            words = [w.strip().lower() for w in f]
        words = [w for w in words if w.isalpha() and 5 <= len(w) <= 10]
        if words:
            return words
    return FALLBACK_WORDS


def mask(word, guessed):
    return " ".join(c if c in guessed else "_" for c in word)


def show(word, guessed, wrong):
    print(STAGES[len(wrong)])
    print("\nWord:  ", mask(word, guessed))
    print("Wrong: ", " ".join(sorted(wrong)) or "-")
    print(f"Lives left: {MAX_MISTAKES - len(wrong)}\n")


def get_guess(guessed, wrong):
    while True:
        g = input("Guess a letter: ").strip().lower()
        if len(g) != 1 or not g.isalpha():
            print("Enter a single letter (a-z).")
        elif g in guessed or g in wrong:
            print(f"You already tried '{g}'. No penalty, try another.")
        else:
            return g


def play(words):
    word = random.choice(words)
    guessed, wrong = set(), set()

    print("\n=== HANGMAN ===")
    while len(wrong) < MAX_MISTAKES and not set(word) <= guessed:
        show(word, guessed, wrong)
        g = get_guess(guessed, wrong)
        if g in word:
            guessed.add(g)
            print(f"Nice! '{g}' is in the word.")
        else:
            wrong.add(g)
            print(f"Nope, '{g}' is not in the word.")

    show(word, guessed, wrong)
    if set(word) <= guessed:
        print("*" * 30)
        print("  YOU WON! The word was:", word.upper())
        print("*" * 30)
    else:
        print("#" * 30)
        print("  GAME OVER! The word was:", word.upper())
        print("#" * 30)


def main():
    words = load_words()
    while True:
        play(words)
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
