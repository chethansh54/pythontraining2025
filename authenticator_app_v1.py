"""
Docstring for authenticator_app_v1
Version : 1.0

Application Name : User Account Authenticator
Features:
1. Login With Username & Password
2. Create New User Account 
3. Update/Reset Password
4. Update/Reset Username
"""

# user account local database/data store
user_account_store = {}

while True:
    print("Welcome To User Authenticator")
    print("MENU OPTIONS")
    print("================")

    print("1. Login with username password")
    print("2. Create New Account")
    print("3. Forgot Password")
    print("4. Forgot Username")
    print("5. Exit")

    choice_option=int(input("Choose an Option : "))

    # login user code
    if choice_option == 1:
        print("Please enter your username and password to login.")
        username=input("Username: ")
        password=input("Password: ")

        if username in user_account_store:
            if user_account_store[username] == password:
                print(f"Login Success : Hello {username}, welcome to your Profile ! ")
            else:
                print(f"Hey {username}, your entered password is incorrect, please try with correct password.")
        else:
            print(f"User with name {username}, does not exist.")
            print("Use option 2 to create a new user !")

        print() # prints new line for clean visibility
    
    elif choice_option == 2:
        print("Create a New Account : ")
        
        username=input("Please enter a username : ")
        password=input("Please enter a password : ")

        user_account_store[username] = password

        print(f"Hey, {username}, your account has been created. Please Login Now")

        print() # print new line at the end of block
    
    elif choice_option == 3:
        print("Forgot Password : ")
        print("To Reset your password : ")

        username = input("Please Enter your Username : ")

        if username in user_account_store:
            print(f"Hey, {username} !")
            password = input("Enter your new password : ")
            re_password = input("Confirm your password : ")

            if password == re_password:
                user_account_store[username] = password
                print(f"Password Reset Successful ! Please Login Now.")
            else:
                print("Your passwords did not match, please try again...")
        else:
            print(f"Username {username}, does not exist, please create an account and try again...")
        
        print() # new line at end of block
    
    elif choice_option == 4:
        print("Please contact your administrator for this.")
        print()
    
    elif choice_option == 5:
        print("Thanks for using authenticator.")
        print("Bye ! ")
        exit(0) # exit with success code

    else:
        print("Please Enter Valid Option : [ 1/2/3/4/5 ]")















