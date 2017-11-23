#! /usr/bin/env python

import sys

from PIL import Image
import cgi, cgitb

print "Content-Type: image/png\n"

background = Image.open("space.png")
bw, bh = background.size

img = Image.open("floor-hole.png")
img = img.convert("RGBA")
data = img.getdata()

h = img.size[0] * bh / bw
background = background.resize((img.size[0], h), Image.ANTIALIAS)
bgdata = background.getdata()

newdata = []
p = 0
#if h > img.size[1]:
#    p = img.size[0] * (h - img.size[1])

for item in data:
    if p < len(bgdata) and item[0] == 255 and item[1] == 0 and item[2] == 255:
        newdata.append(bgdata[p] + (255,))
    else:
        newdata.append(item)
    p += 1

img.putdata(newdata)
img.save(sys.stdout, "PNG")
