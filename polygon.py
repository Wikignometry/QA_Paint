class Polygon():
    def __init__(self):
        self.points = []
        self.status = 0
    
    def assignPoint(self, x, y):
        self.points.append((x, y))

        self.status += 1
        if self.status > 2:
            self.status = 1
        
    
    def draw(self, canvas):
        for i in range(0, len(self.points)-1,2):
            x0,y0=self.points[i]
            x1,y1=self.points[i+1]
            # if math.isclose(x0,x1,abs_tol=1)
            canvas.create_rectangle(x0, y0, x1, y1, width=5)
        if len(self.points)%2==1:
            x0,y0=self.points[-1]
            x1,y1=self.currentLocation
            canvas.create_rectangle(x0, y0, x1, y1, width=5)
    
    def undo(self):
        for _ in range(self.status):
            self.points.pop()
        
        self.status = 0

