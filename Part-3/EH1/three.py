try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a/b) 
    
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
finally:
    print("Finally will always")

print("GM")