import turtle
from random import randint
bob = turtle.Turtle()
turtle.bgcolor("black")
bob.speed(0)
bob.pensize(2)
# second drawing: flower burst
bob.penup()
bob.goto(0,0)
bob.pendown()
turtle.tracer(0)
bob.pensize(2)


def draw_spiral():
    bob.pencolor("red")
    for times in range(100):
        bob.forward(times * 2)
        bob.left(91)
    bob.pencolor("orange")
    for times in range(100, 200):
        bob.forward(times * 2)
        bob.left(91)
    bob.pencolor("yellow")
    for times in range(200, 300):
        bob.forward(times * 2)
        bob.left(91)
    bob.pencolor("green")
    for times in range(300, 400):
        bob.forward(times * 2)
        bob.left(91)
    bob.pencolor("blue")
    for times in range(400, 500):
        bob.forward(times * 2)
        bob.left(91)
    bob.pencolor("purple")
    for times in range(500, 600):
        bob.forward(times * 2)
        bob.left(91)

def draw_star():        
    for times in range(100):
        bob.penup()
        bob.goto(randint(-400,400), randint(-400,400))
        bob.pendown()

        bob.pencolor("white")
        bob.pensize(1)

        for times in range(5):
            bob.forward(27)
            bob.right(144)


