with open("user_data.csv", "r+") as user_file:
    print("WELCOME TO DATA STORE")
    # insert header only if doesnt exist in first line of csv file
    columns = "username,password,emailid,role"
    
    for line in user_file:
        print(f"HEADER = {line}")

        if line != columns:
            user_file.write(columns)
            user_file.write("\n")
        break

with open("user_data.csv", "a") as user_file:
    while True:
        print("1. Add User Data\n2. Exit\n")
        choice = input("Enter Your Choice : ")

        if choice == "1":
            username=input("Enter Username : ")
            password=input("Enter password : ")
            emailid=input("Enter emailid : ")
            role=input("Enter role : ")

            user_file.write(f"{username},{password},{emailid},{role}")
            user_file.write("\n")
        
        elif choice == "2":
            print("Bye")
            break
        else:
            print("Invalid Option")

    print("Data Stored to File : user_data.csv ")