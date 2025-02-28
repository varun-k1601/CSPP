a=eval(input())
d={}
def fun(a):
    for user,website in a:
        if user in d:
            d[user].append(website)
        else:
            d[user]=[website]
    return d
print(fun(a))
# [('alice', 'example.com'), ('bob', 'website.com'), ('alice', 'another.com'), ('bob', 'example.com')]
# {'alice': ['example.com', 'another.com'], 'bob': ['website.com', 'example.com']}