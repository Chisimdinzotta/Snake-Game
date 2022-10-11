from turtle import Turtle

POSITION = "center"
FONT = ("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        # To get it to go up instead of it to be at the centre of the screen
        self.goto(0, 270)
        self.update_score()
        #The score shows and so does a turtle thing. To remove that
        self.hideturtle()

    def update_score(self):
        self.write(arg=(f"score = {self.score}"), align=POSITION, font=FONT)

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=("Game over!"), align=POSITION, font=("Courier", 20, "normal"))