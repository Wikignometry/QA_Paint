from button import *

def makeNGonButtons(app):
    buttons = []
    nGonButtonActions ={'outline\nthickness':getNGonThickness, 'fill':getNGonFill, 'outline\ncolor':getNGonOutline, 'sides':getNGonSides}
    
    y = 30
    x = 100
    for label in nGonButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='light grey', action=nGonButtonActions[label]))
        x += 90
    return buttons

def getNGonThickness(app):
    app.polygonOutlineThickness = int(app.getUserInput('input your nGon thickness here'))

def getNGonFill(app):
    app.polygonFill = app.getUserInput('input your polygon color here')

def getNGonOutline(app):
    app.polygonOutlineColor = app.getUserInput('input your polygon outline color here')

def getNGonSides(app):
    app.polygonSides = int(app.getUserInput('input your number of sides here'))