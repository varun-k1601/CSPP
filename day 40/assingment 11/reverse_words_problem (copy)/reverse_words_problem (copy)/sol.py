a=input()
def fun(a):
    words=a.split(" ")
    reversed_words=[word[::-1] for word in words]
    return " ".join(reversed_words)
print(fun(a))