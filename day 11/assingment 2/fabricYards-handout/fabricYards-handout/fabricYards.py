import math
def fabricYards(inches):
	if inches==0:
		return int("0")
	elif inches<36 or inches==36:
		return int("1")
	else:
		return math.ceil(inches/36)

print(fabricYards(int(input())))