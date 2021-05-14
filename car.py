from turtle import Turtle
import random

STRETCH_WIDTH = 1
STRETCH_LENGTH_MIN = 2
STRETCH_LENGTH_MAX = 3
STRETCH_LENGTH = round(random.uniform(STRETCH_LENGTH_MIN,STRETCH_LENGTH_MAX),1)

class Car(Turtle):

    

    def __init__(self, color, position, heading):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.speed('fastest')
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.penup()
        self.color(color)
        self.goto(position)
        self.setheading(heading)
        self.showturtle()
        self.speed('normal')

    def move(self, distance):
        self.forward(distance)

    def xRange(self):
        hLength = (20*STRETCH_LENGTH)/2
        return (self.xcor()-hLength,self.xcor()+hLength)
    
    def xCollision(self,turtle):
        xr = self.xRange()
        return turtle.xcor() >= xr[0] and turtle.xcor() <= xr[1]
    