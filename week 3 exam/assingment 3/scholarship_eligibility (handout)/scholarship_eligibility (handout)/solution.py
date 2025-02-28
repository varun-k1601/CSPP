GPA=float(input())
extracurricular_activities=int(input())
community_service_hours=int(input())
financial_need=float(input())
def eligibility(GPA,extracurricular_activities,community_service_hours,financial_need):
    if((GPA>=3.5) and (extracurricular_activities>=2) and (community_service_hours>=50) and (financial_need>=10000)) or ((GPA>=4.0) and (extracurricular_activities>=1) and (community_service_hours>=100)) or ((GPA>=3.0) and (extracurricular_activities>=3) and (community_service_hours>=200) and (financial_need>=5000)):
        return True
    else:
        return False
output=eligibility(GPA,extracurricular_activities,community_service_hours,financial_need)
print(output)