from cmu_112_graphics import *

from polygon import *
from line import *
from oval import *


def appStarted(app):
    app.polygon = Polygon()
    app.line = Line()
    app.status = 'Polygon'
    app.actions = [[]]

def keyPressed(app, event):
    if event.key == 'p':

        app.status = 'Line'
    elif event.key == 'g':
        app.status = 'Polygon'
    elif event.key == 'w':
        print(app.actions)
    elif event.key == 'z':
        undo(app)
    pass

def undo(app):
    #Edge case of nothing
    if app.actions == [[]]:
        return

    action = app.actions[-1]
    if action[0] == 'Line':
        app.line.undo()
    elif action[0] == 'Polygon':
        app.polygon.undo()
    app.actions.pop()


def mousePressed(app, event):
    #Adds an action to the history (WORKS FOR 2 CLICKS)
    if len(app.actions[-1])==2:
        app.actions[-1].append((event.x, event.y))
    else:
        app.actions.append([app.status, (event.x, event.y)])

    #Makes objects
    if app.status == 'Polygon':
        app.polygon.assignPoint(event.x, event.y)
    elif app.status == 'Line':
        app.line.assignPoint(event.x, event.y)

def mouseMoved(app, event):
    if app.status == 'Polygon':
        app.polygon.currentLocation = (event.x,event.y)
    elif app.status == 'Line':
        app.line.currentLocation=(event.x,event.y)

def redrawAll(app, canvas):
    app.polygon.draw(canvas)
    app.line.draw(canvas)

runApp(width=500,height=500)