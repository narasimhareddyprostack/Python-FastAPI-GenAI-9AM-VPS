fp=open('data.txt','r')
print(fp.name)      #data.txt
print(fp.mode)      #r

print(fp.readable())#True
print(fp.writable())#False
print(fp.read())    #Data
print(fp.closed)   #False
#how to close a file?
fp.close()
print(fp.closed)   #True
