from turtle import Turtle, Screen
import random

screen = Screen() 
random_walk = random.randint(5, 10)
red = Turtle()
red.color("red")
red.speed("slow")
red.goto(-150, 0)
blue = Turtle()
blue.color("blue")
blue.speed("slow")
for i in range(500):
    red.forward(random_walk)

# blue = Turtle()
# blue.color("blue")

# def random_Walk():
#     global red
#     r_walk = red.forward(random.randint(5, 10))
#     return r_walk

screen.exitonclick()
# random_Walk()