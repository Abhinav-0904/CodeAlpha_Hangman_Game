import random
import time
words = ['panda', 'pizza', 'junks', 'mouse', 'phone']
word = random.choice(words)
guessed_word = ['_'] * len(word)
attempts_left = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word! You have 6 wrong attempts.\n")

while attempts_left > 0 and '_' in guessed_word:
    print("Word:", ' '.join(guessed_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    print("Attempts left:", attempts_left)

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print("Wrong guess!\n")

if '_' not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)

time.sleep(2)
