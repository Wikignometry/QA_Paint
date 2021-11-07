#           Imported Functions

from cmu_112_graphics import *
from button import *
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
        self.points = []
        self.pointMaker()


    def draw(self, app, canvas):
        canvas.create_text(self.x, self.y, 
                    text=f'{self.text}', 
                    font = (self.font, self.size, self.style),
                    anchor=self.anchor, 
                    justify=self.justify, 
                    fill=self.fill)
    
    def pointMaker(self):
        self.intSize = int(self.size)
        y0, y1 = self.y-self.intSize , self.y+self.intSize 
        x0, x1 = self.x-self.intSize *(len(self.text)/2), self.x+self.intSize *(len(self.text)/2)
        self.points.append((x0, y0))
        self.points.append((x1, y1))

    def moveHelper(self, x, y):
        x0, y0 = self.points[0]
        x1, y1 = self.points[1]

        self.w0 = x - x0
        self.h0 = y - y0
        self.w1 = x1 - x
        self.h1 = y1 - y

    def move(self, newX, newY):
        nx0, ny0 = newX - self.w0, newY - self.h0
        nx1, ny1 = newX + self.w1, newY + self.h1

        self.points[0] = (nx0, ny0)
        self.points[1] = (nx1, ny1)

        self.x = nx0 + self.intSize *(len(self.text)/2)
        self.y = ny0 + self.intSize 



#####

def makeTextButtons(app):
    buttons = []
    textButtonActions = {'color': getTextFill, 'font': getFont, 'size': getSize, 'anchor': getAnchor, 'justify': getJustify, 'style': getStyle}
    y = 30
    x = 100
    for label in [ 'color', 'font', 'size', 'anchor', 'justify', 'style']:
        buttons.append(Button((80,30), location=(x, y), label=label, fill='powder blue', action=textButtonActions[label]))
        x += 90
    return buttons

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
                        font=app.font, size=app.size, style=app.style, 
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
    app.style = app.getUserInput('input roman, italics, bold, or underline here')

################################################################################
#               test functions

# def appStarted(app):
#     makeAutoTextValues(app)
#     makeTextButtons(app)
#     app.objects = [ ]

# def mousePressed(app, event):
#     for button in app.textButtons:
#         if button.isPressed(event.x, event.y):
#             button.action(app)
#             return
#     getText(app, event)


# def redrawAll(app, canvas):
#     for button in app.textButtons:
#         button.draw(canvas)
#     for object in app.objects:
#         object.draw(canvas)


# runApp(width=500, height=500)


    



