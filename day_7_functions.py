# Functions in python

def add_numbers(number_1, number_2):
    sum_value = number_1 + number_2

    return sum_value

def display():
    print("Namaste")
    print("Khonichiva")

def greet(name):
    print(f"Hello, {name}")
    

x = 10
y= 20

sum = add_numbers(10,20)
print(f"Sum = {sum}")

x = 100
y = 300

sum = add_numbers(x,y)

print(f"Sum = {sum}")

greet("Chetan")
greet("gaurav")
greet("Daya")
greet("Virat")
greet("Rohit")

def greet_based_on_time(name):
    # write time based code
    print(f"Hello, {name} : Good Morning")

greet("Suresh")
greet("Suryakumar")


greet_based_on_time("Chetan")
greet_based_on_time("Sachin")