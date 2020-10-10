#! /usr/bin/python

from PIL import Image
import sys

def get_main_color(file):
    img = Image.open(file)
    colors = img.getcolors(256*1024) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        #Too many colors in the image
    return (0, 0, 0)

if get_main_color('screen.png') != (0, 0, 0):
    print('Aw,snap')
    sys.exit(1)