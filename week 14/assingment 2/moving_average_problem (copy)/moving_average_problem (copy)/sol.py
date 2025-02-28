l=eval(input())
size=int(input())
def fun(l,size):
    l1=[]
    if size<=0 or size>len(l):
        return []
    else:
        for i in range(len(l)):
            sum=0
            count=0
            for j in range(i,len(l)):
                if count==size:
                    break
                count+=1
                sum+=l[j]
            if count==size:
                k=sum/size
                l1.append(k)
    return l1
print(fun(l,size))