# simple calculator

value_1=1000
value_2=1500
x=10

print(f"value_1 = {value_1}")
print(f"value_2 = {value_2}")

sum_value = value_1 + value_2
diff_value = value_2 - value_1
product_value = value_1 * 2
division_value = value_1 / 3
floor_division_value = value_1 // 3

power_value_square = x ** 2 # x square
power_value_cube = x ** 3 # x cube

print(f"Sum = {sum_value}")
print(f"Difference = {diff_value}")
print(f"Product = {product_value}")
print(f"Division = {division_value}")
print(f"Floor Division = {floor_division_value}")
print(f"Power Of 2 = {power_value_square}")
print(f"Power of 3 = {power_value_cube}")

string_data = "*" * 5
print(f"String Multipled = {string_data}")

first_name = "Jethalal"
last_name = "gada"

full_name = first_name + " " + last_name

print(f" Full Name = {full_name}")


x = 20
y = 20 


print(f"x = {x} , y={y}")
print(f" x>y = {x>y}")
print(f" x>=y = {x>=y}")
print(f" x<y = {x<y}")
print(f" x<=y = {x<=y}")
print(f" x==y = {x==y}")
print(f" x!=y = {x!=y}")


if x >= y:
    print("x is greater/equal than y")


x = 30
if x == 20 or x % 2 == 0:
    print(f"{x} is even number")

x = 30

if not x == 30:
    print("The condition x==30, was never true. it was a lie")

speed = None # un allocated / un-assigned / null / nothing
print(f"Speed = {speed}")

distance = 10
time = 20 

speed = distance/time

print(f"Speed = {speed}")

