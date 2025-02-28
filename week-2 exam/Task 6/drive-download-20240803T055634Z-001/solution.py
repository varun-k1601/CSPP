# Write your solution here
import math
def pythagoreanTheorem(a,b):
    return math.sqrt(a**2+b**2)
a=float(input())
b=float(input())
c=pythagoreanTheorem(a,b)
print(round(c,2))