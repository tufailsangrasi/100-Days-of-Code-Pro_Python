# Turtle Graphic and Tuples
# If we just import the module without import its class the object will be created like timmy=turtle.Turtle()
# from turtle import * has some disadvantages
# Working with alises import turtle as t
# Python 2 vs Python 3
# In Virtual environment we setup the python
from turtle import Turtle , Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("black")

# We can also used for loop as well
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
for _ in range(13):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()



screen = Screen()
screen.exitonclick()
