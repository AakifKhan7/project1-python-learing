from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-240, 260)
        self.color("black")
        self.write(f"level: {self.level}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    
    def score(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", align="center", font=("Arial", 20, "normal"))