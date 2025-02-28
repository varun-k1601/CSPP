import math
def eggCartons(eggs):
	if eggs==0:
		return int("0")
	else:
		return math.ceil(eggs/12)

print(eggCartons(int(input())))