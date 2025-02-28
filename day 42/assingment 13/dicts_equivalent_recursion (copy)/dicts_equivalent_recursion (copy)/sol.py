# def check_dic(dic1,dic2):
#     if dic1.keys() != dic2.keys():
#         return False
#     for k in dic1:
#         val1 = dic1[k]
#         val2 = dic2[k]

#         if isinstance(val1, dict) and isinstance(val2, dict):
#             if not check_dic(val1, val2):
#                 return False

#         elif val1 != val2:
#                 return False

#     return True

# dic1 = eval(input())
# dic2 = eval(input())
# print(check_dic(dic1,dic2))


def add_lst(lst):
    new_lst =[]
    for i in lst:
        if isinstance(i,int):
            new_lst.append(i)
        else:
            ar = add_lst(i)
            new_lst.extend(ar)
    return new_lst
lst = eval(input())
print(add_lst(lst))