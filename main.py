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
    myTurtle.right(135)
    myTurtle.forward(cathetus)
    myTurtle.right(90)
    myTurtle.forward(cathetus)

def drawParallelogram(myTurtle,x,y,shortside,longside,angle = 0):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.setheading(90)
    myTurtle.pendown()
    myTurtle.right(angle)
    myTurtle.right(45)
    myTurtle.forward(shortside)
    myTurtle.right(135)
    myTurtle.forward(longside)
    myTurtle.right(45)
    myTurtle.forward(shortside)
    myTurtle.right(135)
    myTurtle.forward(longside)

ada = turtle.Turtle()
drawSquare(ada, 35, 35, 50,30)
drawTriangle(ada,60,60,50)
drawTriangle(ada,70,70,60)
drawParallelogram(ada,50,50,30,60)
sleep(1000)
