# Write your solution here
def areaOfTriangle(base,height):
    result=(1/2)*base*height
    return result
base=float(input())
height=float(input())
output=areaOfTriangle(base,height)
print(round(output,2))