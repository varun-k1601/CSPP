# Write your solution hereimport math
'''import math
a=float(input())
b=float(input())
c=float(input())
d=math.pow(b,2)-(4*a*c)
x=math.pow(d,1/2)
y=str((-b+x)/2*a)
z=str((-b-x)/2*a)
print("("+y+", "+z+")")'''
import math
a=float(input())
b=float(input())
c=float(input())
d=str((-b+math.sqrt((b**2)-4*a*c))/(2*a))
e=str((-b-math.sqrt((b**2)-4*a*c))/(2*a))
print("("+d+", "+e+")")