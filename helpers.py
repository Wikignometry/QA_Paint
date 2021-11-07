# contains helper functions

from button import *

def makeTextButtons(app):
    app.textButtons = []
    textButtonActions = {'color': getTextFill, 'font': getFont, 'size': getSize, 'anchor': getAnchor, 'justify': getJustify, 'style': getStyle}
    y = 100
    x = 30
    for label in [ 'color', 'font', 'size', 'anchor', 'justify', 'style']:
        app.textButtons.append(Button((50,30), location=(x, y), label=label, fill='light grey', action=textButtonActions[label]))
        x += 60

def makeAutoTextValues(app):
    app.font = 'Calbri'
    app.textFill = 'black'
    app.size = '12'
    app.anchor = 'center'
    app.justify = 'center'
    app.style = 'roman'

def getText(app, event):
    text = app.getUserInput('input your text here')
    thing = Text(str(text), (50,50)#, 
                        # color=app.textFill, 
                        # font=(app.font, app.size, app.style), 
                        # anchor=app.anchor, 
                        # justify=app.justify
                        )
    app.objects.append(thing)

def getFont(app):
    app.font = app.getUserInput('input your font family here')

def getTextFill(app):
    app.textFill = app.getUserInput('input your color here')

def getSize(app):
    app.size = app.getUserInput('input your font size here')

def getAnchor(app):
    app.anchor = app.getUserInput('input your color here')

def getJustify(app):
    app.justify = app.getUserInput('input left, right or center here')

def getStyle(app):
    app.style = app.getUserInput('input roman or italics here')


