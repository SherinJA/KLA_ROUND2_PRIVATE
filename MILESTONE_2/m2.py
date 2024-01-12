import numpy as np
import sympy as sp
import math
import csv
from fractions import Fraction

x1,y1=sp.symbols(('x','y'))

def dist(p1,p2):
    dist=math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return dist

def circle_eq(x1,y1):
    return (x1**2 + y1**2)

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
        d2_str=d2[:-2]
        print(d2_str)

        d1_int=int(d1_str)
        d2_int=int(d2_str)

        #print(d1_int)
        #print(d2_int)

        die_sv=((d1_int,d2_int))

    if 'ReferenceDie' in line:
        temp,val=line.split(':')
        d1,d2=val.split(',')
        d1_str=d1[1:]
        d2_str=d2[:-1]

        r1_int=int(d1_str)
        r2_int=int(d2_str)

        #print(d1_int)
        #print(d2_int)

        ref_die=((r1_int,r2_int))

print("Wafer Diameter:", diameter)
print("dim1:" , dim1)
print("dim2:",dim2)
print("Die shift vector: ",die_sv)
print("Reference die: ",ref_die)

#trying to find the llc of the reference die
x_cord=(ref_die[0]-(dim1/2))
y_cord=(ref_die[1]-(dim2/2))
radius=diameter/2
print(x_cord)
print(y_cord)
initial_x=x_cord+die_sv[0]
initial_y=y_cord+die_sv[1]

label={}
label[(0,0)]=(x_cord,y_cord)


#Quadrant 1
i=0
j=0
while(circle_eq(x_cord,y_cord)<=radius**2):
    
    while(circle_eq(x_cord,y_cord)<=radius**2):
        label[(i,j)]=(x_cord,y_cord)
        y_cord=y_cord+dim1
        j+=1

    x_cord=x_cord+dim1
    y_cord=initial_y
    j=0
    i+=1

print(label)


#Quadrant 2
x_cord=initial_x
y_cord=initial_y

i=0
j=0
while(circle_eq(x_cord,y_cord)<=radius**2):
    print("out")
    while(circle_eq(x_cord,y_cord)<=radius**2):
        print("in")

        #print(x_cord,y_cord)
        label[(i,j)]=(x_cord,y_cord)
        y_cord=y_cord+dim1
        j+=1
            
    x_cord=x_cord-dim1
    y_cord=initial_y
    j=0
    i-=1

#print(label)

#Quadrant 3
x_cord=initial_x
y_cord=initial_y

i=0
j=0
while(circle_eq(x_cord,y_cord)<=radius**2):
    while(circle_eq(x_cord,y_cord)<=radius**2):

        #print(x_cord,y_cord)
        label[(i,j)]=(x_cord,y_cord)
        y_cord=y_cord-dim1
        j-=1
            
    x_cord=x_cord-dim1
    y_cord=initial_y
    j=0
    i-=1

print(label)


#Quadrant 4
x_cord=initial_x
y_cord=initial_y

i=0
j=0
while(circle_eq(x_cord,y_cord)<=radius**2):

    while(circle_eq(x_cord,y_cord)<=radius**2):
        #print(x_cord,y_cord)
        label[(i,j)]=(x_cord,y_cord)
        y_cord=y_cord-dim1
        j-=1
            
    x_cord=x_cord+dim1
    y_cord=initial_y
    j=0
    i+=1

print(label)


with open("m2_t1.txt", 'w') as file:
    # Iterate over the dictionary items and write them to the file
    for key, value in label.items():
        # Convert the tuple values to a string for writing
        line = f"{key}: ({value[0]}, {value[1]})\n"
        # Write the line to the file
        file.write(line)











