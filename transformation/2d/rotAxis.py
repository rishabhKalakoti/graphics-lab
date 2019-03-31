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
	
def translate(points,t):
	tx = t[0]
	ty = t[1]
	temp = [[1,0,0],[0,1,0],[tx,ty,1]]
	m2 = np.matrix(temp)
	n = len(points)
	new_points = []
	for i in range(n):
		m1 = np.matrix(points[i])
		temp2 = np.matmul(m1,m2)
		temp2 = np.array(temp2)
		new_points.append(temp2)
	return new_points
def rotate(points,angle):
	 angle = math.radians(angle)
	 c = math.cos(angle)
	 s = math.sin(angle)
	 r = [[c,s,0],[-s,c,0],[0,0,1]]
	 m2 = np.matrix(r)
	 n = len(points)
	 new_points = []
	 for i in range(n):
	 	m1 = np.matrix(points[i])
	 	temp = np.matmul(m1,m2)
	 	temp = np.array(temp)
	 	new_points.append(temp)
	 return new_points

def rotationAboutAxis(polygon,angle,axis):
	polygon = homogeneous(polygon)
	x0,y0,x1,y1 = axis
	tx = -x0
	ty = -y0
	polygon = translate(polygon,[tx,ty])
	#angle between line and x-axis
	x2 = x1-x0
	y2 = y1-y0
	x_axis = [1,0,1]
	temp = (x2)/math.sqrt(x2*x2 + y2*y2)
	if(temp<0):
		temp = -temp
	angle2 = math.acos(temp)
	angle2 = math.degrees(angle2)
	#print(angle2)
	if(x1>=0 and y1>=0):
		polygon = rotate(polygon,-angle2)
	elif(x1>=0 and y1<=0):
		polygon = rotate(polygon,angle2)
	elif(x1<=0 and y1<=0):
		polygon = polygon(polygon,-angle2)
	elif(x1<=0 and y1>=0):
		polygon = polygon(polygon,angle2)
	polygon = rotate(polygon,angle)
	if(x1>=0 and y1>=0):
		polygon = rotate(polygon,angle2)
	elif(x1>=0 and y1<=0):
		polygon = rotate(polygon,-angle2)
	elif(x1<=0 and y1<=0):
		polygon = polygon(polygon,angle2)
	elif(x1<=0 and y1>=0):
		polygon = polygon(polygon,-angle2)
	polygon = translate(polygon,[-tx,-ty])
	return polygon
	
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

polygon = rotationAboutAxis(polygon,90,(10,0,0,10))
for i in range(len(polygon)):
	k = (i+1)%len(polygon)
	p1 = Point(polygon[i][0][0],polygon[i][0][1])
	p2 = Point(polygon[k][0][0],polygon[k][0][1])
	line = Line(p1,p2)
	line.setFill('red')
	line.draw(win)
print(polygon)
	
time.sleep(10)
