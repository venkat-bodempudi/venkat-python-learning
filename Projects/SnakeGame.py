from turtle import Turtle,Screen

#set up screen
snakeScreen=Screen()
snakeScreen.screensize(500,500)
snakeScreen.bgcolor("black")
snakeScreen.title("My Snake Game")

Snake1=Turtle("square")
Snake1.color("White")

Snake2=Turtle("square")
Snake2.color("White")
Snake2.goto(-20,0)

Snake3=Turtle("square")
Snake3.color("White")
Snake3.goto(-40,0)

snakeScreen.exitonclick()