s=input()
def fun(s):
    d={}
    l=s.split(" ")
    for word in l:
        if len(word)>2:
            d[word]=word[0]+str(len(word[1:-1]))+word[-1]
        else:
            d[word]=word
    return d
print(fun(s))
# international example word AI
# {'international': 'i11l', 'example': 'e5e', 'word': 'w2d', 'AI': 'AI'}