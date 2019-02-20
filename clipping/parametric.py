import viewport
from graphics import *
from drawLine import *
surface = None
class Rect:
	def __init__(self, px,py,qx,qy):
		points = list()
		self.Xmn = min(px,qx)
		self.Xmx = max(px,qx)
		self.Ymn = min(py,qy)
		self.Ymx = max(py,qy)

def parametric(x1,y1,x2,y2):
	xmin,ymin = surface.Xmn,surface.Ymn
	xmax,ymax = surface.Xmx,surface.Ymx
	if(x1>=xmin and y1>=ymin and x2<=xmax and y2<=ymax):
		return x1,y1,x2,y2
	tLeft = 0
	tBottom = 0
	tRight = 1
	tTop = 1
	if(x2-x1 != 0):
		tLeft = -(x1-xmin)/(x2-x1)
		tRight = -(x1-xmax)/(x2-x1)
	else:
		y1 = max(y1,ymin)
		y2 = min(y2,ymax)
		return x1,y1,x2,y2
	if(y2-y1 != 0):
		tBottom = -(y1-ymin)/(y2-y1)
		tTop = -(y1-ymax)/(y2-y1)
	else:
		x1 = max(x1,xmin)
		x2 = min(x2,xmax)
		return x1,y1,x2,y2
	tE = max(0,max(tLeft,tBottom))
	tL = min(1,min(tRight,tTop))
	x1_new = x1
	y1_new = y1
	x2_new = x2
	y2_new = y2
	
	if(tE == tBottom):
		y1_new = ymin
		x1_new = x1 + (x2-x1)*tE
	if(tE == tLeft):
		x1_new = xmin
		y1_new = y1 + (y2-y1)*tE
	if(tL == tRight):
		x2_new = xmax
		y2_new = y1 + (y2-y1)*tL
	if(tL == tTop):
		y2_new = ymax
		x2_new = x1 + (x2-x1)*tL
	if(x1_new>xmax or y1_new>ymax or x2_new<xmin or y2_new<ymin):
		return False
		
	#print("Line from ",x1_new,y1_new,"to",x2_new,y2_new)
	return x1_new,y1_new,x2_new,y2_new
def parametricClipInterface():
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
	
	out = parametric(x0,y0,x1,y1)
	if out == False:
		print("Rejected.")
	else:
		print("Accepted.")
		x0,y0,x1,y1 = out
		x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)
		print(x0,y0,x1,y1)
		drawLine(x0,y0,x1,y1)
	viewport.closeWin()
