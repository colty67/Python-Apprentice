"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0.1)                           # Make the turtle move as fast, but not too fast. 

                                   # Turn tina left by the left turn
tina.begin_fill()
tina.circle(100)
tina.color("blue")
tina.end_fill()
tina.penup()
tina.goto(0,67)     
tina.pendown()
tina.begin_fill()
tina.circle(50)
tina.color("red")
tina.end_fill()
tina.goto(0,80)     
tina.pendown()
tina.begin_fill()
tina.circle(25)
tina.color("black")
tina.end_fill()


                       # Continue the last two steps three more times

turtle.exitonclick()                    # Close the window when we click on i