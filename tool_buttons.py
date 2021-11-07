from button import *

def makeToolButtons(app):
    app.toolButtons = []
    textButtonActions = {'line': initiateLine, 
                        'polygon': getFont, 
                        'oval': getSize, 
                        'anchor': getAnchor, 
                        'justify': getJustify, 
                        'style': getStyle}
    y = 100
    x = 30
    for label in [ 'color', 'font', 'size', 'anchor', 'justify', 'style']:
        app.textButtons.append(Button((50,30), location=(x, y), label=label, fill='light grey', action=textButtonActions[label]))
        x += 60


def initiateLine(app):
    app.status = 'Line'

