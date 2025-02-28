
def isEquilateralTriangle(side1, side2, side3):
	if side1==side2==side3:
		return "True"
	else:
		return "False"

print(isEquilateralTriangle(float(input()), float(input()), float(input())))