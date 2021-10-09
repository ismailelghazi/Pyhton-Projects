from turtle import *
import random
turtle = Turtle()
turtle.shape("arrow")
turtle.color("red")

# count =

while not count > 2:
    number = [1,0]
    pos = random.choice(number)
    if pos==1:
        turtle.left(90)
        turtle.forward(50)
    else:
        turtle.right(90)
        turtle.forward(50)
    count+=1
done()
