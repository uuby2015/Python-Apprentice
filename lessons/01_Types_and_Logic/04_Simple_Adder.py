"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for wha modult you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""








# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import requiredes
# Create a window object
window = Tk()     # Create a window object
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   r
number1  = simpledialog.askinteger("", 'enter a number') 
# Ask the user for the second number
number2= simpledialog.askinteger("", 'enter another number')
# Display the sum of the two numbers 
messagebox.showinfo('numbr1+number2')
# Keep the window open
window.mainloop()  # Keeps the window open
