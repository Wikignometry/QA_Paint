from cmu_112_graphics import *

from polygon import *
from line import *
from oval import *


def appStarted(app):
    app.polygon = Polygon()
    app.line = Line()
    app.oval = Oval()
    app.status = 'Polygon'
    app.actions = [[]]
    app.history = []

def keyPressed(app, event):
    if event.key == 'l':
        app.status = 'Line'
    elif event.key == 'p':
        app.status = 'Polygon'
    elif event.key == 'o':
        app.status = 'Oval'
    
    elif event.key == 'w':
        print(app.history)
    elif event.key == 'z':
        undo(app)
    pass

def undo(app):
    #Edge case of nothing
    # if app.actions == [[]]:
    #     return
    
    if app.history == []:
        return

    # action = app.actions[-1]
    # if action[0] == 'Line':
    #     app.line.undo()
    # elif action[0] == 'Polygon':
    #     app.polygon.undo()
    # elif action[0] == 'Oval':
    #     app.oval.undo()
    
    last = app.history[-1]
    if last == 'Line':
        app.line.undo()
    elif last == 'Polygon':
        app.polygon.undo()
    elif last == 'Oval':
        app.oval.undo()

    app.history.pop()

def mousePressed(app, event):
    # #Adds an action to the history (WORKS FOR 2 CLICKS)
    # if len(app.actions[-1])==2:
    #     app.actions[-1].append((event.x, event.y))
    # else:
    #     app.actions.append([app.status, (event.x, event.y)])

    #Makes objects
    if app.status == 'Polygon':
        app.polygon.assignPoint(event.x, event.y)
        if app.polygon.status == 1:
            app.history.append('Polygon')
            
    elif app.status == 'Line':
        app.line.assignPoint(event.x, event.y)
        if app.line.status == 1:
            app.history.append('Line')
    
    elif app.status == 'Oval':
        app.oval.assignPoint(event.x, event.y)
        if app.oval.status == 1:
            app.history.append('Oval')

def mouseMoved(app, event):
    if app.status == 'Polygon':
        app.polygon.currentLocation = (event.x,event.y)
    elif app.status == 'Line':
        app.line.currentLocation=(event.x,event.y)
    elif app.status == 'Oval':
        app.oval.currentLocation=(event.x,event.y)

def redrawAll(app, canvas):
    app.polygon.draw(canvas)
    app.line.draw(canvas)
    app.oval.draw(canvas)

runApp(width=500,height=500)