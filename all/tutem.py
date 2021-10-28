from turtle import *

ism = Turtle()
isd = Screen()


def z():
    ism.forward(100)
def q():
    ism.left(45)
    ism.heading()
def s():
    ism.backward(100)
def d():
    ism.right(45)
    ism.heading()
def clear():
    ism.clear()
    ism.penup()
    ism.home()

isd.listen()
isd.onkey(key="z", fun=z)
isd.onkey(key="q", fun=q)
isd.onkey(key="s", fun=s)
isd.onkey(key="d", fun=d)
isd.onkey(key="space", fun=clear)
isd.exitonclick()
