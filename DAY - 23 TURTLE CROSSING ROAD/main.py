import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

car_manager = CarManager()
player = Player() 
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    if player.is_it_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score()
        
screen.exitonclick()