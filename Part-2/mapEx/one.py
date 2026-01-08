employees=[
    {"eid":101,"ename":"Rahul"},
    {"eid":102,"ename":"Sonia"},
    {"eid":103,"ename":"Priya"},
    {"eid":104,"ename":"Modi"},
]
#for every employee obj add new key:value 
# loc:"Banglaore"
def addnewpropery(emp):
    emp['loc']='Bangalore'
    return emp 

emp_map_obj=map(addnewpropery,employees)
new_employees=list(emp_map_obj)
print(new_employees)