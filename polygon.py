class Polygon():
    def __init__(self, x, y):
        self.points = [(x, y)]
        self.status = 0
        self.currentLocation = (x, y)
    
    def __repr__(self):
        return f'Polygon({self.points[0]}, {self.points[-1]})'
    
    def assignPoints(self, x, y):
        if self.status < 1:
            self.points.append((x, y))
            self.status += 1

    def draw(self, canvas):
        if len(self.points) == 1:
            x0, y0 = self.points[0]
            x1, y1 = self.currentLocation
        else:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
        
        canvas.create_rectangle(x0, y0, x1, y1, width = 3)