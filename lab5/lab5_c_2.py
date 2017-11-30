from tkinter import *
import math
import random

# Graphics commands.

def drawStar(x, y, radius, points):
    '''draws a star with coordinates at x,y,
    and with some radius and some number of points'''

    degreeList = []
    pointList = []
    for i in range(points):
        degreeList.append((-90 + 360 / points * i) / 180 * math.pi)
    for angle in degreeList:
        pointList.append((x+ math.cos(angle) * radius, y + math.sin(angle) * radius))
    for i in range(points):
        j = (i + 2 + int((points - 5) / 2)) % points
        k = (i + 3 + int((points - 5) / 2)) % points
        line1 = canvas.create_line(pointList[i][0], pointList[i][1], pointList[j][0], pointList[j][1], fill = color)
        line2 = canvas.create_line(pointList[i][0], pointList[i][1], pointList[k][0], pointList[k][1], fill = color)
        starLines.append(line1)
        starLines.append(line2)

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
    global starLines
    global points
    if(event.char == 'q'):
        root.quit()
    elif(event.char == 'c'):
        color = random_color()
    elif(event.char == 'x'):
        for line in starLines:
            canvas.delete(line)
        starLines = []
    elif(event.keysym == 'plus'):
        points += 2
    elif(event.keysym == 'minus'):
        if(points > 5):
            points -= 2

def button_handler(event):
    '''Handle left mouse button click events.'''

    drawStar(event.x, event.y, random.randint(50, 100), points)


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    starLines = []
    color = random_color()
    points = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
