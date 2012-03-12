import os
from PIL import *
import ImageFont
import ImageDraw
import Image
import cairo

output_directory = "static/images/"
text_images = {'wall1': ('#', 'grey'),
               'wall2': ('#', 'darkgrey'),
               'wall3': ('#', 'brown'),
               'wall4': ('#', 'red'),
               'door': ('+', 'brown'),
               'opendoor': ('\'', 'brown'),
               'floor1': ('.', 'lightgrey'),
               'floor2': ('.', 'brown'),
               'floor3': ('.', 'darkgrey'),
               'floor4': ('.', 'red'),
               'stairs': ('>', 'grey'),
               'player': ('@', 'black'),
               'shopkeeper': ('S', 'darkblue'),
               'janitor': ('J', 'brown'),
               'bard': (unichr(223), 'goldenrod'),
               'goblin': ('g', 'green'),
               'cthulhu': (unichr(199), 'green'),
               'water': ('~', 'blue'),
               'lava': ('~', 'red'),
               'wand': ('/', 'brown')}

line_images = {'chest': ([(0.2,0.8), (0.2,0.5), (0.8,0.5),
                          (0.2,0.5), (0.3,0.3), (0.7,0.3),
                          (0.8,0.5), (0.8,0.8), (0.2,0.8)], 'brown'),
               'wizard': ([(0.3,0.2), (0.7,0.8), (0.5,0.5),
                           (0.3,0.8), (0.5,0.5)], 'purple')}

size = 128
margin = 32
width, height = size, size
line_width = size / 16

font = ImageFont.truetype("Inconsolata.otf", size - margin)

for name, (char, color) in text_images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fx, fy = font.getsize(char)
    xoff, yoff = (width - fx) / 2, (height - fy) / 2
    draw.text((xoff, yoff), char, font=font, fill=color)
    image.save(output_directory + name + '.png', "PNG")

for name, (xys, color) in line_images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    xys = [(x * width, y * height) for (x,y) in xys]
    draw.line(xys, width = line_width, fill=color)
    image.save(output_directory + name + '.png', "PNG")
