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
		z = points[i][2]
		p.append([x,y,z,1])
	return p
	
def translate(points,t):
	tx = t[0]
	ty = t[1]
	tz = t[2]
	temp = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[tx,ty,tz,1]]
	m2 = np.matrix(temp)
	n = len(points)
	new_points = []
	for i in range(n):
		m1 = np.matrix(points[i])
		temp2 = np.matmul(m1,m2)
		temp2 = np.array(temp2)
		new_points.append(temp2)
	return new_points
def rotatex(points,angle):
	 angle = math.radians(angle)
	 c = math.cos(angle)
	 s = math.sin(angle)
	 r = [[1,0,0,0],[0,c,s,0],[0,-s,c,0],[0,0,0,1]]
	 m2 = np.matrix(r)
	 n = len(points)
	 new_points = []
	 for i in range(n):
	 	m1 = np.matrix(points[i])
	 	temp = np.matmul(m1,m2)
	 	temp = np.array(temp)
	 	new_points.append(temp)
	 return new_points
def rotatey(points,angle):
	 angle = math.radians(angle)
	 c = math.cos(angle)
	 s = math.sin(angle)
	 r = [[c,0,-s,0],[0,1,0,0],[s,0,c,0],[0,0,0,1]]
	 m2 = np.matrix(r)
	 n = len(points)
	 new_points = []
	 for i in range(n):
	 	m1 = np.matrix(points[i])
	 	temp = np.matmul(m1,m2)
	 	temp = np.array(temp)
	 	new_points.append(temp)
	 return new_points
def rotatez(points,angle):
	 angle = math.radians(angle)
	 c = math.cos(angle)
	 s = math.sin(angle)
	 r = [[c,s,0,0],[-s,c,0,0],[0,0,1,0],[0,0,0,1]]
	 m2 = np.matrix(r)
	 n = len(points)
	 new_points = []
	 for i in range(n):
	 	m1 = np.matrix(points[i])
	 	temp = np.matmul(m1,m2)
	 	temp = np.array(temp)
	 	new_points.append(temp)
	 return new_points
def scale(points,s):
	sx = s[0]
	sy = s[1]
	sz = s[2]
	temp = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
	m2 = np.matrix(temp)
	n = len(points)
	new_points = []
	for i in range(n):
		m1 = np.matrix(points[i])
		temp2 = np.matmul(m1,m2)
		temp2 = np.array(temp2)
		new_points.append(temp2)
	return new_points


def rotateAboutAxis(polygon,angle,axis):
	polygon = homogeneous(polygon)
	x0,y0,z0,x1,y1,z1 = axis
	A = x1-x0
	B = y1-y0
	C = z1-z0
	polygon = translate(polygon,[-x0,-y0,-z0])
	
	L = math.sqrt(A*A + B*B + C*C)
	V = math.sqrt(B*B + C*C)
	temp1 = B/V
	angle1 = math.asin(temp1)
	angle1 = math.degrees(angle1)
	polygon = rotatex(polygon,angle1)
	
	temp2 = V/L
	angle2 = math.acos(temp2)
	angle2 = math.degrees(angle2)
	polygon = rotatey(polygon,-angle2)
	
	polygon = rotatez(polygon,angle)
	
	polygon = rotatey(polygon,angle2)
	
	polygon = rotatex(polygon,-angle1)
	
	polygon = translate(polygon,[x0,y0,z0])
	
	return polygon
win=GraphWin("Window1",600,600)
win.setCoords(-300,-300,300,300)
xaxis=Line(Point(-300,0),Point(300,0))
yaxis=Line(Point(0,-300),Point(0,300))
xaxis.draw(win)
yaxis.draw(win)
polygon = [[10,15,20], [20,25,30], [30,20,50]]
"""
for i in range(len(polygon)):
	k = (i+1)%len(polygon)
	p1 = Point(polygon[i][0],polygon[i][1])
	p2 = Point(polygon[k][0],polygon[k][1])
	line = Line(p1,p2)
	line.setFill('blue')
	line.draw(win)
	"""
print(polygon)
polygon = rotateAboutAxis(polygon,0,(0,0,0,1,1,1))
print(polygon)
"""
for i in range(len(polygon)):
	k = (i+1)%len(polygon)
	p1 = Point(polygon[i][0][0],polygon[i][0][1])
	p2 = Point(polygon[k][0][0],polygon[k][0][1])
	line = Line(p1,p2)
	line.setFill('red')
	line.draw(win)"""
time.sleep(10)



