house_occupied=input()
high_energy_appliance_on=input()
peak_hours=input()
current_energy_usage=int(input())
def example(house_occupied,high_energy_appliance_on,peak_hours,current_energy_usage):
    return (house_occupied=="False") or ((high_energy_appliance_on=="True") and (current_energy_usage>50))
output=example(house_occupied,high_energy_appliance_on,peak_hours,current_energy_usage)
print(output)