from cmu_112_graphics import *
import math

#All the tools
class Tools():
    def __init__(self, icon, name, location):
        self.icon = icon
        self.name = name
        self.location = location
        self.status = False
    

class Pen(Tools):
    def __init__(self, icon, name, location):
        super().__init__(icon, name, location)
        self.points = []


    def assignPoint(self, x, y):
        self.points.append((x, y))

    def draw(self, canvas):
        for i in range(0, len(self.points)-1,2):
            x0,y0=self.points[i]
            x1,y1=self.points[i+1]
            # if math.isclose(x0,x1,abs_tol=1)
            canvas.create_line(x0, y0, x1, y1, width=5)
        if len(self.points)%2==1:
            x0,y0=self.points[-1]
            x1,y1=self.currentLocation
            canvas.create_line(x0, y0, x1, y1, width=5)

def appStarted(app):
    app.pen = Pen('pwn', 'pen', (50,50))

def mousePressed(app, event):
    app.pen.assignPoint(event.x, event.y)
    pass

def mouseMoved(app,event):
    app.pen.currentLocation=(event.x,event.y)

def redrawAll(app, canvas):
    app.pen.draw(canvas)
    pass





runApp(width=500,height=500)



