from button import *

def makeNGonButtons(app):
    buttons = []
    nGonButtonActions ={'outline\nthickness':getNGonThickness, 'fill':getNGonFill, 'outline\ncolor':getNGonOutline, 'sides':getNGonSides}
    
    y = 30
    x = 100
    for label in nGonButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='powder blue', action=nGonButtonActions[label]))
        x += 90
    return buttons

def getNGonThickness(app):
    thickness = app.getUserInput('input your nGon thickness here')
    if thickness != None:
        app.polygonOutlineThickness = int(thickness)

def getNGonFill(app):
    app.polygonFill = app.getUserInput('input your polygon color here')

def getNGonOutline(app):
    app.polygonOutlineColor = app.getUserInput('input your polygon outline color here')

def getNGonSides(app):
    sides = app.getUserInput('input your number of sides here')
    if sides != None:
        app.polygonSides = int(sides)