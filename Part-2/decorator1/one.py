def homeapage(name,logi_status):
    return "Home Page"

def productpage(name,logi_status):
    return "Product  Page"

def orders(name,logi_status):
    return "Order Details Page"

def profile(name,logi_status):
    return "Profile Page"

print(homeapage("RG",True))
print(productpage("RG",False))
print(orders("RG",False))
print(profile("RG",False))