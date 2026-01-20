fp=open("data.txt",'r')
#data=fp.read()
#data=fp.readline()
#data=fp.readline(6)
lines=fp.readlines()
print(lines)
for line in lines:
    print(line)