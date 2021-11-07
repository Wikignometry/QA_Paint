import math

class nPolygon():
    def __init__(self, x, y, n):
        self.points = [(x, y)]
        self.status = 0
        self.currentLocation = (x, y)
        self.w0, self.w1, self.h0, self.h1 = (0, 0, 0, 0)
        self.width = 3
        self.fill = ''
        self.outline = 'black'
        self.n = n
        self.npoints = []
        self.angle = 2*math.pi/self.n
    
    def assignPoints(self, x, y):
        if self.status < 1:
            self.points.append((x, y))
            self.status += 1
    
    def calculateRadius(self):
        if len(self.points) == 1:
            x0, y0 = self.points[0]
            x1, y1 = self.currentLocation
        else:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]

        self.midpoint = ((x1+x0)/2, (y1+y0)/2)
        self.r = ((x1-x0)**2 + (y1-y0)**2)**0.5 / 2
    

    def draw(self, app, canvas):
        self.calculateRadius()
        self.npoints = []
        for point in range(self.n):
            nx = self.midpoint[0] + self.r*math.cos(point*self.angle)
            ny = self.midpoint[1] + self.r*math.sin(point*self.angle)
            self.npoints.extend([nx, ny])
        
        canvas.create_polygon(self.npoints, width = self.width, outline = self.outline, fill = self.fill)