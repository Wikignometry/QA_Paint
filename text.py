#           Imported Functions

from cmu_112_graphics import *
from helpers import *
################################################################################


class Text():

    def __init__(self, text, location, anchor='center', fill='black', 
                font='Arial', size=12, justify='center', style='roman'):
        self.text = text # str
        self.fill = fill # color representation (str or hex)
        self.font = font # font name
        self.size = size # int (font size)
        self.x, self.y = location # refers to the center of the text
        self.justify = justify
        self.anchor = anchor
        self.style = style

    def draw(self, canvas):
        canvas.create_text(self.x, self.y, 
                    text=f'{self.text}', 
                    font = (self.font, self.size, self.style),
                    anchor=self.anchor, 
                    justify=self.justify, 
                    fill=self.fill)


#####

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
    if text != None:
        app.objects.append(Text(str(text), (event.x, event.y), 
                        fill=app.textFill, 
                        font=(app.font, app.size, app.style), 
                        anchor=app.anchor, 
                        justify=app.justify
                        ))

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





################################################################################
#               test functions

def appStarted(app):
    makeAutoTextValues(app)
    makeTextButtons(app)
    app.objects = [ ]

def mousePressed(app, event):
    getText(app, event)

def redrawAll(app, canvas):
    for button in app.textButtons:
        button.draw(canvas)
    for object in app.objects:
        object.draw(canvas)


runApp(width=500, height=500)


    



