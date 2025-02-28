x=input()
y=input()
z=input()
def example(x,y,z):
    return (x==str(True) and y==str(True) and z==str(True)) or (x==str(True) and z==str(True)) or (y==str(True) and (x==str(True) or z==str(True)))
output=example(x,y,z)
print(output)