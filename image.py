from cmu_112_graphics import *
from PIL import Image


class AppImage:
    def __init__(self):
        self.initData = None
        self.currIndex = -1
        self.currData = list()
        self.action = {"crop": {"ing": False, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()},
                       "rotate": {"ing": False},
                       "brightness": {"ing": False, "done": False, "increase": False, "decrease": False, "ratio": 1.1}}
    def importImage(self, path: str) -> None:
        self.initData = Image.open(path)
        self.currData.append(self.initData)
        self.currIndex += 1

    def exportImage(self, path: str) -> None:
        self.currData[self.currIndex].save(path)

    def cropImage(self, app, sPos: tuple, ePos: tuple) -> None:
        if self.currData:
            width, height = self.currData[self.currIndex].size
            dX, dY = (app.width / 2) - (width / 2), (app.height / 2) - (height / 2)
            x0, y0 = min(sPos[0], ePos[0]) - dX, min(sPos[1], ePos[1]) - dY
            x1, y1 = max(sPos[0], ePos[0]) - dX, max(sPos[1], ePos[1]) - dY
            # drop previous redo-move after tempIndex
            self.currData = self.currData[:self.currIndex + 1]
            self.currData.append(self.currData[self.currIndex].crop((x0, y0, x1, y1)))
            self.currIndex += 1

    def rotateImage(self):
        if self.currData:
            self.currData = self.currData[:self.currIndex + 1]
            self.currData.append(self.currData[self.currIndex].transpose(Image.ROTATE_270))
            self.currIndex += 1
            self.action["rotate"]["ing"] = False

    def brightnessImage(self):
        if self.currData:
            self.currData = self.currData[:self.currIndex + 1]
            tempData = Image.new(mode="RGB", size=self.currData[self.currIndex].size)
            for x in range(tempData.width):
                for y in range(tempData.height):
                    r, g, b = self.currData[self.currIndex].getpixel((x, y))
                    if self.action["brightness"]["increase"]:
                        r, g, b = (int(r * self.action["brightness"]["ratio"]),
                                   int(g * self.action["brightness"]["ratio"]),
                                   int(b * self.action["brightness"]["ratio"]))
                    elif self.action["brightness"]["decrease"]:
                        r, g, b = (int(r / self.action["brightness"]["ratio"]),
                                   int(g / self.action["brightness"]["ratio"]),
                                   int(b / self.action["brightness"]["ratio"]))
                    if r > 255: r = 255
                    if g > 255: g = 255
                    if b > 255: b = 255
                    tempData.putpixel((x, y), (r, g, b))
            self.currData.append(tempData)
            self.currIndex += 1

    def drawCropRegion(self, canvas, sPos: tuple, ePos: tuple) -> None:
        canvas.create_rectangle(sPos[0], sPos[1], ePos[0], ePos[1], width=1)

    def draw(self, app: TopLevelApp, canvas: WrappedCanvas) -> None:
        if self.currData:
            canvas.create_image(app.width / 2, app.height / 2, image=ImageTk.PhotoImage(self.currData[self.currIndex]))
            width, height = self.currData[self.currIndex].size
            dX, dY = (app.width / 2) - (width / 2), (app.height / 2) - (height / 2)
            canvas.create_rectangle(dX, dY, dX + width, dY + height, width=1)
        if self.action["crop"]["ing"] and self.action["crop"]["dPos"]:
            self.drawCropRegion(canvas, self.action["crop"]["sPos"], self.action["crop"]["dPos"])

    def update(self, app):
        if self.action["crop"]["ing"] and self.action["crop"]["done"]:
            self.cropImage(app, self.action["crop"]["sPos"], self.action["crop"]["ePos"])
            self.action["crop"].update({"ing": True, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()})
        if self.action["rotate"]["ing"]:
            self.rotateImage()
            self.action["rotate"].update({"ing": False})
        if self.action["brightness"]["ing"] and self.action["brightness"]["done"]:
            self.brightnessImage()
            self.action["brightness"].update({"ing": False, "done": False, "increase": False, "decrease": False, "ratio": 1.1})

    def undo(self):
        if self.currIndex > 0: self.currIndex -= 1

    def redo(self):
        if -1 < self.currIndex < len(self.currData) - 1 and self.currData: self.currIndex += 1


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
    if event.key == "c":
        app.image.action["crop"]["ing"] = True
    if event.key == "b":
        app.image.action["brightness"]["ing"] = True
    if event.key == "Up":
        if app.image.action["brightness"]["ing"]:
            app.image.action["brightness"]["increase"] = True
            app.image.action["brightness"]["done"] = True
    if event.key == "Down":
        if app.image.action["brightness"]["ing"]:
            app.image.action["brightness"]["decrease"] = True
            app.image.action["brightness"]["done"] = True


def timerFired(app):
    app.image.update(app)


def appStarted(app):
    app.image = AppImage()


def redrawAll(app, canvas):
    app.image.draw(app, canvas)


# runApp(width=1920, height=1080)
