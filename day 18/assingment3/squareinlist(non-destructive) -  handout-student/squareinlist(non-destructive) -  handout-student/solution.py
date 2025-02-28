a=list(map(int,input().split(",")))
b=[]
for i in range(len(a)):
	b.append(a[i]*a[i])
print(b)