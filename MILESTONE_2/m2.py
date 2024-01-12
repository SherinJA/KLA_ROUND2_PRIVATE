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
        
    if 'DieSize' in line:
        temp,val=line.split(':')
        dim1_str,dim2_str=val.split('x')
        #print(dim1_str)
        dim1=int(dim1_str)
        dim2=int(dim2_str)

    if 'DieShiftVector' in line:
        temp,val=line.split(':')
        d1,d2=val.split(',')
        d1_str=d1[1:]
        d2_str = d2[:-2]

        d1_int=int(d1_str)
        d2_int=int(d2_str)

        #print(d1_int)
        #print(d2_int)

        die_sv=((d1_int,d2_int))




print("Wafer Diameter:", diameter)
print("dim1:" , dim1)
print("dim2:",dim2)
print("Die shift vector: ",die_sv)






"""radius=diameter/2
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
        writer.writerow(points)"""
