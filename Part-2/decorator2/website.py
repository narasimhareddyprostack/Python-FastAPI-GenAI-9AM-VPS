from login_req import login_req

def homepage(name,login_status):
    print("Home Page")

@login_req
def productpage(name,login_status):
    print("Product Page")

@login_req
def profilepage(name,login_status):
    print("Prfile Page")

homepage('RG',False)
homepage('RG',True)

productpage('RG',False)
productpage('RG',True)


profilepage('RG',False)
profilepage('RG',True)

