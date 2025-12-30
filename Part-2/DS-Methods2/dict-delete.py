emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'loc':'Bangalore',
    'gender':'Male',
    'avail':True
}
print(emp)
#remove specified key:value from dict object
emp.pop('esalary')
print(emp)
#dict.popitem() - remove last key:value pair
emp.popitem()
print(emp)
emp.clear()
print(emp)