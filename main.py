
from turtle import Screen
import time
#from numpy import linspace
import random

from frogger import Frogger
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 270

screen_width = 600
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.title("Frogger, but a turtle... Turtler")

frogger = Frogger()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(frogger.up,"Up")
screen.onkey(frogger.down,"Down")
screen.onkey(frogger.left,"Left")
screen.onkey(frogger.right,"Right")

while scoreboard.game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # Detect crossing the finish line, level pass
    if frogger.ycor() > FINISH_LINE_Y:
        scoreboard.nextLevel()
        frogger.spawn()
        car_manager.resetCars()

    # Detect collision with car
    for car in car_manager.cars:
        if frogger.distance(car) < 10:
            scoreboard.die()
            frogger.spawn()
    
    # Detect car moving off screen

screen.exitonclick()