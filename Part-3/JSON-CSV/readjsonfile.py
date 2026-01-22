import json 

fp=open('emp.json','r')
employees=json.load(fp)

for emp in employees:
    if emp['gender']=="Male":
        print("Employe Id:",emp['eid'],"and Name:", emp['ename'])