'''
filter(fun,seq)
'''
numbers=[1,2,3,4,5,6,7,8,9,10]

def even_no(num):
    return num%2 ==0

filter_obj=filter(even_no,numbers)

print(filter_obj)

even_numbers=list(filter_obj)
print(numbers)
print(even_numbers)
