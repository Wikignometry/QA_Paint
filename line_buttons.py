from button import *

def makeAutoLineValues(app):
    app.thickness = 2
    app.lineFill = 'black'
    
def makeLineButtons(app):
    app.lineButtons = []
    lineButtonActions={'thickness':getThickness, 'lineFill': getLineFill}
    
def getThickness(app):
    app.thickness = app.getUserInput('input your line thickness here')

def getLineFill(app):
    app.lineFill = app.getUserInput('input your line color here')
