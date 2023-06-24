from turtle import Screen
import time
from Snake import Snake
from Food import Food
#set up screen
snakeScreen=Screen()
snakeScreen.screensize(500,500)
snakeScreen.bgcolor("black")
snakeScreen.title("My Snake Game")
snakeScreen.tracer(0)
 
snake=Snake() 
food=Food()
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
    #Detect snake collision with food
    if snake.head.distance(food) < 10:
        food.RefreshFood()
    
snakeScreen.exitonclick()