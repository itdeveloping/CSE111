""""
File: scene.py
Author: Oscar Rodriguez

Purpose: Prove that you can write functions with parameters and call those functions multiple times with arguments.

"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import (
    start_drawing,
    draw_line,
    draw_oval,
    draw_arc,
    draw_rectangle,
    draw_polygon,
    draw_text,
    finish_drawing,
)

# import random library
import random

# define main function
def main():

    # canvas dimensions
    scene_width = 800
    scene_height = 600

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky
    draw_sky(canvas, scene_width, scene_height)

    # call function draw_lake
    draw_lake(canvas, scene_width, scene_height)

    # draw_ground(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # call draw_signature function
    draw_signature(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# function draw_signature
def draw_signature(canvas):
    draw_text(canvas, 90, 570, "Oscar Jose Rodriguez Alfaro", fill="brown")
    draw_rectangle(
        canvas,
        10,
        560,
        168,
        580,
        width=2,
        outline="brown4",
        fill="",
    )


# function draw_clouds
def draw_clouds(canvas, diameter, distance, x_ref, y_ref):

    for i in range(7):
        number = random.randint(1, 15)
        draw_oval(
            canvas,
            x_ref + number + distance,
            y_ref + number,
            x_ref + number + distance + diameter,
            y_ref + number + diameter,
            outline="",
            fill="white",
        )
        distance += 10


# function draw_seagull
def draw_seagull(canvas, x_ref, y_ref):
    draw_arc(
        canvas,
        x_ref + 50,
        y_ref + 100,
        x_ref + 70,
        y_ref + 120,
        width=2,
        start=0,
        extent=180,
    )
    draw_arc(
        canvas,
        x_ref + 60,
        y_ref + 110,
        x_ref + 70,
        y_ref + 120,
        width=2,
        start=0,
        extent=180,
    )


# function draw_lake
def draw_lake(canvas, scene_width, scene_height):
    draw_rectangle(
        canvas,
        0,
        scene_height - 500,
        scene_width,
        scene_height - 451,
        outline="",
        fill="deepSkyBlue",
    )


# function draw_ground
def draw_ground(canvas, scene_width, scene_height):

    # call function draw_mountains
    draw_mountains(canvas, scene_width, scene_height)

    # Draw grass
    draw_rectangle(
        canvas, 0, 0, scene_width, scene_height - 491, outline="", fill="forestGreen"
    )

    # call functions draw_pine and draw_pine_2
    draw_pine(canvas, scene_width, scene_height, 100, 70)
    draw_pine(canvas, scene_width, scene_height, 200, 40)
    draw_pine(canvas, scene_width, scene_height, 600, 50)
    draw_pine(canvas, scene_width, scene_height, 670, 20)
    draw_pine_2(canvas, scene_width, scene_height, 300, 45)
    draw_pine_2(canvas, scene_width, scene_height, 50, 35)
    draw_pine_2(canvas, scene_width, scene_height, 50, 35)


# function draw_pine2
def draw_pine_2(canvas, scene_width, scene_height, x_ref, y_ref):
    pine_color = "darkGreen"
    trunk_color = "sienna3"

    # draw trunk
    draw_polygon(
        canvas,
        x_ref + 104,
        y_ref + 3,
        x_ref + 92,
        y_ref + 3,
        x_ref + 92,
        y_ref + 19,
        x_ref + 104,
        y_ref + 19,
        outline="",
        fill=trunk_color,
    )

    # draw first level
    draw_polygon(
        canvas,
        x_ref + 116,
        y_ref + 50,
        x_ref + 134,
        y_ref + 19,
        x_ref + 63,
        y_ref + 19,
        x_ref + 80,
        y_ref + 50,
        outline="",
        fill=pine_color,
    )

    # draw second level
    draw_polygon(
        canvas,
        x_ref + 110,
        y_ref + 80,
        x_ref + 128,
        y_ref + 50,
        x_ref + 68,
        y_ref + 50,
        x_ref + 86,
        y_ref + 80,
        outline="",
        fill=pine_color,
    )

    # draw third level
    draw_polygon(
        canvas,
        x_ref + 98,
        y_ref + 113,
        x_ref + 117,
        y_ref + 80,
        x_ref + 79,
        y_ref + 80,
        outline="",
        fill=pine_color,
    )
    pass


# function draw_pine
def draw_pine(canvas, scene_width, scene_height, x_ref, y_ref):
    pine_shadow_color = "darkGreen"
    pine_color = "green3"
    trunk_shadow_color = "sienna4"
    trunk_color = "sienna3"

    # draw a pine using x_ref and y_ref for the pine position
    draw_polygon(
        canvas,
        x_ref + 101,
        y_ref + 117,
        x_ref + 124,
        y_ref + 77,
        x_ref + 116,
        y_ref + 77,
        x_ref + 137,
        y_ref + 40,
        x_ref + 122,
        y_ref + 40,
        x_ref + 144,
        y_ref + 4,
        x_ref + 101,
        y_ref + 3,
        outline="",
        fill=pine_shadow_color,
    )

    draw_polygon(
        canvas,
        x_ref + 101,
        y_ref + 117,
        x_ref + 78,
        y_ref + 77,
        x_ref + 86,
        y_ref + 77,
        x_ref + 65,
        y_ref + 40,
        x_ref + 80,
        y_ref + 40,
        x_ref + 59,
        y_ref + 4,
        x_ref + 101,
        y_ref + 3,
        outline="",
        fill=pine_color,
    )

    draw_polygon(
        canvas,
        x_ref + 101,
        y_ref + 3,
        x_ref + 109,
        y_ref + 4,
        x_ref + 109,
        y_ref - 16,
        x_ref + 101,
        y_ref - 20,
        outline="",
        fill=trunk_shadow_color,
    )

    # draw tpine trunk
    draw_polygon(
        canvas,
        x_ref + 101,
        y_ref + 3,
        x_ref + 101,
        y_ref - 16,
        x_ref + 94,
        y_ref - 20,
        x_ref + 94,
        y_ref + 4,
        outline="",
        fill=trunk_color,
    )


def draw_sky(canvas, scene_width, scene_height):

    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, width=0, fill="lightBlue1")

    # call draw_clouds function with clouds randomly
    number = random.randint(3, 7)
    for i in (1, number):
        draw_clouds(canvas, i * 35, 10, i * 70, i * 150)
        pass

    # call function draw_clouds with fixed parameters
    draw_clouds(canvas, 50, 10, 200, 300)
    draw_clouds(canvas, 50, 10, 300, 400)
    draw_clouds(canvas, 70, 10, 550, 500)
    draw_clouds(canvas, 90, 10, 500, 450)

    # draw sun
    draw_oval(canvas, 70, 350, 260, 540, outline="", fill="yellow1")
    draw_oval(canvas, 90, 370, 240, 520, outline="", fill="yellow3")

    # call function draw_seagulls
    draw_seagull(canvas, 50, 100)
    draw_seagull(canvas, 0, 50)
    draw_seagull(canvas, 10, 80)


# function draw_mountains
def draw_mountains(canvas, scene_width, scene_height):
    mountain_shine_color = "steelBlue1"
    mountain_color = "steelBlue3"
    mountain_shadow_color = "steelBlue4"
    snow_color = "snow"
    snow_shadow_color = "snow2"

    # back small mountain
    draw_polygon(canvas, 800, 327, 768, 293, 800, 242, outline="", fill=mountain_color)

    # back Mountain
    draw_polygon(canvas, 534, 322, 774, 109, 354, 109, outline="", fill=mountain_color)

    # back Mountain shadow
    draw_polygon(
        canvas, 534, 322, 673, 198, 583, 130, outline="", fill=mountain_shadow_color
    )

    # back Mountain shine
    draw_polygon(
        canvas,
        534,
        322,
        532,
        280,
        516,
        284,
        506,
        250,
        492,
        253,
        420,
        131,
        421,
        188,
        outline="",
        fill=mountain_shine_color,
    )

    # back mountain snow shadow
    draw_polygon(
        canvas,
        534,
        322,
        571,
        289,
        554,
        288,
        548,
        268,
        outline="",
        fill=snow_shadow_color,
    )

    # back mountain snow
    draw_polygon(
        canvas, 534, 322, 548, 268, 523, 291, 501, 283, outline="", fill=snow_color
    )

    # main Mountain
    draw_polygon(
        canvas,
        717,
        370,
        801,
        242,
        801,
        109,
        386,
        109,
        457,
        164,
        513,
        223,
        555,
        194,
        outline="",
        fill=mountain_color,
    )

    # main Mountain shine
    draw_polygon(
        canvas,
        717,
        370,
        669,
        278,
        630,
        253,
        657,
        247,
        579,
        178,
        555,
        194,
        outline="",
        fill=mountain_shine_color,
    )

    # main Mountain small shine
    draw_polygon(
        canvas,
        501,
        192,
        498,
        180,
        471,
        170,
        473,
        161,
        386,
        109,
        457,
        164,
        481,
        189,
        outline="",
        fill=mountain_shine_color,
    )

    # shadow below big snow
    draw_polygon(
        canvas,
        717,
        370,
        801,
        242,
        800,
        109,
        743,
        109,
        728,
        253,
        outline="",
        fill=mountain_shadow_color,
    )

    # big snow
    draw_polygon(
        canvas,
        717,
        370,
        630,
        275,
        685,
        295,
        728,
        253,
        757,
        288,
        789,
        260,
        outline="",
        fill=snow_color,
    )

    # big snow shadow
    draw_polygon(
        canvas,
        717,
        370,
        789,
        260,
        757,
        288,
        728,
        253,
        outline="",
        fill=snow_shadow_color,
    )

    # shadow below small snow
    draw_polygon(
        canvas, 513, 223, 678, 109, 551, 109, outline="", fill=mountain_shadow_color
    )

    # small snow
    draw_polygon(
        canvas,
        513,
        223,
        543,
        203,
        523,
        201,
        527,
        179,
        501,
        192,
        481,
        189,
        outline="",
        fill=snow_color,
    )

    # small snow shadow
    draw_polygon(
        canvas,
        513,
        223,
        543,
        203,
        532,
        201,
        527,
        179,
        outline="",
        fill=snow_shadow_color,
    )
    pass


# Call the main function so that
# this program will start executing.
main()
