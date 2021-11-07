from cmu_112_graphics import *
from text import *
from polygon import *
from line import *
from oval import *
from helpers import *
from image import *
from tool_buttons import *
from line_buttons import *
from ngons_buttons import *
from oval_buttons import *
from image_buttons import *

from button import *
from polygon_buttons import *

def appStarted(app):
    app.status = 'Line'
    app.image = AppImage()
    app.objects = []
    app.currentObject = None
    
    app.buttons = dict()

    app.buttons['Tools']= makeToolButtons(app)

    makeAutoTextValues(app)
    makeAutoOvalValues(app)
    # create a bunch of top level attributes

    app.buttons['Line'] = makeLineButtons(app)
    app.buttons['Polygon'] = makeNGonButtons(app)
    app.buttons['Oval'] = makeOvalButtons(app)
    app.buttons['Image'] = makeImageButtons(app)
    app.buttons['Crop'] = makeImageButtons(app)
    app.buttons['Drag'] = []
    app.buttons['Text'] = makeTextButtons(app)


    app.lineThickness=2
    app.lineFill="black"
    app.polygonOutlineThickness=2
    app.polygonFill=""
    app.polygonOutlineColor="black"
    app.polygonSides=4
    app.ovalThickness=2
    app.ovalFill=""
    app.ovalOutline="black"

def keyPressed(app, event):
    if event.key == 'l':
        app.status = 'Line'
    elif event.key == 'p':
        app.status = 'Polygon'
    elif event.key == 'o':
        app.status = 'Oval'
    elif event.key == 'i':
        app.status = 'Image'
    elif event.key == 'd':
        app.status = 'Drag'
    elif event.key == 't':
        app.status = 'Text'

    # https://pythonspot.com/tk-file-dialogs/
    if event.key == "control-o":
        filePath = filedialog.askopenfilename(initialfile="import-image", defaultextension=".jpg", )
        if filePath: app.image.importImage(path=filePath)
    if event.key == "control-s" and app.image.tempData:
        filePath = filedialog.asksaveasfilename(initialfile="export-image", defaultextension=".jpg",
                                                filetypes=[("ImageFile", ".jpg")])
        if filePath: app.image.exportImage(path=filePath)
    if event.key == "control-z":
        app.image.undo()
    if event.key == "control-r":
        app.image.redo()
    elif event.key == 'z':
        undo(app)

def mousePressed(app, event):
    for button in app.buttons['Tools']:
        if button.isPressed(event.x, event.y):
            button.action(app)
            return
    for button in app.buttons[app.status]:
        if button.isPressed(event.x, event.y):
            button.action(app)
            return

    if app.status == 'Line':
        app.objects.append(Line(event.x, event.y,app.lineThickness,app.lineFill))

    elif app.status == 'Polygon':
        app.objects.append(Polygon(event.x, event.y,app.polygonSides, app.polygonOutlineThickness, app.polygonOutlineColor, app.polygonFill))

    elif app.status == 'Oval':
        app.objects.append(Oval(event.x, event.y, app.ovalFill, app.ovalThickness, app.ovalOutline))

    elif app.status == 'Crop':
        app.image.action["crop"]["ing"] = True
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

    elif app.status == 'Text':
        getText(app, event)

def mouseDragged(app, event):
    if app.status == 'Line' or app.status == 'Polygon' or app.status == 'Oval':
        if app.objects != []:
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

# def undo(app):
#     if app.objects == []:
#         return
#     app.objects.pop()

def timerFired(app):
    app.image.update(app)
    pass

def redrawAll(app, canvas):
    app.image.draw(app, canvas)
    for object in app.objects:
        object.draw(app, canvas)
    for button in app.buttons['Tools']:
        button.draw(canvas)
    for button in app.buttons[app.status]:
        button.draw(canvas)

runApp(width=500,height=500)