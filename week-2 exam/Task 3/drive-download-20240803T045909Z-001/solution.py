# Write your solution here
def BMI_Calculator(weight,height):
    BMI=weight/(height**2)
    return BMI
weight=float(input())
height=float(input())
output=BMI_Calculator(weight,height)
print(round(output,2))