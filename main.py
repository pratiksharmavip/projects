# screen

from tkinter import N
from turtle import *
import turtle
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)

# paddel_1
paddel_1=Turtle()
paddel_1.speed("fastest")
paddel_1.hideturtle()
paddel_1.color('white')
paddel_1.shape("square")
paddel_1.shapesize(5,1)
paddel_1.penup()
paddel_1.goto(380,0)
paddel_1.showturtle()

def go_up():
    newx=(paddel_1.ycor()+20)
    paddel_1.goto(paddel_1.xcor(),newx)
def go_dn():
    newx=(paddel_1.ycor()-20)
    paddel_1.goto(paddel_1.xcor(),newx)
turtle.listen()
onkeypress(go_up,"Up")
turtle.listen()
onkeypress(go_dn,"Down")
screen.exitonclick()