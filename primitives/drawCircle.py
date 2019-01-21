from graphics import *
from viewport import *

def putpixel(x,y):
	global win
	x,y = viewTransform(x,y)
	p=Point(x,y)
	p.draw(win)
	
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

if __name__ == "__main__":
	#global win
	
	print("Device Window (-300, -200, 300, 200)")
	print("Input Coordinates for center: (x0, y0)")
	x, y = input().split()
	x = int(x)
	y = int(y)
	print("Input radius r:)")
	r = int(input())
	win = GraphWin('line', 600, 400)
	win.yUp()
	drawCircle(x,y,r)
	win.getMouse()
	win.close()
