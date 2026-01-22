import json 
fp1=open("emp.json",'r')
fp2=open("male_emp.json",'w')

employees=json.load(fp1)
male_employees=[]

for emp in employees:
    if emp['gender']=="Male":
        male_employees.append(emp)


json.dump(male_employees,fp2)
print("New Json File Created")

fp1.close()
fp2.close()