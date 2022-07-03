import turtle


class baall(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.width =20
        self.height =20
        self.color("white")
        self.shape("circle")
    def move(self):
        self.speed(1)
        new_x=self.xcor()+1
        new_y=self.ycor()+1
        self.goto(new_x,new_y)