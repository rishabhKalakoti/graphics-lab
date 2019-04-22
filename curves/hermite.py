import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure("Hermite Curve")
ax = fig.add_subplot(111,projection = '3d')

p0 = [0,0,0]
p1 = [10,10,0]
d0 = 45
d1 = 45

d0 = math.tan((math.pi*d0)/180)
d1 = math.tan((math.pi*d1)/180)

prev_x = p0[0]
prev_y = p0[1]
prev_z = p0[2]

x = 0
y = 0
z = 0

#Standard Hermite Matrix derived for a cubic polynomial
hermite_mat = np.array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]])

mgeox = np.array([[p0[0]],[p1[0]],[d0],[d1]])
mgeoy = np.array([[p0[1]],[p1[1]],[d0],[d1]])
mgeoz = np.array([[p0[2]],[p1[2]],[d0],[d1]])

for i in range(101):
	u = i/100
	U = np.array([[math.pow(u,3),math.pow(u,2),u,1]])

	x = U.dot(hermite_mat.dot(mgeox))
	y = U.dot(hermite_mat.dot(mgeoy))
	z = U.dot(hermite_mat.dot(mgeoz))

	x = x[0][0]
	y = y[0][0]
	z = z[0][0]

	ax.plot([prev_x,x],[prev_y,y],[prev_z,z])

	prev_x = x
	prev_y = y
	prev_z = z

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
