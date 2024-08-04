import random
logo = """
          / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
         / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
        / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
        \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)
print("welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 101)

guess_correct = False
level = input("Type 'hard' for hard level, or type 'easy' for easy level.\n").lower()
attempt = 0

if level == "hard":
    attempt = 5
elif level == "easy":
    attempt = 10

while guess_correct == False:
    guess = int(input("Guess a number :\n"))
    if guess > random_number:
        print("Too high!")
    elif guess < random_number:
        print("Too Low!")
    if guess == random_number:
        guess_correct = True
        print(f"You guessed {guess} and that's correct number")
    else:
        attempt -= 1
        print(f"You have {attempt} attempts remaining to guess the number.")
    if attempt == 0:
        print("game over!")
        break