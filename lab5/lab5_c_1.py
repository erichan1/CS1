from tkinter import *
import random

# Graphics commands.

def drawCircle(x, y, diameter):
    '''
    Arguments - x, y, and diameter. All numbers.
    Action - Draws circle with center of circle w/ coordinates x and y with
    the given diameter
    '''

    circle = canvas.create_oval(x - diameter / 2, y - diameter / 2, x
    + diameter / 2, y + diameter / 2, outline = color, fill = color)
    circleList.append(circle)

def random_color():
    '''Takes no arguments. Returns a random color value that is recognized
    by tkinter package. Is of the form #RRGGBB. Values are in hexadecimal.'''

    color = ''
    hexaList = [0, 1, 2 , 3, 4, 5, 6 ,7 ,8 ,9, 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += str(random.choice(hexaList))
    return '#' + color

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''

    global color
    global circleList
    if(event.char == 'q'):
        root.quit()
    elif(event.char == 'c'):
        color = random_color()
    elif(event.char == 'x'):
        for circle in circleList:
            canvas.delete(circle)
        circleList = []

def button_handler(event):
    '''Handle left mouse button click events.'''

    drawCircle(event.x, event.y, random.randint(10, 50))


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    circleList = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
