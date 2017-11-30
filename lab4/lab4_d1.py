'''Question 1 of Part D of lab 4 of CS 1.
Creates a canvas with four boxes at the corners'''

from tkinter import *
root = Tk()
root.geometry('800x800')
c = Canvas(root, width=800, height=800)
c.pack()
redSquare = c.create_rectangle(0, 0, 100, 100, fill='red', outline='red')
blueSquare = c.create_rectangle(0, 700, 100, 800, fill='blue', outline='blue')
yellowSquare = c.create_rectangle(700, 700, 800, 800, fill='yellow', outline='yellow')
greenSquare = c.create_rectangle(700, 0, 800, 100, fill='green', outline='green')
root.mainloop()
