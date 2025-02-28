a=input()
a=a.lower()
def fun(a):
    set1=set("abcdefghijklmnopqrstuvwxyz")
    set2=set()
    for char in a:
        if char.isalpha():
            set2.add(char)
    if len(set1)==len(set2):
        return True
    else:
        return False
print(fun(a))