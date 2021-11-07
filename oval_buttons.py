from button import *

def makeOvalButtons(app):
    buttons = []
    ovalButtonActions={'thickness':getOvalThickness, 'color':getOvalFill, 'outline':getOvalOutline}

    y = 50
    x = 100
    for label in ovalButtonActions:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=ovalButtonActions[label]))
        x += 60
    return buttons

def getOvalThickness(app):
    app.ovalThickness = int(app.getUserInput('input your oval thickness here'))

def getOvalFill(app):
    app.ovalFill = app.userInput('input your oval color here')

def getOvalOutline(app):
    app.ovalOutline = app.userInput('input your oval outline color here')