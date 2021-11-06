from cmu_112_graphics import *


class Image:
    def __init__(self):
        self.data = None

    def importImage(self, app: TopLevelApp, path: str) -> None:
        self.data = ImageTk.PhotoImage(app.loadImage(path))


def appStarted(app):
    app.image = Image()
    app.image.importImage(app, path="./test/pikachu.jpg")


def redrawAll(app, canvas):
    if app.image.data: canvas.create_image(app.width / 2, app.height / 2, image=app.image.data)


runApp(width=500, height=500)
