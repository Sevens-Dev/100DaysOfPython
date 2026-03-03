import random
import hangman_words
from hangman_art import game_start, stages

game_start()

game_over = False

game_word = random.choice(hangman_words.possible_words)
word_length = len(game_word)

placeholder = "_" * word_length
print(placeholder)

current_stage = stages[0]
index = 0

correct_letters = []
guessed_letters = []

while not game_over:
    display = ""
    user_guess = input("Enter your guess: ").lower()
    if user_guess in guessed_letters:
        print("You already guessed this letter")
    else:
        for letter in game_word:
            if letter == user_guess:
                display += user_guess
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        if user_guess not in game_word:
            guessed_letters.append(user_guess)
            index += 1
            current_stage = stages[index]
            if index == 6:
                game_over = True
                print("**********"
                      "*You lose*"
                      "**********")
        if "_" not in display:
            game_over = True
            print('''
                  ___________
                  | You win |
                  -----------''')

    print(display)
    print(current_stage)

