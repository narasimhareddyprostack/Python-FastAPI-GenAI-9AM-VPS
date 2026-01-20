def login_req(func):

    def inner(name,login_status):
        if login_status==False:
            print("Login Required")
        else:
            return func(name,login_status)
        
    return inner