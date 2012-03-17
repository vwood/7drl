#!/usr/bin/env python2

import os
from PIL import *
import ImageFont
import ImageDraw
import Image

output_directory = "static/images/"
text_images = {'Blank': (' ', 'black'),
               'Rock_Wall': ('#', 'grey'),
               'Stone_Wall': ('#', 'darkgrey'),
               'Dirt_Wall': ('#', 'brown'),
               'Red_Wall': ('#', 'red'),
               'Slime_Wall': ('#', 'forestgreen'),
               'Door': ('+', 'brown'),
               'Rock_Floor': ('.', 'lightgrey'),
               'Dirt_Floor': ('.', 'brown'),
               'Stone_Floor': ('.', 'darkgrey'),
               'Red_Floor': ('.', 'red'),
               'Moss_Floor': ('.', 'forestgreen'),
               'Corpse': (unichr(216), 'darkred'),
               'Cat-dog': (unichr(162), 'orange'),
               'Rogue': ('@', 'white'),
               'Shopkeeper': ('S', 'darkblue'),
               'Janitor': ('J', 'brown'),
               'Dwarf': (unichr(181), 'honeydew'), # I'm hilarious
               'Bard': (unichr(223), 'goldenrod'),
               'Goblin': ('g', 'green'),
               'Cthulhu': (unichr(199), 'green'),
               'Water': ('~', 'blue'),
               'Lava': ('~', 'red'),
               'Wand': ('/', 'brown'),
               'Gold_Sword': ('(', 'gold'),
               'Crystal_Sword': ('(', 'azure'),
               'Silver_Sword': ('(', 'silver'),
               'Tree': ('T', 'green'),
               'Attack': ('A', 'red')}

smaller_text_images = {'Kobold_Baby': ('k', 'brown'),
                       'Spaniard': (unichr(209), 'white'),
                       'Hat_Guy': (unichr(212), 'white')}

underlined_text_images = {'Stairs': ('>', '#0077cc'), # Default link color in chrome
                          'Exit': ('.', '#0077cc'),
                          'Open_Door': ('\'', '#0077cc')}

line_images = {'Wizard': ([(0.3,0.2), (0.7,0.8), (0.5,0.5),
                           (0.3,0.8), (0.5,0.5)], 'purple')}

margin = -6
width, height = 64, 96
size = height
line_width = size / 16

font = ImageFont.truetype("Inconsolata.otf", size - margin)

for name, (char, color) in text_images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fx, fy = font.getsize(char)
    xoff, yoff = (width - fx) / 2, (height - fy) / 2
    draw.text((xoff, yoff), char, font=font, fill=color)
    image.save(output_directory + name + '.png', "PNG")

for name, (char, color) in smaller_text_images.iteritems():
    font2 = ImageFont.truetype("Inconsolata.otf", size - margin - 10)
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fx, fy = font2.getsize(char)
    xoff, yoff = (width - fx) / 2, (height - fy) / 2
    draw.text((xoff, yoff), char, font=font2, fill=color)
    image.save(output_directory + name + '.png', "PNG")

for name, (char, color) in underlined_text_images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    fx, fy = font.getsize(char)
    xoff, yoff = (width - fx) / 2, (height - fy) / 2
    draw.text((xoff, yoff), char, font=font, fill=color)
    draw.line([(0.2 * width, 0.9 * height),
               (0.8 * width, 0.9 * height)], width = line_width, fill=color)
    image.save(output_directory + name + '.png', "PNG")

for name, (xys, color) in line_images.iteritems():
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    xys = [(x * width, y * height) for (x,y) in xys]
    draw.line(xys, width = line_width, fill=color)
    image.save(output_directory + name + '.png', "PNG")
