from math import cos, sqrt, acos, atan, pi, sin
import numpy as np
from scipy.optimize import fsolve
''' This program determines the distance necessary for a plane at (x1,y1) and bearing (degrees) to travel to point (x2,y2)
	based on its turning radius r in a 2-D coordiante system. This assumes the destination is 'in front' of the plane's direction,
	i.e. its destination is within +- 90 degrees relative to forward bearing'''

# (x1,y1), (x2,y2), turning radius, and bearing (in degrees) to be input
x1 = 0.; y1 = 0.; x2 = 4.; y2 = 2.; r = 2; bearing = 90.
bearing = bearing*pi/180

# normalize the coordinate system so the plane is at (0,0) facing the positive y-axis and (x2,y2) becomes point (i,j)
dxy = sqrt((x2-x1)**2+(y2-y1)**2)
mxy = (y2-y1)/(x2-x1)
phi = atan(abs(y2-y1)/abs(x2-x1))
theta = abs(bearing - phi)

# if (x2,y2) are right relative to the plane's bearing
if mxy > 0:
	i = dxy*sin(theta)
	j = dxy*cos(theta)
	print "(i,j) is (%f, %f)." %(i,j)

# if (x2,y2) are left relative to the plane's bearing
if mxy < 0:
	i = -dxy*sin(theta)
	j = dxy*cos(theta)
	print "(i,j) is (%f, %f)." %(i,j)

	
''' Solving for point (x,y), the point on the turning radius tangent to (i,j)'''

# use if (i,j) is left of the plane	
def func_left(p, *data):
	x,y = p
	i,j,r = data
	return ((x+r)*(i-x)+(j-y)*y,(x+r)**2+y**2-r**2)

# use if (i,j) is right of plane
def func_right(p, *data):
	x,y = p
	i,j,r = data
	return ((x-r)*(i-x)+(j-y)*y,(x-r)**2+y**2-r**2)

data = (i,j,r)
m = j/i

# if (i,j) to the right
if m > 0:
	x,y = fsolve(func_right, [1,1], args=data)
	print "(x,y) is (%f, %f)." %(x,y)

# if (i,j) to the left
if m < 0:
	x,y = fsolve(func_left, [1,1], args=data)
	print "(x,y) is (%f, %f)." %(x,y)

# distance bewteen (x,y) and (i,j)
d1 = sqrt((i-x)**2+(j-y)**2)

# straight line distance between starting point (origin) and (x,y)
d2 = sqrt(x**2+y**2)

# arclength distance traveled based on turning radius
theta = acos((2*r**2-d2**2)/(2*r**2))
s = r*theta

# total distance plane needs to travel to reach (i,j)
D = d1 + s
print "Total distance is %f." %D