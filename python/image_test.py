import time as tm
import numpy as np
import json as js
import random as rd
from PIL import Image as im

config = js.load(open("config/test.json"))

width = config["width"]
height = config["height"]
iterations = config["iterations"]

def formatTime(time):
	ms = ""
	minutes = time // 60
	seconds = time - minutes * 60
	seconds = round(seconds, 2)
	ms = "{:02d}".format(int(minutes))
	ms += ":"
	ms += "{:05.2f}".format(seconds)
	return ms

def getWorkingTime(start, end):
	time = end - start
	formatedTime = formatTime(time)
	return formatedTime

def create_image(w, h):
	image_data = np.full((w, h, 3), (0,0,0))
	red = 0
	green = 0
	blue = 0
	for c in range(w):
		r_number = rd.randint(0,64)
		g_number = rd.randint(0,64)
		b_number = rd.randint(0,64)
		red = (red + r_number)%255
		green = (green + g_number)%255
		blue = (blue + b_number)%255
		for r in range(h):
			image_data[r][c] = (red, green, blue)
	data = np.array(np.round(image_data), dtype="uint8")
	image = im.fromarray(data)
	image.save("output/test" + "{:04}".format(w) + ".jpg")

for i in range(iterations):
	w = width * pow(2, i)
	h = height * pow(2, i)
	print("Creating image of " + str(w) + " x " + str(h) + " pixels...", end="\n")
	start = tm.time()
	create_image(w,h)
	time = tm.time()
	print("This took me " + getWorkingTime(start, time), end="\n")