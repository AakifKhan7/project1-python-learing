from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwerd():
    tim.forward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def move_backword():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key ="w", fun=move_forwerd)
screen.onkey(key ="s", fun=move_backword)
screen.onkey(key ="a", fun=move_left)
screen.onkey(key ="d", fun=move_right)
screen.onkey(key ="c", fun=clear)
screen.exitonclick()