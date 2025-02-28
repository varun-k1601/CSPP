# Write your solution here
import math
def distanceBetweenPoints(x1,y1,x2,y2):
    a=(x2-x1)**2
    b=(y2-y1)**2
    c=a+b
    return math.sqrt(c)
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
output=distanceBetweenPoints(x1,y1,x2,y2)
print(round(output,2))
