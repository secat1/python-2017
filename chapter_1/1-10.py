# Exercise 1.10

import turtle

# Moves turtle pointer to start position
# Sets pointer facing south
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.right(90)

# Prints the first line
turtle.left(18)
turtle.forward(100)

# Loop to print the next 4 lines
for i in range(4):
    
    # Sets the turtle pointer to point inwards
    turtle.right(180)
    
    # Prints next 4 lines
    turtle.left(36)
    turtle.forward(100)

# Pauses the turtle graphic screen 
turtle.done()
 
