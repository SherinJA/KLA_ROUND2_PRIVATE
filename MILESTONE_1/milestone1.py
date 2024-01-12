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

print(rng)

points=[]

for i in range(len(rng)):
    val=lhs.subs(x,rng[i])

    circle=circle_eq(rng[i],val,radius)

    if(circle<=radius**2):
        points.append((rng[i],val))


print(points)

print(radius**2)

point_distance={}

main_dict=defaultdict(set)

dist_list=set()
for i in range(len(points)):
    sub_dict={}
    for j in range(len(points)):
        if(points[i]==points[j]):
            continue
        dist=find_distance(points[i],points[j])

        main_dict[dist].add(points[i])
        main_dict[dist].add(points[j])

for key in main_dict.keys():
    print(len(main_dict[key]))
    if(len(main_dict[key])>=num_points):
        final_list=main_dict[key]
        break

final_list=list(final_list)
final_points=[]
for i in range(num_points):
    final_points.append(final_list[i])

print(final_points)

print("len: ",len(final_points))


"""with open('m1_t1.txt', 'w') as file:
    # Iterate over each tuple in the list
    for t in final_points:
        # Write the tuple in the desired format to the file
        file.write(f"(0)".format(t))
        #file.write(f"({t[0]}) {t}\n")"""


with open('m1_t1.txt', 'w') as f:
    for point in final_points:
        f.write(str(point) + '\n')





