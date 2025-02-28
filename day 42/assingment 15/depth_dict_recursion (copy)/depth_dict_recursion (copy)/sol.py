def depth_dicti(d):
    if d=={}:
        return c
    else:
        c=1
        for k,v in d.items():
            if isinstance(v,dict):
                c+=depth_dicti(v)
    return c
print(depth_dicti(eval(input())))

                