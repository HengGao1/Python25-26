import turtle
bob = turtle.Turtle()
turtle.colormode(255)
from random import randint
turtle.bgcolor("black")
turtle.tracer(0)

def draw_spiral():
  bob.pencolor("red")
  for times in range(100):
    bob.forward(times*2)
    bob.left(91)
  bob.pencolor("orange")
  for times in range(100,200):
    bob.forward(times*2)
    bob.left(91)
  bob.pencolor("yellow")
  for times in range(200,300):
    bob.forward(times*2)
    bob.left(91)
  bob.pencolor("green")
  for times in range(300,400):
    bob.forward(times*2)
    bob.left(91)
  bob.pencolor("blue")
  for times in range(400,500):
    bob.forward(times*2)
    bob.left(91)
  bob.pencolor("purple")
  for times in range(500,600):
    bob.forward(times*2)
    bob.left(91)

