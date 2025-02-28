#Task 1

a=1
print("Initial integer value:",a)
a=2
print("Changed integer value:",a)
b=20.1
print("Initial float value:",b)
b=25.5
print("Changed float value:",b)
c="IIIT Hyderabad"
print("Initial string value:",c)
c=c+" MSIT"
print("Changed string value:",c)
i=100
j=200
print("Before swap:",i,j)
i=i+j
j=i-j
i=i-j
print("After swap:",i,j)



#Task 2

a=10
b=20.5
c="MSIT"
d=True
print("Integer:",type(a),",""Value =",a)
print("Float:",type(b),",""Value =",b)
print("String:",type(c),",""Value =",c)
print("Boolean:",type(d),",""Value =",d)
print("Integer to float:",float(a))
print("Float to integer:",int(b))
print("Float to string:",str(b))


#Task 3

a=10 #it is used to represent only integer values
b=20.5 #it is used to represent only float values
c="MSIT" #it is used to represent only string values
d=True #Boolean values are used to represent given condition is true or false
e="b"
print(f) #Name error is nothing but the value is assigned to one variable but we are trying to print another variable which is not defined


#Task 4

a=10
prin t(a) #It is intentionally not following the syntax
print(b) #It is trying to use undefined variable known as name error
c="MSIT"
print(float(c)) #we are trying to send unexpected value here known as value error
f=10+"MSIT"
print(f)#It is known as type error because we are trying to perform invalid operation between two incompatible data types
d=10/0
print(d) #It is known as Zero division error because we are trying to divide it with zero
import p
print(p) #It is known as module not found error because we are trying to import non-existent module
