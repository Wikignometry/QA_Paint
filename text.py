#           Imported Functions

from cmu_112_graphics import *

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

################################################################################
#               test functions

def appStarted(app):
    app.text = Text('I am a text', (app.height//2, app.width//2), fill='blue', font='Calbri', size=50)



def redrawAll(app, canvas):
    app.text.draw(canvas)


runApp(width=500, height=500)


    



