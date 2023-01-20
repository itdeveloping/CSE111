# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 600

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_mountains(canvas, scene_width, scene_height)

    #draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""

    draw_rectangle(canvas, 0, 200, 800, 600, width=0, fill="skyBlue2")


def draw_mountains(canvas, scene_width, scene_height):

    draw_polygon(canvas,
        419, 261, 719, 477, 152, 488, fill="darkGreen")

    draw_polygon(canvas,
        340, 340, 400, 300, 150, 200, fill="gray90")        
    pass

# Call the main function so that
# this program will start executing.
main()