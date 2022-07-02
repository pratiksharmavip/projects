# screen
from paddel import *
from turtle import *
import turtle
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)

# paddel_1
screen.tracer(0)
paddel_1=Paddel((380,0))
paddel_2=Paddel((-380,0))



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


def go_up_1():
    newx=(paddel_2.ycor()+20)
    paddel_2.goto(paddel_2.xcor(),newx)
def go_dn_1():
    newx=(paddel_2.ycor()-20)
    paddel_2.goto(paddel_2.xcor(),newx)
turtle.listen()
onkeypress(go_up_1,"w")
turtle.listen()
onkeypress(go_dn_1,"s")
game=1
while game==1:
    screen.update()

screen.exitonclick()