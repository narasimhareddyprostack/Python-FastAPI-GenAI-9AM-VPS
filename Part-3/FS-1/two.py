fp1=open('data.txt','r')
data=fp1.read()

fp2=open("greet.txt",'w')
fp2.write(data)
print('New Text File Created')

fp1.close()
fp2.close()