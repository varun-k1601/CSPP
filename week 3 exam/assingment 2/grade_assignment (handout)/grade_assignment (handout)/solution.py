score=int(input())
def grade(score):
    result=""
    if(score>=90):
        result="A"
        return result
    elif(score>=80 and score<90):
        result="B"
        return result
    elif(score>=70 and score<80):
        result="C"
        return result
    elif(score>=60 and score<70):
        result="D"
        return result
    else:
        result="F"
        return result
output=grade(score)
print(output)