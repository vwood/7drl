import os
from PIL import *
import ImageFont
import ImageDraw
import Image

output_directory = "static/images/"
images = {'wall': ('#', 'grey'),
          'door': ('+', 'brown'),
          'player': ('@', 'black'),
          'water': ('~', 'blue')}

size = 128
margin = 32
width, height = size, size

font = ImageFont.truetype("Inconsolata.otf", size - margin)

for name, (char, color) in images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fx, fy = font.getsize(char)
    xoff, yoff = (width - fx) / 2, (height - fy) / 2
    print char, font.getsize(char), (xoff, yoff)

    draw.text((xoff, yoff), char, font=font, fill=color)
    image.save(output_directory + name + '.png', "PNG")

