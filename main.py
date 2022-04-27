
from turtle import Screen
from snake import Snake
from food import Food  
import time

#Crear escenario

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600) # X, Y
screen.bgcolor( "black")
screen.title("Programate")

screen.tracer(0)#se quita animacion de cuadro x cuadro

#crear el objeto serpiente -instanciar-
snake = Snake()
food= Food()#instanciar comida

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


screen.exitonclick()