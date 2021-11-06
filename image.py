from cmu_112_graphics import *
from PIL import Image


class AppImage:
    def __init__(self):
        self.initData = None
        self.tempData = None
        self.action = {"crop": {"ing": True, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()}}

    def importImage(self, path: str) -> None:
        self.initData = Image.open(path)
        self.tempData = ImageTk.PhotoImage(self.initData)

    def exportImage(self, path: str) -> None:
        self.initData.save(path)

    def cropImage(self, sPos: tuple, ePos: tuple) -> None:
        self.initData = self.initData.crop((sPos[0], sPos[1], ePos[0], ePos[1]))

    def drawCropRegion(self, canvas, sPos: tuple, ePos: tuple) -> None:
        canvas.create_rectangle(sPos[0], sPos[1], ePos[0], ePos[1], width=1)

    def draw(self, app: TopLevelApp, canvas: WrappedCanvas) -> None:
        if self.initData:
            self.tempData = ImageTk.PhotoImage(self.initData)
            canvas.create_image(app.width / 2, app.height / 2, image=self.tempData)
        if self.action["crop"]["ing"] and self.action["crop"]["dPos"]:
            self.drawCropRegion(canvas, self.action["crop"]["sPos"], self.action["crop"]["dPos"])

    def update(self):
        if self.action["crop"]["ing"] and self.action["crop"]["done"]:
            self.cropImage(self.action["crop"]["sPos"], self.action["crop"]["ePos"])
            # reset self.action["crop"]
            self.action["crop"].update({"ing": True, "done": False, "sPos": tuple(), "dPos": tuple(), "ePos": tuple()})


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
        filePath = filedialog.askopenfilename(initialfile="import-image", defaultextension=".jpg",)
        if filePath: app.image.importImage(path=filePath)
    if event.key == "control-s":
        filePath = filedialog.asksaveasfilename(initialfile="export-image", defaultextension=".jpg",
                                                filetypes=[("ImageFile", ".jpg")])
        if filePath: app.image.exportImage(path=filePath)


def timerFired(app):
    app.image.update()


def appStarted(app):
    app.image = AppImage()


def redrawAll(app, canvas):
    app.image.draw(app, canvas)


runApp(width=500, height=500)
