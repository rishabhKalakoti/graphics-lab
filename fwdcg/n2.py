#paraller projection (orthogonal) on arbitrary plane
from graphics import *
import math

def translate():
	for i in range(n):
		vertex1[i][0]=vertex1[i][0]+tx
		vertex1[i][1]=vertex1[i][1]+ty
		vertex1[i][2]=vertex1[i][2]+tz
		vertex2[i][0]=vertex2[i][0]+tx
		vertex2[i][1]=vertex2[i][1]+ty
		vertex2[i][2]=vertex2[i][2]+tz

def line(x0,y0,z0,x1,y1,z1,color):
	ax=x0-(z0*0.3)
	ay=y0-(z0*0.3)
	bx=x1-(z1*0.3)
	by=y1-(z1*0.3)
	line=Line(Point(ax,ay),Point(bx,by));
	line.setFill(color)
	line.setWidth(3)
	line.draw(win_obj)
	
def draw3d(clr):
	for i in range(n):
		x0=vertex1[i][0]
		y0=vertex1[i][1]
		z0=vertex1[i][2]
		x1=vertex2[i][0]
		y1=vertex2[i][1]
		z1=vertex2[i][2]
		line(x0,y0,z0,x1,y1,z1,clr)

def arbitraryplane():
	for i in range(n):
		x0=vertex1[i][0]
		y0=vertex1[i][1]
		z0=vertex1[i][2]
		x1=vertex2[i][0]
		y1=vertex2[i][1]
		z1=vertex2[i][2]
		x0=(x0*(d1-a*n1)-y0*a*n2-z0*a*n3+a*d0)/d1
		y0=(y0*(d1-b*n2)-x0*b*n1-z0*b*n3+b*d0)/d1
		z0=(z0*(d1-c*n3)-x0*c*n1-y0*c*n2+c*d0)/d1
		x1=(x1*(d1-a*n1)-y1*a*n2-z1*a*n3+a*d0)/d1
		y1=(y1*(d1-b*n2)-x1*b*n1-z1*b*n3+b*d0)/d1
		z1=(z1*(d1-c*n3)-x1*c*n1-y1*c*n2+c*d0)/d1
		vertex1[i]=[x0,y0,z0]
		vertex2[i]=[x1,y1,z1]

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

tx=int(input("x translate : "))
ty=int(input("y translate : "))
tz=int(input("z translate : "))
translate()

draw3d(color1)

print("Enter vector normal :")
n1=int(input())
n2=int(input())
n3=int(input())
a=-n1
b=-n2
c=-n3
print("Enter reference point :")
R0=input().split()
d0=int(R0[0])*n1+int(R0[1])*n2+int(R0[2])*n3
d1=a*n1+b*n2+c*n3

arbitraryplane()

draw3d(color2)

win_obj.getMouse()
win_obj.close()