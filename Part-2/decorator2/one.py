def smart_div(func):

    def inner(a,b):
        if b==0:
            print('Cant Divide by Zero')
        else:
            return func(a,b)
        
    return inner

@smart_div
def calc(a,b):
    print(a/b)
    
calc(10,5)
calc(10,0)