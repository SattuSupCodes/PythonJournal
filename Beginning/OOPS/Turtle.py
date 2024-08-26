from turtle import *

red_turtle= Turtle()
red_turtle.color("red")

purple_turtle=Turtle()
purple_turtle.color("purple")

#  property must be linked to objects to work

red_turtle.speed=5
red_turtle.shape("turtle")
purple_turtle.forward(100)
purple_turtle.speed=5
red_turtle.left(120)
red_turtle.forward(100)
purple_turtle.forward(80)