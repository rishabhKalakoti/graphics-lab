from graphics import *

def drawLine(x0, y0, x1, y1):
	win = GraphWin('line', 600, 400)
	win.yUp()
	
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
		p= Point(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
		p.draw(win)
		if D >= 0:
		    y += 1
		    D -= 2*dx
		D += 2*dy
	
	win.getMouse()
	win.close()

if __name__ == "__main__":
	# input
	print("Input Coordinates for point A: (x0, y0)")
	x0, y0 = input().split()
	x0 = int(x0)
	y0 = int(y0)
	print("Input Coordinates for point B: (x1, y1)")
	x1, y1 = input().split()
	x1 = int(x1)
	y1 = int(y1)
	
	drawLine(x0,y0,x1,y1)
