import transform
import numpy
import math
import time
from graphics import *


def 2dTranslate():
	print("Enter number of vertices")
	n = int(input())
	print("Enter the vertices")
	polygon = []
	for i in range(n):
		x = int(input())
		y = int(input())
		polygon.append([x,y])

	win=GraphWin("Window1",600,600)
	win.setCoords(-300,-300,300,300)
	xaxis=Line(Point(-300,0),Point(300,0))
	yaxis=Line(Point(0,-300),Point(0,300))
	xaxis.draw(win)
	yaxis.draw(win)
	for i in range(len(polygon)):
		k = (i+1)%len(polygon)
		p1 = Point(polygon[i][0],polygon[i][1])
		p2 = Point(polygon[k][0],polygon[k][1])
		line = Line(p1,p2)
		line.setFill('blue')
		line.draw(win)
	print("Enter Tx and Ty for translation")
	

