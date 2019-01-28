from graphics import *
import viewport

def drawLine(x0, y0, x1, y1):
	dx = x1 - x0
	dy = y1 - y0

	xsign = 1 if dx > 0 else -1
	ysign = 1 if dy > 0 else -1

	dx = abs(dx)
	dy = abs(dy)

	if dx > dy:
		xx, xy, yx, yy = xsign, 0, 0, ysign
	else:
		dx, dy = dy, dx
		xx, xy, yx, yy = 0, ysign, xsign, 0

	D = 2*dy - dx
	y = 0

	for x in range(dx + 1):
		p = Point(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
		viewport.putPoint(p)
		if D >= 0:
		    y += 1
		    D -= 2*dx
		D += 2*dy

def drawLineInterface():
	# input
	print("Input Coordinates for point A: (x0, y0)")
	x0, y0 = input().split()
	x0 = int(x0)
	y0 = int(y0)
	print("Input Coordinates for point B: (x1, y1)")
	x1, y1 = input().split()
	x1 = int(x1)
	y1 = int(y1)
	viewport.initWindow()
	drawLine(x0,y0,x1,y1)
	viewport.closeWin()
