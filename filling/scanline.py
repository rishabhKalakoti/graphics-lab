from graphics import *
from drawLine import *
import viewport
class Edge:
	# X, Ymax, 1/m
	def __init__(self, line):
		x0,y0,x1,y1 = line
		if y1 < y0:
			x0,y0,x1,y1 = x1,y1,x0,y0
		self.X = x0
		self.Ymax = y1
		self.Ymin = y0
		self.slope = 10000
		if y1!=y0:
			self.slope = (x1-x0)/(y1-y0)
	def updateSlope(self):
		self.X += self.slope
	def __lt__(self, other):
		if self.Ymin != other.Ymin:
			return self.Ymin < other.Ymin
		return self.X < other.X
	def printInfo(self):
		print(self.X,self.Ymax,self.Ymin,self.slope)
def scanline(lines):
	# edge table
	# active edge table
	ET = list()
	for line in lines:
		if line[1]!=line[3]:
			ET.append(Edge(line))
	ET = sorted(ET)
	AET = list()
	d = viewport.device
	y = d.Ymn
	while (len(ET)>0 or len(AET)>0) and y<=d.Ymx:
		i=0
		while i<len(ET):
			if ET[i].Ymin == y:
				AET.append(ET[i])
				ET.pop(i)
			else:
				i+=1
		i=0
		while i<len(AET):
			if y == AET[i].Ymax:
				AET.pop(i)
			else:
				i+=1
		AET = sorted(AET)
		#fill
		f=0
		for x in range(d.Xmn,d.Xmx+1):
			for edge in AET:
				if int(edge.X) == x:
					f+=1
					f=f%2
			if(f==1):
				viewport.putFill(Point(int(x),y))
		y += 1
		for edge in AET:
			edge.updateSlope()
	
def scanlineInterface():	
	print("Enter the number of points in the polygon.")
	n = int(input())
	l=list()
	print("Enter the coords of points one by one.")
	while n>0:
		x,y = input().split()
		l.append([int(x),int(y)])
		n-=1
	viewport.initWindow()
	# print(l)
	n = len(l)
	lines = list()
	for i in range(n):
		drawLine(l[i%n][0],l[i%n][1],l[(i+1)%n][0],l[(i+1)%n][1])
		lines.append([l[i%n][0],l[i%n][1],l[(i+1)%n][0],l[(i+1)%n][1]])
	scanline(lines)
	viewport.closeWin()
