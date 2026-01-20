fp=open("data.txt",'r')

print(fp.name)
print(fp.mode)
print(fp.readable())   #True
print(fp.writable())   #False
print(fp.closed)        #False