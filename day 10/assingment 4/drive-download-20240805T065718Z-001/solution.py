soil_dry=input()
raining=input()
day_time=input()
temperature=int(input())
def example(soil_dry,raining,day_time,temperature):
    return (soil_dry=="True") and (raining=="False") and (day_time=="True") and (temperature>10)
output=example(soil_dry,raining,day_time,temperature)
print(output)