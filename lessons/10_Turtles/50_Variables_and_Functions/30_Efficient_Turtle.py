
"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

star = turtle.Turtle()                  # Create a turtle named tina

star.shape('turtle')                    # Set the shape of the turtle to a turtle
star.speed(0)                           # Make the turtle move as fast, but not too fast. 



     # Calculate angle from number of sides
    
    for i in range(5):                 # Loop through the number of sides
    star.forward(100)
    star.right(144)
                                  # Move tina forward by the forward distance
          

                                   # Turn tina left by the left turn

                        # Draw a square

...                                      # Move tina to another spot on the screen

                        # Draw a pentagon

...                                      # Move tina to another spot on the screen

        
      # Draw a hexagon

turtle.exitonclick()                     # Close the window when we click on it