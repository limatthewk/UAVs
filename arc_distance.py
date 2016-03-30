from math import cos,sqrt
import numpy as np
from scipy.optimize import fsolve
	
def func(p, *data):
	x,y = p
	i,j,r = data
	return ((x+r)*(i-x)+(j-y)*y,(x+r)**2+y**2-r**2)

data = (-7,10,5)
x,y = fsolve(func, [1,1], args=data)
print x,y
d = sqrt((data[0]-x)**2+(data[1]-y)**2)
print d
#make a change