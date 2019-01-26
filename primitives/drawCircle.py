from graphics import *
import viewport

def putpixel(x,y):
	viewport.putPoint(Point(x,y))

def genCircle(xc,yc,x,y):
	putpixel(xc+x, yc+y)
	putpixel(xc-x, yc+y)
	putpixel(xc+x, yc-y)
	putpixel(xc-x, yc-y)
	putpixel(xc+y, yc+x)
	putpixel(xc-y, yc+x)
	putpixel(xc+y, yc-x)
	putpixel(xc-y, yc-x)
    
def drawCircle(xc,yc,r):
	drawLinesInside(xc,yc,r)
	x=0
	y=r
	d = 3-2*r
	while y>=x:
		x+=1
		if d>0:
			y-=1
			d = d + 4 * (x - y) + 10;
		else:
			d = d + 4 * x + 6; 
		genCircle(xc, yc, x, y)
def drawLinesInside(xc,yc,r):
	x=0
	y=0
	while x*x+y*y<=r*r:
		genCircle(xc,yc,x,y)
		x+=1
		y+=1
	y=0
	while y<=r:
		genCircle(xc,yc,0,y)
		y+=1
def drawCircleInterface():
	print("Input Coordinates for center: (x0, y0)")
	x, y = input().split()
	x = int(x)
	y = int(y)
	print("Input radius r:")
	r = int(input())
	viewport.initWindow()
	drawCircle(x,y,r)
	viewport.closeWin()
