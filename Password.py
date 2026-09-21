print("Create a username and password")
username = input("Create a username")
password = input("Create a password")

print("Please your write username and password to log in")
while True:
    checkUsername = input("please write your username")
    checkPassword = input("please write your password")

    if username == checkUsername and password == checkPassword:
        print("Your password is correct: Welcome", checkUsername)
        break
    else:
        print("Wrong password, try again")
        