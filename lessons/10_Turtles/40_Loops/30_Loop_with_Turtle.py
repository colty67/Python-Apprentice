"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

... # Your code here
import turtle

turtle.setup(600,600,0,0)
tina=turtle.Turtle()



for i in range(7):
    tina.pensize(22)
    tina.color("red")
    tina.forward(0)
    tina.left(72)

turtle.exitonclick()