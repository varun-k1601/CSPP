age=int(input())
annual_income=float(input())
credit_score=int(input())
current_debts=float(input())
def example(age,annual_income,credit_score,current_debts):
     if((age>=25 and age<=65) and (annual_income>=50000) and (credit_score>=700) and (current_debts<50000)) or ((age<25) and(annual_income>=70000) and (credit_score>=750) and (current_debts<30000)) or ((age>65) and (annual_income>=40000) and credit_score>=650 and current_debts<20000):
          return "True"
     else:
          return "False"
output=example(age,annual_income,credit_score,current_debts)
print(output)