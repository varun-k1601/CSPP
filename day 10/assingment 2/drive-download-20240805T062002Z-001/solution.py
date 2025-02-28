age=int(input())
has_id=input()
knows_password=input()
def example(age,has_id,knows_password):
    return (age>17 and has_id=="True") or (knows_password=="True" )
output=example(age,has_id,knows_password)
print(output)