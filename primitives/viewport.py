from graphics import *
import drawLine
win = None

def initWindow():
	global win
	global device
	win = GraphWin('Screen', viewport.Xmx - viewport.Xmn, viewport.Ymx - viewport.Ymn)
	win.yUp()
	drawLine.drawLine(device.Xmn,(device.Ymx+device.Ymn)//2,device.Xmx,(device.Ymx+device.Ymn)//2)
	drawLine.drawLine((device.Xmx+device.Xmn)//2,device.Ymn,(device.Xmx+device.Xmn)//2,device.Ymx)
def putPoint(p):
	global win
	p = viewTransform(p.x,p.y)
	p.draw(win)
def closeWin():
	global win
	win.getMouse()
	win.close()
	
class Screen:
	def __init__(self,Xmn,Ymn,Xmx,Ymx):
		self.Xmn = Xmn
		self.Ymn = Ymn
		self.Xmx = Xmx
		self.Ymx = Ymx
	def changeCoords(self,Xmn,Ymn,Xmx,Ymx):
		self.Xmn = Xmn
		self.Ymn = Ymn
		self.Xmx = Xmx
		self.Ymx = Ymx
	def printInfo(self):
		print("Xmin:",self.Xmn,"Ymin:",self.Ymn,"Xmax:",self.Xmx,"Ymax:",self.Ymx)
# for a 600 X 400 viewport and device with mid point at 0,0

device = Screen(-300, -200, 300, 200)
viewport = Screen(0, 0, 600, 400)

def changeDeviceCoords():
	global device
	print("Enter device coords as (Xmin Ymin Xmax Ymax)")
	a,b,c,d = map(int, input().split())
	device.changeCoords(a,b,c,d)
	print("Device coordinates changed Successfully")
	print('')
	
def changeViewportCoords():
	global device
	print("Enter viewport coords as (Xmin Ymin Xmax Ymax)")
	a,b,c,d = map(int, input().split())
	viewport.changeCoords(a,b,c,d)
	print("Viewport coordinates changed Successfully")
	print('')
	printCoords()
def printCoords():
	global device, viewport
	print("Device Coords:")
	device.printInfo()
	print("Viewport Coords:")
	viewport.printInfo()
	
def viewTransform(Dx, Dy):
	global device
	global viewpot
	vp = viewport
	dv = device
	Vx = vp.Xmn + round((Dx-dv.Xmn)*(vp.Xmx-vp.Xmn)/(dv.Xmx-dv.Xmn))
	Vy = vp.Ymn + round((Dy-dv.Ymn)*(vp.Ymx-vp.Ymn)/(dv.Ymx-dv.Ymn))
	return Point(Vx,Vy)

if __name__ == "__main__":
	initWindow()
	p=Point(-150,150)
	putPoint(p)
	p=Point(100,100)
	putPoint(p)
	closeWin()
