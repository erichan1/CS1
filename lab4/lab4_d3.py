'''Question 3 of Part D of lab 4 of CS 1.
Creates a canvas with fifty boxes with random colors, sizes and positions'''

from tkinter import *
import random

def draw_square(canvas, color, sideLength, center):
    '''Takes four arguments that describe how and where to draw a square:
    the canvas, the color, the length of a side, and the center position.
    The function draws the square in the canvas and
    returns the handle for the square'''
    return canvas.create_rectangle(center[0] - sideLength / 2,
    center[1] - sideLength / 2, center[0] + sideLength / 2,
    center[1] + sideLength / 2, fill=color, outline=color)

def random_size(a, b):
    '''Takes two even integers as arguments and returns
    a random even integer greater than the first arg and smaller than the
    second'''
    assert a > 0 and b > 0 and a % 2 == 0 and b % 2 == 0 and a < b
    output = random.randint(a/2, b/2)*2
    assert output % 2 == 0
    return output

def random_position(max_x, max_y):
    '''Takes two integers as arguments, a max X and Y, and returns a tuple of
    two randomly chosen x and y coordinates that are smaller than max_x and
    max_y, respectively, but both greater than zero.'''
    assert max_x >= 0 and max_y >= 0
    return (random.randint(0, max_x), random.randint(0, max_y))

def random_color():
    '''Takes no arguments. Returns a random color value that is recognized
    by tkinter package. Is of the form #RRGGBB. Values are in hexadecimal.'''
    color = ''
    hexaList = [0, 1, 2 , 3, 4, 5, 6 ,7 ,8 ,9, 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += str(random.choice(hexaList))
    return '#' + color

if __name__ == '__main__':
    '''Main method. Creates a canvas and places fifty boxes in it with random
    colors, sizes, and positions'''
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    c.pack()

    for i in range(50):
        draw_square(c, random_color(), random_size(20, 150),
        random_position(800, 800))

    root.bind('<q>', quit)
    root.mainloop()
