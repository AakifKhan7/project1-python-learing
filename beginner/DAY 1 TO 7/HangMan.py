import hangman_word
import hangman_art

blanks = []
lives = 6

import random

print(hangman_art.logo)

choosen_word = random.choice(hangman_word.word_list)
len_choosen_word = len(choosen_word)
print(f"random number is {choosen_word} ")
for _ in range(len_choosen_word):
    blanks += "_"
print(f"{' '.join(blanks)}")

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter : ").lower()
    len_guess = len(guess)
    
    if guess in blanks:
        print(f"You've already guessed a letter {guess} ")
    for position in range(len_choosen_word):
        letter = choosen_word[position]
        if letter == guess:
            blanks[position] = letter

    print(f"{' '.join(blanks)}")

    if not guess in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in word. You lose one life. ")
    if lives == 0:
        print("You Lose!")
        end_of_game = True
    if not "_" in blanks:
        end_of_game = True
        print("You Win!")

    print(hangman_art.stages[lives])