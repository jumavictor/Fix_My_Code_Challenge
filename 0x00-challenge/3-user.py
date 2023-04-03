if user_1.id is None:
        print("New User should have an id")
    else:
        print("User id: ", user_1.id)

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")
    else:
        print("User ids are unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")
    else:
        print("User.password is hashed")

    if user_2.password is not None:
        print("User.password should be None by default")
    else:
        print("User.password is None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")
    else:
        print("User.password is None if set to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")
    else:
        print("User.password is None if set to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right \
password")
    else:
        print("is_valid_password returns True for correct password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right \
password")
    else:
        print("is_valid_password returns False for incorrect password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")
    else:
        print("is_valid_password returns False for None password")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")
    else:
        print("is_valid_password returns False for integer password")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set \
before")
    else:
        print("is_valid_password returns False for no password set")
