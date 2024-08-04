import random

scissors = '''
            ___________
        ---     ______ ) ______
                      __________ )
                ___________________)
                (________)
       ----.____(_______)
        '''

rock = '''
            ___________
        ---'     ______ )
                (_________)
                (_________)
                (________)
       ----.____(_______)
        '''

paper = '''
            ___________
        ---'     ______ ) _______
                      ___________)
                ___________________)
                _________________)
       ----.___________________)
        '''

game_image = [paper, scissors, rock]

print("welcom to Rock Paper Scissors.")
print("choose 0 for paper, 1 for Scissors, 2 for rock")
user_choice = int(input("Enter Your input : "))
computer_choice = random.randint(0, 2)
if user_choice > 2 or user_choice <0:
    print("input is not valid")
else:
    print(game_image[user_choice])
    print("Computer Choose : ")
    print(game_image[computer_choice])


if user_choice == 0 and computer_choice == 1:
    print("You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == computer_choice:
    print("Drow!")