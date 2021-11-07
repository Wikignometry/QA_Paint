from cmu_112_graphics import *
from PIL import Image


class AppImage:
    def __init__(self):
        self.initData = None
        self.tempIndex = -1
        self.tempData = list()
        self.action = {"crop": {"ing": True, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()},
                       "rotate": {"ing": False}}

    def importImage(self, path: str) -> None:
        self.initData = Image.open(path)
        self.tempData.append(self.initData)
        self.tempIndex += 1

    def exportImage(self, path: str) -> None:
        self.tempData[self.tempIndex].save(path)

    def cropImage(self, app, sPos: tuple, ePos: tuple) -> None:
        if self.tempData:
            width, height = self.tempData[self.tempIndex].size
            dX, dY = (app.width / 2) - (width / 2), (app.height / 2) - (height / 2)
            x0, y0 = min(sPos[0], ePos[0]) - dX, min(sPos[1], ePos[1]) - dY
            x1, y1 = max(sPos[0], ePos[0]) - dX, max(sPos[1], ePos[1]) - dY
            # drop previous redo-move after tempIndex
            self.tempData = self.tempData[:self.tempIndex + 1]
            self.tempData.append(self.tempData[self.tempIndex].crop((x0, y0, x1, y1)))
            self.tempIndex += 1

    def rotateImage(self):
        if self.tempData:
            self.tempData = self.tempData[:self.tempIndex + 1]
            self.tempData.append(self.tempData[self.tempIndex].transpose(Image.ROTATE_270))
            self.tempIndex += 1

    def drawCropRegion(self, canvas, sPos: tuple, ePos: tuple) -> None:
        canvas.create_rectangle(sPos[0], sPos[1], ePos[0], ePos[1], width=1)

    def draw(self, app: TopLevelApp, canvas: WrappedCanvas) -> None:
        if self.tempData:
            canvas.create_image(app.width / 2, app.height / 2, image=ImageTk.PhotoImage(self.tempData[self.tempIndex]))
        if self.action["crop"]["ing"] and self.action["crop"]["dPos"]:
            self.drawCropRegion(canvas, self.action["crop"]["sPos"], self.action["crop"]["dPos"])

    def update(self, app):
        if self.action["crop"]["ing"] and self.action["crop"]["done"]:
            self.cropImage(app, self.action["crop"]["sPos"], self.action["crop"]["ePos"])
            # reset self.action["crop"]
            self.action["crop"].update({"ing": True, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()})
        if self.action["rotate"]["ing"]:
            self.rotateImage()
            self.action["rotate"]["ing"] = False

    def undo(self):
        if self.tempIndex > 0: self.tempIndex -= 1

    def redo(self):
        if -1 < self.tempIndex < len(self.tempData) - 1 and self.tempData: self.tempIndex += 1


def mousePressed(app, event):
    if app.image.action["crop"]["ing"]:
        app.image.action["crop"]["sPos"] = (event.x, event.y)


def mouseDragged(app, event):
    if app.image.action["crop"]["ing"]:
        app.image.action["crop"]["dPos"] = (event.x, event.y)


def mouseReleased(app, event):
    if app.image.action["crop"]["ing"]:
        app.image.action["crop"]["ePos"] = (event.x, event.y)
        app.image.action["crop"]["done"] = True


def keyPressed(app, event):
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
    if event.key == "r":
        app.image.action["rotate"]["ing"] = True


def timerFired(app):
    app.image.update(app)


def appStarted(app):
    app.image = AppImage()


def redrawAll(app, canvas):
    app.image.draw(app, canvas)


# runApp(width=500, height=500)
