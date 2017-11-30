'''
lab3c.py
Simple L-system simulator.
'''

# References:
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ----------------------------------------------------------------------
# Example L-systems.
# ----------------------------------------------------------------------

# Koch snowflake.
koch = { 'start' : 'F++F++F',
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1',
              '+' : 'R 60',
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A',
             'A'     : '-BF+AFA+FB-' ,
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1',
                 '-' : 'L 90',
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G',
               'F'     : 'F-G+F+G-F',
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1',
                    'G' : 'F 1',
                    '+' : 'L 120',
                    '-' : 'R 120' }

# ----------------------------------------------------------------------
# L-systems functions.
# ----------------------------------------------------------------------

def update(lsys, s):
    '''Takes two arguments:
    1. a dictionary, which specifies both the starting string and the
    update rules for a particular L-system
    (like the koch dictionary described above) and 2. an L-system string.
    Generates the next version of the L-system string by applying
    the L-system rules to each character of the string
    and combining all the strings into one big string.
    Any character which is not a key in the L-system dictionary
    should be copied into the new string unchanged.'''
    updatedStr = ''
    keys = lsys.keys()
    for c in s:
        if(c in keys):
            updatedStr += lsys[c]
        else:
            updatedStr += c
    return updatedStr

def iterate(lsys, n):
    '''Takes two arguments:
    1. an L-system dictionary as described in the previous problem.
    2. an integer n which should be 0 or greater.
    Returns the string which results from starting
    with the starting string for that L-system and updating n times.'''
    finalStr = lsys['start']
    for i in range(n):
        finalStr = update(lsys, finalStr)
    return finalStr


def lsystemToDrawingCommands(draw, s):
    '''Takes two arguments:
    1. a dictionary whose keys are characters in L-system strings
    and whose values are drawing commands (like koch_draw above)
    2. an L-system string
    Returns list of drawing commands needed to draw the figure
    corresponding to the L-system string.'''
    drawList = []
    keys = draw.keys()
    for c in s:
        if(c in keys):
            drawList.append(draw[c])
    return drawList


def bounds(cmds):
    '''Takes one argument: a list of commands
    such as those generated by lsystemToDrawingCommands.
    Returns bounding coordinates of the sequence of drawing commands.
    Returns a tuple of the (xmin, xmax, ymin, ymax) coordinates.
    Coords are floats'''
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    currentLoc = (0, 0, 0)
    for cmd in cmds:
        currentLoc = nextLocation(currentLoc[0], currentLoc[1], currentLoc[2], cmd)
        if(currentLoc[0] < minX):
            minX = currentLoc[0]
        if(currentLoc[0] > maxX):
            maxX = currentLoc[0]
        if(currentLoc[1] < minY):
            minY = currentLoc[1]
        if(currentLoc[1] > maxY):
            maxY = currentLoc[1]
    return (minX, maxX, minY, maxY)

def nextLocation(x, y, angle, cmd):
    '''Takes four arguments:
    1. the current x coordinate value of the turtle
    2. the current y coordinate value of the turtle
    3. the current direction (angle from the horizontal) the turtle is facing
    4. a drawing command, like 'F 1' or 'L 60'
    Returns a tuple with the next location and direction of the turtle'''
    cmdLst = cmd.split()
    if(cmdLst[0] == 'F'):
        return (x + int(cmdLst[1]) * math.cos(angle * math.pi / 180),
        y + int(cmdLst[1]) * math.sin(angle * math.pi / 180), angle)
    elif(cmdLst[0] == 'L'):
        return (x, y, (angle + int(cmdLst[1])) % 360)
    else:
        return (x, y, (angle - int(cmdLst[1])) % 360)

def saveDrawing(filename, bounds, cmds):
    '''takes three arguments:
    1. a filename to write to
    2. the bounds of the resulting drawing.
    3. a list of drawing commands
    This function will write this information to the
    file corresponding to the given filename by first writing
    the bounds information on a single line,
    and then by writing the drawing commands to the file, one per line.'''
    newFile = open(filename, 'w')
    fileContent = '{} {} {} {}\n'.format(bounds[0],bounds[1],bounds[2], bounds[3])
    for cmd in cmds:
        fileContent += '{}\n'.format(cmd)
    newFile.write(fileContent)
    newFile.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
