from button import *
    
def makeLineButtons(app):
    buttons = []
    lineButtonActions={'thickness':getLineThickness, 
                        'color': getLineFill}
    y = 50
    x = 100
    for label in lineButtonActions:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=lineButtonActions[label]))
        x += 60
    return buttons

def getLineThickness(app):
    app.lineThickness = int(app.getUserInput('input your line thickness here'))

def getLineFill(app):
    app.lineFill = app.getUserInput('input your line color here')
