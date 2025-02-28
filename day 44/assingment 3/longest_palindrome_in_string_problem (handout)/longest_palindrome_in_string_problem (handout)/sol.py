def longest_pali(string):
    a = ""
    l = []
    maxi = 0
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            check = string[i:j]
            if check==check[::-1]:
                l.append(check)
    for i in l:
        if len(i)>maxi:
            maxi = len(i)
            st = i
    print(st)
longest_pali(input())
            