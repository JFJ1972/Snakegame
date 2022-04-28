from msilib.schema import Font
from turtle import Turtle

ALIGN = "center"
FONT  =  ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("red")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Tu Puntaje:{self.score}", font=FONT, align=ALIGN )    
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Ups..chocaste! Fin del Juego.", font=FONT, align=ALIGN )