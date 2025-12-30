# program to authenticate an user based on password

username=input("Enter your username:")
password=input(f"Welcome {username}, please enter your password:")

if username=="daya" and password=="daya123":
    print("Aunthentication Successful !")
    print(f"Welcome, {username} !")
elif username!="daya":
    print(f"Hi, {username}, seems like you are not a registered user.")
    print(f"You need to create account or register, please login after registration.")
    
    choice=input("Do you wish to create new account ? Y/N:")
    if choice=="Y":
        print("Creating New Account, Please enter details : ")
        username=input("Enter your username:")
        password=input(f"Welcome {username}, please enter your password:")

        print("New User Created, Please login.")
    elif choice=="N":
        print("Ok, no problem, thanks. Bye")
    else:
        print("INVALID Option: Please tell me Y or N")
else:
    print("Sorry, authentication failed")
    print("Username and password do not match, please try with correct credentials.")