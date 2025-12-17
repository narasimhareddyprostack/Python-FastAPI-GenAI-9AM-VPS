enames=['Rahul','Sonai','Priya']
print(enames)
#update list element - using index
enames[0]="Rahul Gandhi"
print(enames)

eids={101,101,101,102}
eids.add(103)
eids.add("Rahul")
eids.add(True)
print(eids)

emp={'eid':101,'ename':'Rahul','esal':45000}
emp['esal']=55000
print(emp)

b=bytearray([10,20,30,40])
b[0]=11
for value in b:
    print(value)