counter=int(input())
def incrementGlobal():
    global counter
    counter+=1
    return counter
y=incrementGlobal()
print(y)
print(counter)