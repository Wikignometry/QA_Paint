from button import *

def makePolygonButtons(app):
    buttons = []
    polygonButtonActions={'thickness':getPolygonThickness, 'color':getPolygonFill, 'outline':getPolygonOutline}

    y = 50
    x = 100
    for label in polygonButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='light grey', action=polygonButtonActions[label]))
        x += 90
    return buttons

def getPolygonThickness(app):
    app.polygonThickness = int(app.getUserInput('input your polygon thickness here'))

def getPolygonFill(app):
    app.polygonFill = app.userInput('input your polygon color here')

def getPolygonOutline(app):
    app.polygonOutline = app.userInput('input your polygon outline color here')