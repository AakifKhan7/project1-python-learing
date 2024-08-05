from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
ueser_bet = screen.textinput(title="make your bet" , prompt="which turtle will won the race ? Enter a color.")
color = ["red", "orange", "yellow","green", "blue", "purple"] 
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(-230, y_position[turtle_index])
    all_turtle.append(tim)
    
if ueser_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor()> 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == ueser_bet:
                print(f"You've won! The {turtle} turtle is winner.")
            else:
                print(f"You've lost! The {turtle} turtle is winner.")
        turtle.pendown()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        
screen.exitonclick()
