from turtle import *
from types import new_class


class Paddel(Turtle,):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        

    