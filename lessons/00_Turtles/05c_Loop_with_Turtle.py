
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""


import turtle                           
turtle.setup (width=600, height=600)    

tina = turtle.Turtle() 
for i in range(5):
    tina.forward(100)
    tina.right(72)
