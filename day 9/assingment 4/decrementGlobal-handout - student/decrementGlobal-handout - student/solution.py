count=int(input())
def decrementGlobal():
    global count
    count-=2
    return count
y=decrementGlobal()
print(y)
print(count)