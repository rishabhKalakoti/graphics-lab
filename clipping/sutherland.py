import viewport
from graphics import *
from drawLine import *

surface = None
Left = 1
Right = 2
Bottom = 4
Top = 8
class Rect:
	def __init__(self, px,py,qx,qy):
		points = list()
		self.Xmn = min(px,qx)
		self.Xmx = max(px,qx)
		self.Ymn = min(py,qy)
		self.Ymx = max(py,qy)

def computeOutcode(x,y):
	global surface
	global Top, Bottom, Right, Left
	outcode = 0x0
	if x < surface.Xmn:
		outcode |= Left
	elif x > surface.Xmx:
		outcode |= Right
	if y < surface.Ymn:
		outcode |= Bottom
	elif y > surface.Ymx:
		outcode |= Top
	return outcode

def clipping(x0,y0,x1,y1):
	global surface
	global Top, Bottom, Right, Left
	outcode0 = computeOutcode(x0,y0)
	outcode1 = computeOutcode(x1,y1)
	c=0
	while True:
		if outcode0 == 0 and outcode1 == 0:
			return x0,y0,x1,y1
		if outcode0 & outcode1:
			return False
		
		outcodeOut = max(outcode0,outcode1)
		if x1!=x0:
			if outcodeOut & Top:
				x = x0 + ((x1-x0)*(surface.Ymx-y0)/(y1-y0))
				y = surface.Ymx
			elif outcodeOut & Bottom:
				x = x0 + ((x1-x0)*(surface.Ymn-y0)/(y1-y0))
				y = surface.Ymn
		if y1!=y0:
			if outcodeOut & Right:
				y = y0 + ((y1-y0)*(surface.Xmx-x0)/(x1-x0))
				x = surface.Xmx
			elif outcodeOut & Left:
				y = y0 + ((y1-y0)*(surface.Xmn-x0)/(x1-x0))
				x = surface.Xmn
		
		outcode = computeOutcode(x,y)
		if outcodeOut == outcode0:
			outcode0 = outcode
			x0 = x
			y0 = y
		elif outcodeOut == outcode1:
			outcode1 = outcode
			x1 = x
			y1 = y

def clipInterface():
	print("Give end points of line (x0,y0,x1,y1)")
	x0,y0,x1,y1 = input().split()
	x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)
	print("Give end points of a diagonal of clipping rectangle")
	px,py,qx,qy = input().split()
	px,py,qx,qy = int(px),int(py),int(qx),int(qy)
	
	global surface
	surface = Rect(px,py,qx,qy)
	
	viewport.initWindow()
	drawLine(x0,y0,x1,y1)
	viewport.f = 2
	drawLine(surface.Xmn,surface.Ymn,surface.Xmx,surface.Ymn)
	drawLine(surface.Xmx,surface.Ymn,surface.Xmx,surface.Ymx)
	drawLine(surface.Xmx,surface.Ymx,surface.Xmn,surface.Ymx)
	drawLine(surface.Xmn,surface.Ymx,surface.Xmn,surface.Ymn)
	viewport.f = 3
	
	out = clipping(x0,y0,x1,y1)
	if out == False:
		print("Rejected.")
	else:
		print("Accepted.")
		x0,y0,x1,y1 = out
		x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)
		print(x0,y0,x1,y1)
		drawLine(x0,y0,x1,y1)
	viewport.closeWin()
