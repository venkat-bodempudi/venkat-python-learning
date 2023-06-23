from turtle import Turtle

INITIAL_SNAKE_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_SNAKE_EXTENT=20
UP=90
DOWN=270
LEFT=180
RIGHT=0




class Snake:

    def __init__(self) -> None:
        self.snakes=[]
        self.CreateSnake()
        self.head=self.snakes[0]
    
    def CreateSnake(self):
        for snake_position in INITIAL_SNAKE_POSITIONS:
            snake=Turtle("square")
            snake.color("White")
            snake.penup()
            snake.goto(snake_position)
            self.snakes.append(snake)

    def MoveSnake(self):
        for snake_index in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[snake_index-1].xcor()
            new_y=self.snakes[snake_index-1].ycor()
            self.snakes[snake_index].goto(new_x,new_y)
        self.head.forward(MOVE_SNAKE_EXTENT)
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
