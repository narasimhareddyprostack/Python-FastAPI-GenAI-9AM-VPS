def outer():
    print("Outer function started")

    def inner():
        print("Inner Function")

    #return 100
    return inner

x=outer()
print(type(x))
x()
x()
x()
x()
#print(x)
