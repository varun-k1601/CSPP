def merge_dict(d1, d2):
    res = {}
    for k, v in d1.items():
        if k in d2:
            if isinstance(v, dict) and isinstance(d2[k], dict):
                res[k] = merge_dict(v, d2[k])
            else:
                res[k] = d2[k]
        else:
            res[k] = v 
    for k, v in d2.items():
        if k not in res:
            res[k] = v

    return res
print(merge_dict(eval(input()), eval(input())))