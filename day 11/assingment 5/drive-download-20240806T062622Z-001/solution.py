age=int(input())
BMI=float(input())
health_condition=input()
def example(age,BMI,health_condition):
    if((age>17 and age<61) and (BMI>=18.5 and BMI<=24.9) and (health_condition=="False")) or ((age<18) and (BMI>18.5 and BMI<24.9)) or ((age>60) and (BMI>18.5 and BMI<24.9) and (health_condition=="False")):
        return "True"
    else:
        return "False" 
output=example(age,BMI,health_condition)
print(output)
