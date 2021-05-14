from turtle import Turtle

FINISH_LINE_Y = 260
ALIGNMENT = "center"
FONT1 = ("Courier", 20, "normal")
FONT2 = ("Courier", 48, "bold") 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 5
        self.stamps = []
        self.game_is_on = True
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(stretch_len=0.25, stretch_wid=0.25)
        self.setheading(90)
        self.penup()
        self.updateScoreboard()
            
    def updateScoreboard(self):
        self.goto(-240, 260)
        self.write("Level: {}".format(self.level), align=ALIGNMENT, font=FONT1)
        self.goto(200, 260)
        self.write("Lives: ", align=ALIGNMENT, font=FONT1)
        self.goto(self.xcor()+10,self.ycor())       
        for _ in range(self.lives-1):
            stamp = self.stamp()
            self.stamps.append(stamp)
            self.goto(self.xcor()+10, self.ycor())

    def nextLevel(self):
        self.level += 1
        self.clear()
        self.updateScoreboard()

    def die(self):
        self.lives -= 1
        if self.lives == 0:
            self.game_is_on = False
            self.gameOver()
        else:
            self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)