from turtle import *

ism = Turtle()
isd = Screen()


def move_():
    ism.forward(100)
    ism.forward(-90)


isd.listen()
isd.onkey(key="space", fun=move_)
isd.exitonclick()
