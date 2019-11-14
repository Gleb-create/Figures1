import turtle
from time import *


def drawSquare(myTurtle, x, y, size,angle):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.left(angle)
    myTurtle.forward(size / 2)
    myTurtle.pendown()
    myTurtle.right(90)
    myTurtle.forward(size/2)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size/2)




ada = turtle.Turtle()
drawSquare(ada, 35, 35, 50,30)
sleep(1000)
