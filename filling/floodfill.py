from graphics import *
from drawLine import *
import viewport

def check(x,y):
	screenArr = viewport.screenArr
	global device
	global screen
	d = viewport.device
	vp = viewport.vp
	p = Point(x,y)
	p = viewport.viewTransform(x,y)
	if p.x<=vp.Xmx and p.x>=vp.Xmn and p.y<=vp.Ymx and p.y>=vp.Ymn:
		if screenArr[p.y][p.x]!=2 and screenArr[p.y][p.x]!=1:
			return True
	return False
def floodFill(x,y):
	global screenArr
	global vp
	stack = list()
	stack.append(Point(x,y))
	while len(stack)>0:
		pt = stack.pop(len(stack)-1)
		if check(pt.x,pt.y)==True:
			# colour
			viewport.putFill(pt)
			# push neighbours
			if check(pt.x,pt.y+1)==True:
				stack.append(Point(pt.x,pt.y+1))
			if check(pt.x+1,pt.y)==True:
				stack.append(Point(pt.x+1,pt.y))
			if check(pt.x,pt.y-1)==True:
				stack.append(Point(pt.x,pt.y-1))
			if check(pt.x-1,pt.y)==True:
				stack.append(Point(pt.x-1,pt.y))
			

def floodfillInterface():
	print("Enter the number of points in the polygon.")
	n = int(input())
	l=list()
	print("Enter the coords of points one by one.")
	while n>0:
		x,y = input().split()
		l.append([int(x),int(y)])
		n-=1
	print("Give the coords of the seed")
	x,y = input().split()
	x=int(x)
	y=int(y)
	viewport.initWindow()
	# print(l)
	n = len(l)
	for i in range(n):
		drawLine(l[i%n][0],l[i%n][1],l[(i+1)%n][0],l[(i+1)%n][1])
	floodFill(x,y)
	viewport.closeWin()
