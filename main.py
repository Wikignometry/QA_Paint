from cmu_112_graphics import *
from polygon import *
from line import *
from oval import *
from helpers import *

def appStarted(app):
    app.status = 'Polygon'
    app.objects = []

def keyPressed(app, event):
    if event.key == 'l':
        app.status = 'Line'
    elif event.key == 'p':
        app.status = 'Polygon'
    elif event.key == 'o':
        app.status = 'Oval'
    elif event.key == 'w':
        print(app.objects)
        
    elif event.key == 'z':
        undo(app)

def mousePressed(app, event):   
    if app.status == 'Line':
        app.objects.append(Line(event.x, event.y))
    elif app.status == 'Polygon':
        app.objects.append(Polygon(event.x, event.y))
    elif app.status == 'Oval':
        app.objects.append(Oval(event.x, event.y))

def mouseDragged(app, event):
    app.objects[-1].currentLocation = (event.x, event.y)


def mouseReleased(app, event):
    if len(app.objects) > 0:
        app.objects[-1].assignPoints(event.x, event.y)

def undo(app):
    if app.objects == []:
        return
    app.objects.pop()


def redrawAll(app, canvas):
    for object in app.objects:
        object.draw(canvas)

runApp(width=500,height=500)