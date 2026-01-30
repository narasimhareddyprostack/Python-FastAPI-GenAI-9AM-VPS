try:
    fp=open("data1.txt",'r')
    data=fp.read()
    print(data)
except FileNotFoundError as err:
    fp=open("data.txt",'r')
    data=fp.read()
    print(data)
    print(err)
    #print("Today is Friday")

finally:
    print("finally block will execute always")