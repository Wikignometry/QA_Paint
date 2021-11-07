class Line():
    def __init__(self, x, y):
        self.points = [(x, y)]
        self.status = 0
        self.currentLocation = (x, y)
        self.w0, self.w1, self.h0, self.h1 = (0, 0, 0, 0)
        self.width = 3
        self.fill = 'black'
    
    def __repr__(self):
        return f'Line({self.points[0]}, {self.points[-1]})'
    
    def assignPoints(self, x, y):
        if self.status < 1:
            self.points.append((x, y))
            self.status += 1

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

    def draw(self, app, canvas):
        if len(self.points) == 1:
            x0, y0 = self.points[0]
            x1, y1 = self.currentLocation
        else:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
        
        canvas.create_line(x0, y0, x1, y1, width = self.width, fill = self.fill)
