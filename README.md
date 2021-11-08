# Quantum Aliased Paint

DEMO: https://youtu.be/0qGxYQypkzQ

This is a simple graphics editor with some image editing capabilities. 

Tools can be switched using the grey buttons on the side

## Required Modules

To use this program, please install the following modules:
* cmu_112_graphics
* pyscreenshot

The program may not function properly on some operating systems. 

## Available Tools

### line
creates a straight line by clicking and dragging between two points
* thickness: changes the thickness of the line
* color: changes the color of the line (must type in a valid color recognizable by tkinter)

### pen
draws a freeform line by dragging the cursor
* thickness: changes the thickness of the line
* color: changes the color of the line (must type in a valid color recognizable by tkinter)

### image
* import: imports and exports file from the computer
* crop: dragging across the screen will create a transparent black rectangle which indicates the area which will be cropped
* rotate: rotates the image 
* brightness: press the button to turn brightness mode on. Press the up or down arrows to increase or decrease the brightness
* export: export image only works on certain platforms (i.e. Windows)
* redo: will redo cropping an image

### polygon
creates a polygon of n number of sides
* sides: changes the number of sides of the polygon
* outline thickness: changes the thickness of the outline
* outline color: changes the color of the outline (must type in a valid color recognizable by tkinter)
* fill: changes the color of the shape (must type in a valid color recognizable by tkinter)

### oval
creates a oval by clicking and dragging
* sides: changes the number of sides of the polygon
* outline thickness: changes the thickness of the outline
* outline color: changes the color of the outline (must type in a valid color recognizable by tkinter)
* fill: changes the color of the shape (must type in a valid color recognizable by tkinter)

### polygon
creates a polygon of n number of sides
* thickness: changes the thickness of the outline
* color: changes the fill color of the outline (must type in a valid color recognizable by tkinter)
* outline: changes the outline color of the shape (must type in a valid color recognizable by tkinter)

### drag
drags any object (except pen lines) from one location to another

### text
click on the screen, input text and the text will appear at the location clicked
* size: changes the size of the font
* color: changes the color of the text
* font: changes the font family of the text
* anchor: changes the anchor location of the text
* justify: justifies the text left, right, or center

### undo
 will undo the last object created
