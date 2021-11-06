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

    def displayImage(self, app: TopLevelApp, canvas: WrappedCanvas) -> None:
        if self.initData:
            self.tempData = ImageTk.PhotoImage(self.initData)
            canvas.create_image(app.width / 2, app.height / 2, image=self.tempData)

    def cropImage(self, x0: int, y0: int, x1: int, y1: int) -> None:
        self.initData = self.initData.crop((x0, y0, x1, y1))


def appStarted(app):
    app.image = AppImage()
    # testing purposes
    app.image.importImage(path="./test/importImage.jpg")
    app.image.cropImage(0, 0, 250, 250)
    app.image.exportImage(path="./test/exportImage.jpg")


def redrawAll(app, canvas):
    app.image.displayImage(app, canvas)


runApp(width=500, height=500)
