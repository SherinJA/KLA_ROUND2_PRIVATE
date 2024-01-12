import math
from sympy import *
import numpy as np
from decimal import Decimal
from collections import *

x,y=symbols('x y')


def circle_eq(x_1,y_1,r):
    expr=x**2+y**2
    val1=expr.subs(x,x_1)
    val2=val1.subs(y,y_1)
    #print(val2)

    return val2

def find_distance(p1,p2):
    dist=sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return dist

with open("Testcase1.txt", 'r') as file:
    lines = file.readlines()

for line in lines:
    if 'WaferDiameter' in line:
        temp, diameter_str = line.split(':')
        diameter = int(diameter_str)
        
    if 'NumberOfPoints' in line:
        temp,num_points_str=line.split(':')
        num_points=int(num_points_str)

    if 'Angle' in line:
        temp,angle_str=line.split(':')
        angle=int(angle_str)

print("Wafer Diameter:", diameter)
print("Number of points: ", num_points)
print("Angle: ",angle)

radius=diameter/2
slope=math.tan(math.radians(angle))

x,y=symbols('x y')
lhs=slope*x

print("Line equation:y={0}".format(slope*x))

x_start=-1*radius
x_end=radius+1

rng=np.arange(x_start,x_end)

