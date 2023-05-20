import pyautogui
from PIL import Image
import imagehash
from tkinter import *
import os
import time


MAX_PAGES = 10


dirname = "images_" + str(int(time.time()))

# create directory
os.mkdir(dirname)

pyautogui.sleep(5)

count = {}
imagemap = {}

for i in range(MAX_PAGES):
    pic: Image = pyautogui.screenshot()

    y = 304
    for j in range(0, 10):
        x = 607
        for k in range(0, 1):
            cropped = pic.crop((x, y, x + 50, y + 50))

            importance = 0
            if k == 0:
                importance = 1
            elif k == 1:
                importance = 1
            else:
                importance = 1

            hash = imagehash.average_hash(cropped)
            if hash in count:
                count[hash] += importance
            else:
                count[hash] = importance
            
            imagemap[hash] = cropped

            x += 52
        
        y += 55

    pyautogui.click(1020, 880)

    pyautogui.sleep(0.7)

idx = 0
for(hash, count) in count.items():
    if count >= 1:
        imagemap[hash].save(f"{dirname}/{'%05d' % count}점 - {hash}.png")

        idx += 1
