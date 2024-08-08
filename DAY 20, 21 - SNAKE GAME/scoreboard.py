from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./DAY 20, 21 - SNAKE GAME/data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./DAY 20, 21 - SNAKE GAME/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()