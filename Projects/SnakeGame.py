from turtle import Turtle,Screen
import time
#set up screen
snakeScreen=Screen()
snakeScreen.screensize(500,500)
snakeScreen.bgcolor("black")
snakeScreen.title("My Snake Game")
snakeScreen.tracer(0)
snakes=[]

initial_snake_positions=[(0,0),(-20,0),(-40,0)]

for snake_position in initial_snake_positions:
    snake=Turtle("square")
    snake.color("White")
    snake.penup()
    snake.goto(snake_position)
    snakes.append(snake)
 
is_game_completed=True
while is_game_completed:
    snakeScreen.update()  
    time.sleep(0.1)

    for snake_index in range(len(snakes)-1,0,-1):
        new_x=snakes[snake_index-1].xcor()
        new_y=snakes[snake_index-1].ycor()
        snakes[snake_index].goto(new_x,new_y)
    snakes[0].forward(20)
    


snakeScreen.exitonclick()