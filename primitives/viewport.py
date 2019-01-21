from graphics import *

class Screen:
	def __init__(self,Xmn,Ymn,Xmx,Ymx):
		self.Xmn = Xmn
		self.Ymn = Ymn
		self.Xmx = Xmx
		self.Ymx = Ymx

# for a 600 X 400 viewport and device with mid point at 0,0
device = Screen(-300, -200, 300, 200)
viewport = Screen(0, 0, 600, 400)

def viewTransform(Dx, Dy):
	global device
	global viewpot
	vp = viewport
	dv = device
	
	Vx = vp.Xmn+round((Dx-dv.Xmn)*(vp.Xmx-vp.Xmn)/(dv.Xmx-dv.Xmn))
	Vy = vp.Ymn+round((Dy-dv.Ymn)*(vp.Ymx-vp.Ymn)/(dv.Ymx-dv.Ymn))
	return Vx, Vy
	
if __name__ == "__main__":
	win = GraphWin('viewport', 600, 400)
	win.yUp()
	
	x,y = viewTransform(0,0)
	p=Point(x,y)
	p.draw(win)
	x,y = viewTransform(-150,150)
	p=Point(x,y)
	p.draw(win)
	x,y = viewTransform(-100,-100)
	p=Point(x,y)
	
	p.draw(win)
	win.getMouse()
	win.close()
