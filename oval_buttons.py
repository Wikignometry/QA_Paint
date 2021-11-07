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


def makeAutoOvalValues(app):
    app.ovalThickness = 3
    app.ovalFill = ''
    app.ovalOutline = 'black'

def getOvalThickness(app):
    thickness = (app.getUserInput('input your oval thickness here'))
    if thickness != None:
        app.ovalThickness = int(thickness)

def getOvalFill(app):
    app.ovalFill = app.getUserInput('input your oval color here')

def getOvalOutline(app):
    app.ovalOutline = app.getUserInput('input your oval outline color here')