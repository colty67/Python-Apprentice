"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(500)                           # Make the turtle move as fast, but not too fast. 

for i in range(5000):
    tina.forward(150)                       # Move tina forward by the forward distancetina.left(90)
    tina.left(90)                           # Turn tina left by the left turn

                       # Continue the last two steps three more times

turtle.exitonclick()                    # Close the window when we click on it