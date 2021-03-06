
from turtle import Screen
from snake import Snake
from food import Food  
import time
from scoreboard import Scoreboard
#Crear escenario

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600) # X, Y
screen.bgcolor( "black")
screen.title("Programate")

screen.tracer(0)#se quita animacion de cuadro x cuadro

#crear el objeto serpiente -instanciar-
snake = Snake()
food= Food()#instanciar comida
scoreboard= Scoreboard()

#movimiento
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")     
screen.onkey(snake.left,"Left")     
screen.onkey(snake.right,"Right")     

game_is_on = True

while game_is_on:   
    screen.update()#refresca la pantalla para que se vean los cuadros continuos
    time.sleep(0.2)#tiempo de movimiento
    snake.move()

#detectar colision
    if snake.head.distance(food) < 15:
        food.refresh() 
        scoreboard.increase_score()
        snake.extend()

#colision con paredes
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over() 

#Detectar la colision de la cola 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()