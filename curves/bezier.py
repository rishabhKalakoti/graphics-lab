import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("Bezier Curves")
ax = fig.add_subplot(111,projection='3d')

N = 4 		#Number of control points
n = N-1  	#Degree of the curve's polynomial

#Control Points:
controlx = [0,30,40,50]
controly = [0,10,10,0]
controlz = [0,0,0,0]

for i in range(0,n):
	ax.plot([controlx[i],controlx[i+1]],[controly[i],controly[i+1]],[controlz[i],controlz[i+1]])


def C(n,k):
	return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

prev_x = controlx[0]
prev_y = controly[0]
prev_z = controlz[0]

for i in range(1001):
	u = i/1000
	x = 0
	y = 0
	z = 0

	for k in range(0,n+1):
		blend = C(n,k)*math.pow(u,k)*math.pow((1-u),n-k)
		x += controlx[k]*blend
		y += controly[k]*blend
		z += controlz[k]*blend

	ax.plot([prev_x,x],[prev_y,y],[prev_z,z])
	prev_x = x
	prev_y = y
	prev_z = z

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
