from random import random
from turtle import Turtle
import random



class Food(Turtle):
    
    def __init__(self):
        super().__init__() #indica que se toma todo lo heredado desde turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.3)
        self.color("yellow")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)