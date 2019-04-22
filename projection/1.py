#parallel projection (orthogonal) on principle planes
from graphics import *
import math

def line(x0,y0,z0,x1,y1,z1,color):
	ax=x0-(z0*0.3)
	ay=y0-(z0*0.3)
	bx=x1-(z1*0.3)
	by=y1-(z1*0.3)
	line=Line(Point(ax,ay),Point(bx,by));
	line.setFill(color)
	line.setWidth(3)
	line.draw(win_obj)
	
def draw3d(vertex1,vertex2,clr):
	for i in range(n):
		x0 = vertex1[i][0]
		y0 = vertex1[i][1]
		z0 = vertex1[i][2]
		x1 = vertex2[i][0]
		y1 = vertex2[i][1]
		z1 = vertex2[i][2]
		line(x0,y0,z0,x1,y1,z1,clr)

win_obj=GraphWin("Orthogonal Projection",900,900) 
win_obj.setCoords(-300,-300,600,600)
x_axis=Line(Point(-300,0),Point(600,0)) 
y_axis=Line(Point(0,-300),Point(0,600))
z_axis=Line(Point(300,300),Point(-300,-300))      

x_axis.setOutline("Black")
y_axis.setOutline("Black")
z_axis.setOutline("Black")
x_axis.setArrow('both')
y_axis.setArrow('both')
z_axis.setArrow('both')
x_axis.draw(win_obj)
y_axis.draw(win_obj)
z_axis.draw(win_obj)

info_x=Text(Point(580,-10),"x")
info_x.draw(win_obj)
info_y=Text(Point(-10,580),"y")
info_y.draw(win_obj)
info_ny=Text(Point(-280,-280),"z")
info_ny.draw(win_obj)

color1="blue"
color2="red"

vertex1=[]
vertex2=[]

n=int(input())

for i in range(n):
	pointstr=input().split(' ')
	points=[int(i) for i in pointstr]
	x=points[0]
	y=points[1]
	z=points[2]
	vertex1.append([x,y,z])
	x=points[3]
	y=points[4]
	z=points[5]
	vertex2.append([x,y,z])

draw3d(vertex1,vertex2,color1)

print("Select principle plane (xy->1 or yz->2 or xz->3) Enter number :")
k=int(input())

if(k==1):
	for i in range(n):
		vertex1[i][2]=0
		vertex2[i][2]=0

elif (k==2):
	for i in range(n):
		vertex1[i][0]=0
		vertex2[i][0]=0

else:
	for i in range(n):
		vertex1[i][1]=0
		vertex2[i][1]=0

draw3d(vertex1,vertex2,color2)

win_obj.getMouse()
win_obj.close()
