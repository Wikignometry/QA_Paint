from cmu_112_graphics import *

from polygon import *
from line import *
from oval import *
from image import *

def appStarted(app):
    app.status = 'Line'
    app.image = AppImage()
    app.objects = []
    app.currentObject = None

def keyPressed(app, event):
    if event.key == 'l':
        app.status = 'Line'
    elif event.key == 'p':
        app.status = 'Polygon'
    elif event.key == 'o':
        app.status = 'Oval'
    elif event.key == 'c':
        app.status = 'Crop'
    elif event.key == 'd':
        app.status = 'Drag'
            
    # https://pythonspot.com/tk-file-dialogs/
    if event.key == "control-o":
        filePath = filedialog.askopenfilename(initialfile="import-image", defaultextension=".jpg", )
        if filePath: app.image.importImage(path=filePath)
    if event.key == "control-s" and app.image.tempData:
        filePath = filedialog.asksaveasfilename(initialfile="export-image", defaultextension=".jpg",
                                                filetypes=[("ImageFile", ".jpg")])
        if filePath: app.image.exportImage(path=filePath)
    

    elif event.key == 'w':
        print(app.objects)
        
    elif event.key == 'z':
        undo(app)

def mousePressed(app, event):
    if app.status == 'Line':
        app.objects.append(Line(event.x, event.y))
    
    elif app.status == 'Polygon':
        app.objects.append(Polygon(event.x, event.y))
    
    elif app.status == 'Oval':
        app.objects.append(Oval(event.x, event.y))
    
    elif app.status == 'Crop':
        if app.image.action["crop"]["ing"]:
            app.image.action["crop"]["sPos"] = (event.x, event.y)
    
    elif app.status == 'Drag':
        for object in app.objects:
            x0, y0 = object.points[0]
            x1, y1 = object.points[1]
            minX, maxX = min(x0, x1), max(x0, x1)
            minY, maxY = min(y0, y1), max(y0, y1)
            if minX < event.x < maxX and minY < event.y < maxY:
                app.currentObject = object
                object.moveHelper(event.x, event.y)
                
def mouseDragged(app, event):
    if app.status == 'Line' or app.status == 'Polygon' or app.status == 'Oval':
        app.objects[-1].currentLocation = (event.x, event.y)
    
    elif app.status == 'Crop':
        if app.image.action["crop"]["ing"]:
            app.image.action["crop"]["dPos"] = (event.x, event.y) 
    
    elif app.status == 'Drag':
        app.currentObject.move(event.x, event.y)
    
def mouseReleased(app, event):
    if app.status == 'Line' or app.status == 'Polygon' or app.status == 'Oval':
        if len(app.objects) > 0:
            app.objects[-1].assignPoints(event.x, event.y)
    
    elif app.status == 'Crop':
        if app.image.action["crop"]["ing"]:
            app.image.action["crop"]["ePos"] = (event.x, event.y)
            app.image.action["crop"]["done"] = True


def undo(app):
    if app.objects == []:
        return
    app.objects.pop()


def timerFired(app):
    app.image.update()

def redrawAll(app, canvas):
    # app.image.draw(app, canvas)
    for object in app.objects:
        object.draw(app, canvas)
    
    
if __name__ == '__main__':
    runApp(width=500,height=500)