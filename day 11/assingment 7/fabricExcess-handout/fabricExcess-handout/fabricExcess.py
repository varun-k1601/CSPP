
'''def fabricExcess(inches):
	y= inches%36
	if y==0:
		return 0
	else:
		return 36-y
print(fabricExcess(int(input())))'''
def fabricExcess(inches):
    if inches==0:
        return 0
    elif inches==36:
        return 0
    elif inches%36==0:
        return 0
    else:
        a=inches%36
        return 36-a
print(fabricExcess(int(input())))
    