# def readList():
# 	a = []
# 	l = int(input())
# 	for i in range(l):
# 		a.append(int(input()))
# 	return a

# def recursionOnlyAlternatingSum(l):
# 	# your code goes here
# 	sum=0
# 	if
# 	return -1

# print(recursionOnlyAlternatingSum(readList()))


a=[]
l=int(input())
for i in range(l):
    a.append(int(input()))
def recursionOnlyAlternatingSum(a,i,l,sum):
    if i>=l:
        return sum
    if(i%2==0):
        sum+=a[i]
    else:
        sum-=a[i]
    return recursionOnlyAlternatingSum(a,i+1,l,sum)
print(recursionOnlyAlternatingSum(a,0,l,0))