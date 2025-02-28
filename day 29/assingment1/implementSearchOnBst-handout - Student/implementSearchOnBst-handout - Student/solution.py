a=eval(input())
n=int(input())
def find_subtree(a,n):
    if a is None:
        return None
    if a["value"]==n:
        return a
    if n<a["value"]:
        return find_subtree(a.get("left"),n)
    else:
        return find_subtree(a.get("right"),n)
result=find_subtree(a,n)
print(result)