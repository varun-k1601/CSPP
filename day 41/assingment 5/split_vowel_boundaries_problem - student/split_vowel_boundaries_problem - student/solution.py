def split_by_vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    l = []
    temp = ''
    count = 0
    for i in s:
        if i in vowels:
            if temp != '':
                l.append(temp)
            l.append(i)
            temp = ''
            count += 1
        else:
            temp += i

    if temp != '':
        l.append(temp)
        
    return l

            #l.append(i)
    # if l[0]=='':
    #     return l[1:]

    return l
string = input()
print(split_by_vowels(string))