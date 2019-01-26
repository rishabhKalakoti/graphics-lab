from graphics import *
import viewport

def putpixel(x,y):
	viewport.putPoint(Point(x,y))

def genEllipse(xc,yc,x,y):
	putpixel(xc+x,yc-y)
	putpixel(xc-x,yc-y)
	putpixel(xc-x,yc+y)
	putpixel(xc+x,yc+y)
def drawEllipse(xc,yc,a,b):
	x=0
	y=b;
	d=int((b*b)-(a*a*b)+(0.25*a*a))
	while(int(((a*a)*(y-0.5)))>((b*b)*(x+1))):
		genEllipse(xc,yc,x,y)
		if d<0 :
			d=d+(b*b)*((2*x)+3)
		else:
			d=d+((b*b)*(2*x+3))+((a*a)*((-2*y)+3))
			y=y-1
		x=x+1
	d=int(((b*b)*((x+0.5)*(x+0.5)))+((a*a)*((y-1)*(y-1)))-((a*a)*(b*b)))
	while y>0:
		   genEllipse(xc,yc,x,y)
		   if(d<0):
		       d=d+((b*b)*(2*x+2))+((a*a)*(((-2)*y)+3))
		       x=x+1
		   else:
		       d=d+((a*a)*(((-2)*y)+3))
		   y=y-1
	genEllipse(xc,yc,x,y)

def drawEllipseInterface():
	print("Input Coordinates for center: (x0, y0)")
	x, y = input().split()
	x = int(x)
	y = int(y)
	print("Input values a and b:")
	a,b = input().split()
	a=int(a)
	b=int(b)
	viewport.initWindow()
	drawEllipse(x,y,a,b)
	viewport.closeWin()
