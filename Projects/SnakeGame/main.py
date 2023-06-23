from turtle import Turtle,Screen
import time
from Snake import Snake
#set up screen
snakeScreen=Screen()
snakeScreen.screensize(500,500)
snakeScreen.bgcolor("black")
snakeScreen.title("My Snake Game")
snakeScreen.tracer(0)
 
snake=Snake() 

snakeScreen.listen()
snakeScreen.onkey(snake.Up,"Up")
snakeScreen.onkey(snake.Down,"Down")
snakeScreen.onkey(snake.Left,"Left")
snakeScreen.onkey(snake.Right,"Right")

is_game_on=True

while is_game_on:
    snakeScreen.update()  
    time.sleep(0.1)
    snake.MoveSnake()

    
snakeScreen.exitonclick()