from turtle import *
import random
turtle = Turtle()
turtle.shape("arrow")
turtle.color("red")
color=["red", "bleu", "black","pink"]
turtle.color(random.choice(color))
for triangle in range(3):
    turtle.forward(100)
    turtle.left(-120)

for square in range(4):
        turtle.forward(100)
        turtle.right(90)
for pentagon in range(5):
    turtle.forward(100)
    turtle.right(72)
for regular_hexagon in range(6):
    turtle.forward(100)
    turtle.right(60)
for heptagon in range(7):
    turtle.forward(100)
    turtle.right(51)
for octagon in range(8):
    turtle.forward(100)
    turtle.right(45)
for nontagon in range(9):
    turtle.forward(100)
    turtle.right(40)
for nontagon in range(10):
    turtle.forward(100)
    turtle.right(36)
done()
#############2###############
