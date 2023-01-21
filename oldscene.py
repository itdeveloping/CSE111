# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky (canvas, scene_width, scene_height)
    
    draw_brick(canvas, 400,350)
    draw_brick(canvas, 440,350)
    draw_brick(canvas, 410,365)
    draw_brick(canvas, 450,365)
    draw_brick(canvas, 420,380)
    draw_brick(canvas, 460,380)
    draw_brick(canvas, 430,395)
    draw_brick(canvas, 470,395)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas,0,0,100,100,width=0, fill="sky blue")

    pass

def draw_ground():
    pass

def draw_brick(canvas, x, y):
    draw_rectangle(canvas, x,y,x+40,y+15,width=2, outline="black", fill="brown1")
# Call the main function so that
# this program will start executing.
main()