from graphics import *
import drawLine
win = None
screenArr = list(list())
f = 0
def initWindow():
	global win
	global f
	global device
	global vp
	global screenArr
	win = GraphWin('Screen', vp.Xmx - vp.Xmn, vp.Ymx - vp.Ymn)
	#win.setCoords(device.Xmn,device.Ymn,device.Xmx,device.Xmx)
	win.yUp()
	for i in range(vp.Ymn,vp.Ymx+1):
		row = list()
		for j in range(vp.Xmn,vp.Xmx+1):
			row.append(0)
		screenArr.append(row)
	drawLine.drawLine(device.Xmn,(device.Ymx+device.Ymn)//2,device.Xmx,(device.Ymx+device.Ymn)//2)
	drawLine.drawLine((device.Xmx+device.Xmn)//2,device.Ymn,(device.Xmx+device.Xmn)//2,device.Ymx)
	for i in range(vp.Ymn,vp.Ymx+1):
		for j in range(vp.Xmn,vp.Xmx+1):
			screenArr[i][j]=0
	f = 1
def putPoint(p):
	global win
	global screenArr
	p = viewTransform(p.getX(),p.getY())
	screenArr[p.y][p.x] = 1
	p.setOutline("Black")
	if f==1:
		p.setOutline("Blue")
	elif f==2:
		p.setOutline("Yellow")
	elif f==3:
		p.setOutline("Red")
	p.draw(win)
def putFill(p):
	global win
	global screenArr
	p = viewTransform(p.getX(),p.getY())
	screenArr[p.y][p.x] = 2
	p.setOutline("Green")
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

device = Screen(-200, -200, 200, 200)
vp = Screen(0, 0, 400, 400)

def changeDeviceCoords():
	global device
	print("Enter device coords as (Xmin Ymin Xmax Ymax)")
	a,b,c,d = map(int, input().split())
	device.changeCoords(a,b,c,d)
	print("Device coordinates changed Successfully")
	print('')
	
def changeViewportCoords():
	global vp
	print("Enter viewport coords as (Xmin Ymin Xmax Ymax)")
	a,b,c,d = map(int, input().split())
	vp.changeCoords(a,b,c,d)
	print("Viewport coordinates changed Successfully")
	print('')
	printCoords()
def printCoords():
	global device, vp
	print("Device Coords:")
	device.printInfo()
	print("Viewport Coords:")
	vp.printInfo()
	
def viewTransform(Dx, Dy):
	global device
	global vp
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
