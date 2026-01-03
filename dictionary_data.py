employee_data={"name" : "daya", "salary" : 10000, "place" : "bangalore"}

employees_data = {
    "employee_1" : {"name" : "daya", "salary" : 10000, "place" : "bangalore"},
    "employee_2" : {"name" : "gaurav", "salary" : 10000, "place" : "bangalore"},
    "employee_3" : {"name" : "arjun", "salary" : 10000, "place" : "noida"},
    "employee_4" : {"name" : "bheem", "salary" : 10000, "place" : "bangalore"},
    "employee_5" : {"name" : "chetan", "salary" : 15000, "place" : "bengal"},
    "employee_6" : {"name" : "nakul", "salary" : 20000, "place" : "mumbai"},
}

print(f"Single Employee Data : {employee_data}")
print(f"All Employee Data : {employees_data}")

employee_1_data = employees_data["employee_1"]

print(f"Employee 1 Data : {employee_1_data}")

for item in employees_data:
    print(employees_data[item])

for data in employees_data.items():
    print(data)

daya_salary = employee_data.get("salary")
print(f"Salary Of Daya is Rs {daya_salary}")

employee_data["salary"] = 20000
daya_salary = employee_data.get("salary")
print(f"Salary Of Daya is Rs {daya_salary}")


user_accounts = {}

username=input("Enter Username:")
password=input("Enter Password:")

user_accounts[username] = password

print(f"User Details  : {user_accounts}")

username=input("Enter Username:")
password=input("Enter Password:")

user_accounts[username] = password

print(f"User Details  : {user_accounts}")