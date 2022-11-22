import os, sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

# blank_slate = Image.new('RGB', (50, 50), color='#32a852')

def draw_room(x_start, y_start, x_end, y_end, image):
    draw = ImageDraw.Draw(image)
    rectangle_shape = [(x_start, y_start), (x_end, y_end)]
    draw.rectangle(rectangle_shape, fill='#000000')
    # image.show()


def connect_rooms():
    pass

# draw_room(5, 5, 15, 15)

# draw = ImageDraw.Draw(blank_slate)
# draw.line([(5, 16), (5, 20)])

# draw_room(5, 20, 25, 25)

# file_name = 'somethin.png'

# blank_slate.save(file_name, 'PNG')

# im = Image.open('picture.ppm')

# print(blank_slate.format, blank_slate.size, blank_slate.mode)