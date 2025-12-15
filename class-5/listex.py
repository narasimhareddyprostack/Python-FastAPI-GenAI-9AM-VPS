#create
a=[]  #empty list
b=[10,20,30,10,20,30,True,[],(),{}]
enames=['RG','SG','PG','Modi']

#read
print(a)
print(b)
print(enames)
#read list elements using index
print(enames[0]) #RG
print(enames[1]) #SG
print(enames[2]) #PG
#print(enames[8]) #IndexError:list index out of range
#update
enames[0]="Rahul Gandhi"
print(enames)