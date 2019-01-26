from graphics import *
from drawLine import *
import viewport

def drawPolygonInterface():
	print("Enter the number of points in the polygon.")
	n = int(input())
	l=list()
	print("Enter the coords of points one by one.")
	while n>0:
		x,y = input().split()
		l.append([int(x),int(y)])
		n-=1
	viewport.initWindow()
	# print(l)
	n = len(l)
	for i in range(n):
		drawLine(l[i%n][0],l[i%n][1],l[(i+1)%n][0],l[(i+1)%n][1])
	viewport.closeWin()	
