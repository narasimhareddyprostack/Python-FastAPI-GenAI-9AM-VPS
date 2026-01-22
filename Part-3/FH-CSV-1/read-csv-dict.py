import csv 
fp=open('emp.csv','r')
emp_csv=csv.DictReader(fp)

print(emp_csv)

for emp in emp_csv:
    print(emp['ename'])
