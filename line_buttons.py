from button import *
    
def makeLineButtons(app):
    buttons = []
    lineButtonActions={'thickness':getThickness, 
                        'lineFill': getLineFill}
    y = 50
    x = 60
    for label in [ 'thickness', 'lineFill']:
        buttons.append(Button((50,30), location=(x, y), 
        label=label, fill='light grey', action=lineButtonActions[label]))
        x += 60
    return buttons

def getThickness(app):
    app.thickness = app.getUserInput('input your line thickness here')

def getLineFill(app):
    app.lineFill = app.getUserInput('input your line color here')
