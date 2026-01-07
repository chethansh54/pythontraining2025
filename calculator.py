# Calculator Code

def add(n1,n2):
    return n1+n2

def diff(n1,n2):
    return n2-n1

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    division=0

    try:
        division = n1/n2
    except Exception as e:
        print(e)
    return division

def power(x,y):
    return x**y

while True:
    print("CALCULATOR")
    print("1. ADD\n2. MINUS\n3. DIVIDE\n4. PRODUCT\n 5. X ^ Y Power\n 6. EXIT")
    option=input("Choose Option : ")

    if option == "1":
        a = int(input("Enter Num1 : "))
        b = int(input("Enter Num2 : "))
        print(f"SUM OF {a} and {b} = {add(a,b)}")
    elif option == "2":
        a = int(input("Enter Num1 : "))
        b = int(input("Enter Num2 : "))
        print(f"MINUS OF {a} and {b} = {diff(a,b)}")
    elif option == "3":
        a = int(input("Enter Num1 : "))
        b = int(input("Enter Num2 : "))
        print(f"DIVISION OF {a} and {b} = {divide(a,b)}")
    elif option == "4":
        a = int(input("Enter Num1 : "))
        b = int(input("Enter Num2 : "))
        print(f"PRODUCT OF {a} and {b} = {multiply(a,b)}")
    elif option == "5":
        a = int(input("Enter Num1 : "))
        b = int(input("Enter Num2 : "))
        print(f"{a}^{b} ({a} to the power of {b}) = {power(a,b)}")
    elif option == "6":
        print("BYE")
        exit(0)
    else:
        print("INVALID OPTION")
