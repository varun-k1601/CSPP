x=int(input())
y=int(input())
def sumOrDifference(x,y):
    if (abs(x+y==5)) or (abs(x-y)==5):
        return True
    return False
output=sumOrDifference(x,y)
print(output)