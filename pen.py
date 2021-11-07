import math

class Pen():
    def __init__(self,x,y,thickness,fill):
        self.linePoints = [(x, y)]
        self.status = 0
        self.currentLocation = (x, y)
        self.w0, self.w1, self.h0, self.h1 = (0, 0, 0, 0)
        self.width = thickness
        self.fill = fill
        self.style = ''
        self.w = []
        self.h = []
        self.findMinMax()
        
    def __repr__(self):
        return f'Pen({self.linePoints[0]}, {self.linePoints[-1]})'
    
    def assignPoints(self, x, y):
        self.linePoints.append((x, y))

    def draw(self, app, canvas):
        if len(self.linePoints) > 2:
            canvas.create_line(self.linePoints, width = self.width, fill = self.fill, smooth=True)
        # for i in range(len(self.linePoints)-1):
        #     x0,y0=self.linePoints[i]
        #     x1,y1=self.linePoints[i+1]
        #     canvas.create_line(x0, y0, x1, y1, width = self.width, fill = self.fill)
    
    def findMinMax(self):
        self.points = []
        xList = []
        yList = []
        for x, y in self.linePoints:
            xList.append(x)
            yList.append(y)

        print(xList, yList)
        print(self.w, self.h)

        x0, x1 = min(xList), max(xList)
        y0, y1 = min(yList), max(yList)

        self.points.append((x0, y0))
        self.points.append((x1, y1))

    def moveHelper(self, x, y):
        self.w = []
        self.h = []
        for px, py in self.linePoints:
            self.w.append(px-x)
            self.h.append(py-y)
            
        self.findMinMax()

    def move(self, newX, newY):
        for i in range(self.w):
            self.linePoints[i] = (newX+self.w[i], newY+self.h[i])