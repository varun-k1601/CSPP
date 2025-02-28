# Write your solution here
import math
def areaOfCircle(r):
    area=math.pi*(r**2)
    return area
r=float(input())
y=areaOfCircle(r)
print(round(y,2))