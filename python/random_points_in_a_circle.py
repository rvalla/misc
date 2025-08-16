import random as rd
import time as tm
import math
import matplotlib.pyplot as plt

cycles = [50,100,500,1000,5000,10000]
start_time = None
print("--- RANDOM POINTS IN A CIRCLE: Testing alternatives", end="\n")
print("Number of points: " + str(cycles), end="\n")

def get_polar_point(radious):
  a = rd.random() * math.pi*2
  h = rd.random() * radious
  return (a, h), (math.cos(a) * h, math.sin(a) * h)

def get_pitagoras_point(radious):
  x = min(rd.random(), rd.random()) * radious
  if rd.random() < 0.5:
    x = x*-1
  y_limit = math.sqrt(radious*radious - x*x)
  y = rd.random() * y_limit * 2 - y_limit
  return (x, y)

def get_pitagoras_point_rq(radious):
  x = min(rd.random(), rd.random()) * radious
  y = rd.random() * (math.sqrt(radious*radious - x*x))
  return (rd.choice([-1,1])*x, rd.choice([-1,1])*y)

def get_pitagoras_point_crq(radious):
  if rd.random() < 0.5:
    x = min(rd.random(), rd.random()) * radious
    y = rd.random() * (math.sqrt(radious*radious - x*x))
  else:
    y = min(rd.random(), rd.random()) * radious
    x = rd.random() * (math.sqrt(radious*radious - y*y))
  return (rd.choice([-1,1])*x, rd.choice([-1,1])*y)

def visualize(x, y, ox, oy, title):
  f = plt.figure(figsize=(12,8))
  plt.subplot2grid((2, 3), (0, 0), 2, 2)
  plt.suptitle(title, fontsize=20)
  plt.scatter(x, y, marker=".")
  plt.subplot2grid((2, 3), (0, 2), 1, 1)
  plt.hist(ox, 10)
  plt.subplot2grid((2, 3), (1, 2), 1, 1)
  plt.hist(oy, 10)
  plt.tight_layout()
  plt.savefig("output/random_points_in_a_circle_" + title + ".png")
  plt.close(f)
  print("Data visualization saved!", end="\n")

def format_time(time):
	ms = ""
	minutes = time // 60
	seconds = time - minutes * 60
	seconds = round(seconds, 2)
	ms = "{:02d}".format(int(minutes))
	ms += ":"
	ms += "{:06.3f}".format(seconds)
	return ms

def get_working_time(start, end):
	time = end - start
	formatedTime = format_time(time)
	return formatedTime

print("Generating points using polar coordinates", end="\n")
start_time = tm.time()
for c in cycles:
  polar_angles = []
  polar_magnitudes = []
  polar_x = []
  polar_y = []
  for i in range(c):
    am, p = get_polar_point(25)
    polar_angles.append(am[0])
    polar_magnitudes.append(am[1])
    polar_x.append(p[0])
    polar_y.append(p[1])
  visualize(polar_x, polar_y, polar_angles, polar_magnitudes, str(c) + "p polar generated points")
print("This took me " + get_working_time(start_time, tm.time()), end="\n")

print("Generating points with pitagoras equation", end="\n")
start_time = tm.time()
for c in cycles:
  pitagoras_x = []
  pitagoras_y = []
  for i in range(c):
    p = get_pitagoras_point(25)
    pitagoras_x.append(p[0])
    pitagoras_y.append(p[1])
  visualize(pitagoras_x, pitagoras_y, pitagoras_x, pitagoras_y, str(c) + "p pitagoras")
print("This took me " + get_working_time(start_time, tm.time()), end="\n")

print("Generating points with pitagoras equation selecting a random quadrant", end="\n")
start_time = tm.time()
for c in cycles:
  pitagoras_x = []
  pitagoras_y = []
  for i in range(c):
    p = get_pitagoras_point_rq(25)
    pitagoras_x.append(p[0])
    pitagoras_y.append(p[1])
  visualize(pitagoras_x, pitagoras_y, pitagoras_x, pitagoras_y, str(c) + "p pitagoras random quadrant")
print("This took me " + get_working_time(start_time, tm.time()), end="\n")

print("Generating points with pitagoras equation selecting a random quadrant", end="\n")
start_time = tm.time()
for c in cycles:
  pitagoras_x = []
  pitagoras_y = []
  for i in range(c):
    p = get_pitagoras_point_crq(25)
    pitagoras_x.append(p[0])
    pitagoras_y.append(p[1])
  visualize(pitagoras_x, pitagoras_y, pitagoras_x, pitagoras_y, str(c) + "p pitagoras corrected random quadrant")
print("This took me " + get_working_time(start_time, tm.time()), end="\n")
