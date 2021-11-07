from button import *

def makeNGonButtons(app):
    buttons = []
    nGonButtonActions ={'outlineThickness':getNGonThickness, 'fill':getNGonFill, 'outlineColor':getNGonOutline, 'sides':getNGonSides}
    
    y = 50
    x = 100
    for label in nGonButtonActions:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=nGonButtonActions[label]))
        x += 60
    return buttons

def getNGonThickness(app):
    app.polygonOutlineThickness = int(app.getUserInput('input your nGon thickness here'))

def getNGonFill(app):
    app.polygonFill = app.getUserInput('input your nGon color here')

def getNGonOutline(app):
    app.polygonOutlineColor = app.getUserInput('input your nGon outline color here')

def getNGonSides(app):
    app.polygonSides = int(app.getUserInput('input your nGon sides here'))