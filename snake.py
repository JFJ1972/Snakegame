from hashlib import new
from turtle import Screen, Turtle, pen, penup
import time

#Crear escenario

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600) # X, Y
screen.bgcolor( "black")
screen.title("Programate")

screen.tracer(0)#se quita animacion de cuadro x cuadro

#ahora el cuerpo
starting_positions = [(0,0),(-20, 0),(-40, 0)]

segments = []

for position in starting_positions:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()#quita la linea
    snake_segment.goto(position)
    segments.append(snake_segment)

game_is_on = True

while game_is_on:   
    screen.update()#refresca la pantalla para que se vean los cuadros continuos
    time.sleep(0.2)#tiempo de movimiento

    '''
            for segment in segments:
        segment.forward(20)
    '''
    for seg_num in range(len(segments) - 1, 0, -1 ):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90) 




'''
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
