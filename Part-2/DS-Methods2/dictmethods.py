emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'loc':'Bangalore',
    'gender':'Male',
    'avail':True
}
#print all keys
print(emp.keys())

for key in emp.keys():
    print(key,":",emp.get(key))
#print all values

for value in emp.values():
    print(value)
#print all key and values