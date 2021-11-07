from cmu_112_graphics import *

def appStarted(app):
    url = 'https://tinyurl.com/great-pitch-gif'
    app.image1 = app.loadImage(url)

    # now let's make a copy that only uses the red part of each rgb pixel:
    app.image1 = app.image1.convert('RGB')
    for x in range(app.image2.width):
        for y in range(app.image2.height):
            r,g,b = app.image1.getpixel((x,y))
            app.image2.putpixel((x,y),(r,0,0))

def redrawAll(app, canvas):
    canvas.create_rectangle(200, 300,500,600)
    canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))

runApp(width=700, height=800)