eids=[101,102,103,104]
enames=('RG','SG','PG')
sizes={'S','M','L','XL','XXL'}
ename="Rahul"
b=bytes([10,20,30,255])
ba=bytearray([10,20,30,255])
fz=frozenset({10,20,30})
numbers=range(100)

print(101 in eids)  #True
print(108 in eids)  #False
print(108 not in eids)  #True

print('a' in ename)  #True
print('z' in ename)  #False

print(98 in numbers) #True
print(99 in numbers) #True
print(100 in numbers) #False
print(100  not in numbers) #True