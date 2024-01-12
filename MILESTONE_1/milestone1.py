import numpy as np
import sympy as sp
import math
import csv
from fractions import Fraction

x1,y1,x2,y2=sp.symbols(('x1','y1','x2','y2'))

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
start_x=0
start_y=0

constant_1=start_y-(slope*start_x)

eq1=sp.Eq(slope*x1+constant_1-y1,0)
eq2=sp.Eq((x1-start_x)**2+(y1-start_y)**2-(diameter//2)**2,0)
coordinates=sp.solve((eq1,eq2),(x1,y1))

print(coordinates)
x_1=coordinates[0][0]
y_1=coordinates[0][1]
x_2=coordinates[1][0]
y_2=coordinates[1][1]

interval_len=diameter/(num_points-1)
final_points=[]

final_points.append(coordinates[0])

for i in range(num_points-2):
    eq2=sp.Eq((x1-x_2)**2+(y1-y_2)**2-(diameter-((i+1)*interval_len))**2,0)
    final_points.append(sp.solve((eq1,eq2),(x1,y1))[0])

final_points.append(coordinates[1])

with open('m1_t1.txt','w',newline='') as file1:
    writer=csv.writer(file1)
    for points in final_points:
        writer.writerow(points)
