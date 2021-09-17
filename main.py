# IMPORT THE MODULE
import turtle
from turtle import Screen

s = Screen()
s.bgcolor('black')
#-------------------------> Created a turtle object
a = turtle.Turtle()
a.shape('arrow')
a.pensize(10)
a.color('blue')
#––––––––––––––––> Created blue cicrcle
a.begin_fill()
a.circle(160, 360)
a.end_fill()
#  --------------->Started to create letter "J"
a.color('blue')
a.penup()
a.left(90)
a.forward(250)
a.right(90)
a.pendown()
#  --------------->"J"
a.color('white')
a.pensize(10)
a.begin_fill()
a.forward(100)
a.backward(200)
a.forward(100)
a.right(90)
a.forward(120)
a.circle(-60,200)

a.hideturtle()
turtle.done()