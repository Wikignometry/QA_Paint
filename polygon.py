class Polygon():
    def __init__(self):
        self.points = []
        self.currentLocation = (0, 0)
    
    def assignPoint(self, x, y):
        self.points.append((x, y))
    
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
        if len(self.points) > 0:
            if len(self.points)%2==0:
                self.points.pop()
                self.points.pop()
            else:
                self.points.pop()

    

