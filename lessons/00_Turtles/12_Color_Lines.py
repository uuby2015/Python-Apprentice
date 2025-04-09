"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90
colors = [ 'red', 'blue', 'black', 'orange']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)
turtle.done()