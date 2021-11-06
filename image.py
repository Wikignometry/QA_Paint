from cmu_112_graphics import *
from PIL import Image


class AppImage:
    def __init__(self):
        self.initData = None
        self.tempData = None

    def importImage(self, path: str) -> None:
        self.initData = Image.open(path)
        self.tempData = ImageTk.PhotoImage(self.initData)

    def exportImage(self, path: str) -> None:
        self.initData.save(path)


def appStarted(app):
    app.image = AppImage()
    # testing purposes
    app.image.importImage(path="test/importImage.jpg")
    app.image.exportImage(path="./test/exportImage.jpg")


def redrawAll(app, canvas):
    if app.image.tempData:
        canvas.create_image(app.width / 2, app.height / 2, image=app.image.tempData)


runApp(width=500, height=500)
