# Step 1
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
print("Welcome to the Hangman Game!\n\n")




gameOn = 'y'

while gameOn == 'y':
    chosen_word = random.choice(word_list)
    lives = len(stages) - 1
    currWord = '_' * len(chosen_word)
    while lives >= 0:
        guess = input("Guess a letter: ").lower()

        contains = False
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                contains = True
                l = list(currWord)
                l[i] = guess
                currWord = ''.join(l)

        if (not contains):
            print(stages[lives])
            print(f"You guessed {guess}, that's not in the word.You lose a life")
            print(currWord)
            lives -= 1
        else:
            print(currWord)

        if (currWord == chosen_word):
            print("You win!")
            break

    if lives < 0:
        print(f"Game Over. You lose! The word was {chosen_word}")

    gameOn = input("Do you want to play another game? y or n\n")

