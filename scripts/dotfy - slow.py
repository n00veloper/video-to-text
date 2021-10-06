import cv2
import os
import numpy as np
from PIL import Image
path = input("video path:... ")
vidcap = cv2.VideoCapture(path)
def getframe(time):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, time*1000)
    hasframes, image = vidcap.read()
    if hasframes:
        if not os.path.isdir("./frames"):
            os.mkdir("./frames")
        cv2.imwrite("./frames/image"+str(count)+".jpg", image)
        return hasframes
sec = 0
count = 1
fps = float(input("frames per second "))
pathOut = input("video name?: ")
colorfull = input("colors (y/n)")
success = getframe(sec)
while success:
    count += 1
    sec += fps
    sec = round(sec, 2)
    success = getframe(sec)

def edit(file, color = False):
    with Image.open(file) as size:
        width, height = size.size
        data = np.zeros((height, width, 3), dtype=np.uint8)
        size = size.convert("RGB")
        pos = [0,0]
        while True:
            red, green, blue = size.getpixel((pos[0], pos[1]))
            b = [0, 0, 0]
            w = [255, 255, 255]
            ii = 0
            old = pos[0]
            jmp = 6
            end = jmp * jmp
            if red+green+blue >= 0:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    b,b,b,b,b,b,
                    b,b,b,b,b,b,
                    b,b,w,w,b,b,
                    b,b,w,w,b,b,
                    b,b,b,b,b,b,
                    b,b,b,b,b,b
                ]
            if red+green+blue > 128:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    b,b,b,b,b,b,
                    b,w,b,b,w,b,
                    b,b,w,w,b,b,
                    b,b,w,w,b,b,
                    b,w,b,b,w,b,
                    b,b,b,b,b,b
                ]
            if red+green+blue > 255:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    b,b,b,b,b,b,
                    b,w,w,w,w,b,
                    b,w,w,w,w,b,
                    b,w,w,w,w,b,
                    b,w,w,w,w,b,
                    b,b,b,b,b,b
                ]
            if red+green+blue > 383:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    b,b,w,w,b,b,
                    b,w,w,w,w,b,
                    w,w,b,b,w,w,
                    w,w,b,b,w,w,
                    b,w,w,w,w,b,
                    b,b,w,w,b,b
                ]
            if red+green+blue > 510:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    w,b,w,w,b,w,
                    b,w,w,w,w,b,
                    w,w,b,b,w,w,
                    w,w,b,b,w,w,
                    b,w,w,w,w,b,
                    w,b,w,w,b,w
                ]
            if red+green+blue > 638:
                w = [150, 150, 150]
                if color:
                    w = [red, green, blue]
                draw = [
                    b,b,w,w,b,b,
                    b,w,w,w,w,b,
                    w,w,w,w,w,w,
                    w,w,w,w,w,w,
                    b,w,w,w,w,b,
                    b,b,w,w,b,b
                ]
            while ii < end:
                data[pos[1]-1:pos[1]+1, pos[0]-1:pos[0]+1] = draw[ii]
                pos[0] += 1
                if pos[0] > old + jmp -1:
                    pos[1] += 1
                    pos[0] -= jmp
                ii += 1
            pos[0] += 6
            if pos[0] < width:
                pos[1] -= jmp
            if pos[0] >= width:
                pos[0] = 0
                pos[1] += jmp
            if pos[1] >= height:
                break
    img = Image.fromarray(data, 'RGB')
    img.save(file)

pathIn = "./frames"
frame_array = []
first = True
for i in range(1, count):
    filename = pathIn+"/image"+str(i)+".jpg"
    print(str(i)+" out of "+str(count))
    if colorfull == "y":
        edit(filename, True)
    else:
        edit(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    frame_array.append(img)
    size = (width, height)
    if first:
        out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"mp4v"), fps / (fps * fps), size)
        first = False
    if len(frame_array) > 10:
        for i in range(len(frame_array)):
            out.write(frame_array[i])
        frame_array = []
if len(frame_array) > 0:
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    frame_array = []
out.release()
for f in os.listdir(pathIn):
    os.remove(os.path.join(pathIn, f))