from button import *

def makeNGonButtons(app):
    buttons = []
    nGonButtonActions ={'thickness':getNGonThickness, 'color':getNGonFill, 'outline':getNGonOutline, 'sides':getNGonSides}
    
    y = 50
    x = 100
    for label in nGonButtonActions:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=nGonButtonActions[label]))
        x += 60
    return buttons

def getNGonThickness(app):
    app.nGonThickness = int(app.getUserInput('input your nGon thickness here'))

def getNGonFill(app):
    app.nGonFill = app.getUserInput('input your nGon color here')

def getNGonOutline(app):
    app.nGonOutline = app.getUserInput('input your nGon outline color here')

def getNGonSides(app):
    app.nGonSides = int(app.getUserInput('input your nGon sides here'))