import itertools
s=input()
def lexicographically(s):
    per=["".join(i) for i in itertools.permutations(s)]
    per.sort()
    for j in range(len(per)):
        if per[j]==s:
            return j+1
print(lexicographically(s))