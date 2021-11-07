import math

class Pen():
    def __init__(self,x,y,thickness,fill):
        self.points = [(x, y)]
        self.status = 0
        self.currentLocation = (x, y)
        self.w0, self.w1, self.h0, self.h1 = (0, 0, 0, 0)
        self.width = thickness
        self.fill = fill
        self.style = ''
        
    def __repr__(self):
        return f'Line({self.points[0]}, {self.points[-1]})'
    
    def assignPoints(self, x, y):
        self.points.append((x, y))

    def draw(self, app, canvas):
        if len(self.points) > 2:
            canvas.create_line(self.points, width = self.width, fill = self.fill, smooth=True)
        # for i in range(len(self.points)-1):
        #     x0,y0=self.points[i]
        #     x1,y1=self.points[i+1]
        #     canvas.create_line(x0, y0, x1, y1, width = self.width, fill = self.fill)