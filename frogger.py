from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Frogger(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.spawn() 

    def spawn(self):
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def left(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)

    def right(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)