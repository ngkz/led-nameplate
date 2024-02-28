#!/usr/bin/env python3
from PIL import Image, ImageDraw
import random
import math

speed = 2
fps = 15
length = 3
frame_img_width = 48
frame_width = 44
width = math.ceil(speed * length * fps)
height = 11
im = Image.new("1", (width, height), "black")

frames = []

random.seed(15)
for i in range(50):
    dr = ImageDraw.Draw(im)
    x = random.randrange(width)
    y = random.randrange(height)
    length = random.randint(5, 20)
    dr.line([(x, y), (x + length, y)], fill="white", width=1)
    if x + length > width:
        dr.line([(0, y), (x + length - width, y)], fill="white", width=1)

for off in range(0, width, speed):
    x = width - off
    frame = Image.new("1", (frame_img_width, height))
    cropped = im.crop((x, 0, x + frame_width, height))
    frame.paste(cropped, (0, 0))
    if x + frame_width > width:
        cropped = im.crop((0, 0, x + frame_width - width, height))
        frame.paste(cropped, (width - x, 0))
    frames.append(frame)

frames[0].save('matrix.gif', save_all=True, append_images=frames[1:], optimize=False, duration=1000/fps, loop=0)

data = Image.new("1", (frame_img_width * len(frames), height))
for i, frame in enumerate(frames):
    data.paste(frame, (i * frame_img_width, 0))
data.save("data-matrix.png")
