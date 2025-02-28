a=eval(input())
def detect_self_loops(a):
    for key,value in a.items():
        if key in value:
            return True
    return False
print(detect_self_loops(a))