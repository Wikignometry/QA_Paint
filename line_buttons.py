from button import *
    
def makeLineButtons(app):
    buttons = []
    lineButtonActions={'thickness':getLineThickness, 
                        'color': getLineFill}
    y = 30
    x = 100
    for label in lineButtonActions:
        buttons.append(Button((80,30), location=(x, y), 
        label=label, fill='powder blue', action=lineButtonActions[label]))
        x += 90
    return buttons

def getLineThickness(app):
     thickness = app.getUserInput('input your line thickness here')
     if thickness != None:
        app.lineThickness = int(thickness)

def getLineFill(app):
    app.lineFill = app.getUserInput('input your line color here')
