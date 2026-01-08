def login_req(func):

    def inner(name,login_status):
        if login_status==False:
            print("Login is Required")
        else:
            return func(name,login_status)
        
    return inner
    
def homeapage(name,logi_status):
    return "Home Page"

def productpage(name,logi_status):
    return "Product  Page"

@login_req
def orders(name,logi_status):
    return "Order Details Page"

@login_req
def profile(name,logi_status):
    return "Profile Page"

print(homeapage("RG",True))
print(productpage("RG",False))


print(orders("RG",False))


print(profile("RG",False))