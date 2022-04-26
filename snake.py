
from turtle import Screen, Turtle

#Crear escenario

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600) # X, Y
screen.bgcolor( "black")
screen.title("Programate")

#ahora el cuerpo
positions = [(0,0),(-20, 0),(-40, 0)]

for position in positions:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.goto(position)

''''
snake_segment = Turtle("square")
snake_segment.color("white")

snake_segment2 = Turtle("square")
snake_segment2.color("white")
snake_segment2.goto(position)

snake_segment3 = Turtle("square")
snake_segment3.color("white")
snake_segment3.goto(position)
'''

screen.exitonclick()
