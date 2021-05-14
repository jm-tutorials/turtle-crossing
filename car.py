from turtle import Turtle
import random

STRETCH_WIDTH = 1
STRETCH_LENGTH_MIN = 2
STRETCH_LENGTH_MAX = 3

class Car(Turtle):

    def __init__(self, color, position, heading):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.speed('fastest')
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=round(random.uniform(STRETCH_LENGTH_MIN,STRETCH_LENGTH_MAX),1))
        self.penup()
        self.color(color)
        self.goto(position)
        self.setheading(heading)
        self.showturtle()
        self.speed('normal')

    def move(self, distance):
        self.forward(distance)