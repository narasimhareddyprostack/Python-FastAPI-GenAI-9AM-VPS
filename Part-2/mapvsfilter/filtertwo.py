numbers=[1,2,3,4,5,6,7,8,9,10]

""" def check_even(num):
    return num%2==0
 """
filter_obj=filter(lambda num:num%2==0,numbers)

even_numbers=list(filter_obj)
print(numbers)
print(even_numbers)