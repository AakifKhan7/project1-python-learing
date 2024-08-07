from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))