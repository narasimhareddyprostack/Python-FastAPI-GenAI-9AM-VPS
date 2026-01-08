def user_tr():
    print("user_tr function starte")

    def login():
        return True
    def logout():
        return False
    return login

inner=user_tr()
print(inner())
