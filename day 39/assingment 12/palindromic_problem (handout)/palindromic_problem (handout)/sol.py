a=input()
def paplin(a):
   if a==a[::-1]:
      return True
def palindrome(a):
    c=0
    for i in range(len(a)):
      for j in range(i+1,len(a)+1):
        # print(a[i:j])
        if paplin(a[i:j]):
            c=c+1
    return c
print(palindrome(a))