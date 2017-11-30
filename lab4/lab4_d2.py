'''Question 2 of Part D of lab 4 of CS 1.
Creates a canvas with four boxes at the corners'''

from tkinter import *

def draw_square(canvas, color, sideLength, center):
    '''Takes four arguments that describe how and where to draw a square:
    the canvas, the color, the length of a side, and the center position.
    The function draws the square in the canvas and
    returns the handle for the square'''
    return canvas.create_rectangle(center[0] - sideLength / 2,
    center[1] - sideLength / 2, center[0] + sideLength / 2,
    center[1] + sideLength / 2, fill=color, outline=color)

if __name__ == '__main__':
    '''Main method. Creates a canvas with four boxes at the corners'''
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    c.pack()
    redSquare = draw_square(c, 'red', 100, (50, 50))
    blueSquare = draw_square(c, 'blue', 100, (50, 750))
    yellowSquare = draw_square(c, 'yellow', 100, (750, 750))
    greenSquare = draw_square(c, 'green', 100, (750, 50))
    root.mainloop()
