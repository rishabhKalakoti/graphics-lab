import numpy as np
import math
import time
from graphics import *
def homogeneous(points):
	n = len(points)
	p = []
	for i in range(n):
		x = points[i][0]
		y = points[i][1]
		p.append([x,y,1])
	return p


def shearAboutX(polygon,sh):
	polygon = homogeneous(polygon)
	temp = [[1,0,0],[sh,1,0],[0,0,1]]
	m2 = np.matrix(temp)
	n = len(polygon)
	new_points = []
	for i in range(n):
		m1 = np.matrix(polygon[i])
		temp2 = np.matmul(m1,m2)
		temp2 = np.array(temp2)
		new_points.append(temp2)
	return new_points
def shearAboutY(polygon,sh):
	polygon = homogeneous(polygon)
	temp = [[1,sh,0],[0,1,0],[0,0,1]]
	m2 = np.matrix(temp)
	n = len(polygon)
	new_points = []
	for i in range(n):
		m1 = np.matrix(polygon[i])
		temp2 = np.matmul(m1,m2)
		temp2 = np.array(temp2)
		new_points.append(temp2)
	return new_points
win=GraphWin("Window1",600,600)
win.setCoords(-300,-300,300,300)
xaxis=Line(Point(-300,0),Point(300,0))
yaxis=Line(Point(0,-300),Point(0,300))
xaxis.draw(win)
yaxis.draw(win)
polygon = [[10,15], [20,25], [30,20]]
for i in range(len(polygon)):
	k = (i+1)%len(polygon)
	p1 = Point(polygon[i][0],polygon[i][1])
	p2 = Point(polygon[k][0],polygon[k][1])
	line = Line(p1,p2)
	line.setFill('blue')
	line.draw(win)

polygon = shearAboutX(polygon,0.5)
for i in range(len(polygon)):
	k = (i+1)%len(polygon)
	p1 = Point(polygon[i][0][0],polygon[i][0][1])
	p2 = Point(polygon[k][0][0],polygon[k][0][1])
	line = Line(p1,p2)
	line.setFill('red')
	line.draw(win)
print(polygon)
	
time.sleep(10)
