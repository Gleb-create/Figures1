import turtle
from time import *


def drawSquare(myTurtle, x, y, size,angle = 0):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.setheading(90)
    myTurtle.left(angle)
    myTurtle.pendown()
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    print(myTurtle.pos())
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.right(90)
    myTurtle.forward(size)

def drawTriangle(myTurtle,x,y,cathetus,angle = 0):
    hypothenuse = (cathetus**2 + cathetus**2)**0.5
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.setheading(90)
    myTurtle.pendown()
    myTurtle.right(angle)
    myTurtle.right(45)
    myTurtle.forward(hypothenuse)
    myTurtle.left(135)
    myTurtle.forward(cathetus)
    myTurtle.left(90)
    myTurtle.forward(cathetus)




ada = turtle.Turtle()
drawSquare(ada, 35, 35, 50,30)
drawTriangle(ada,35,35,50)
drawTriangle(ada,78,60,60)
sleep(1000)
