# Exception Handling with try & except blocks
try:
    student_data={
        "101" : {
            "name" :"Daya",
            "eng" : 10,
            "math" : 10,
            "sci" : 10
        }
    }

    # RISKY CODE
    try:
        rollno = input("Enter rollno : ")
        print(f"Student With RollNo {rollno} : ")
        print(student_data[rollno])
    except Exception as error_message:
        print("The Given Student is not in our database")

    print("Line:1 Other Statements and Other code")
    print("Line:2 Other Statements and Other code")
    print("Line:3 Other Statements and Other code")
    print("Line:4 Other Statements and Other code")
except Exception as e:
    print(e)