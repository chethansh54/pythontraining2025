# using modules in python
# inbuilt modules

import time

def sum_of_two(num1,num2):
    return num1+num2

def multiple(num1,num2):
    return num1*num2

print("Calling sum_of_two() function...")

start_time = (time.time()) # start timestamp for sum()
result = sum_of_two(1000000,20000000)
end_time = (time.time()) # start timestamp for sum()

time_taken = end_time - start_time

print(f"sum_of_two() function, took {time_taken/1000000000} nano-seconds to execute")

print("Calling multiply() function...")
start_time = (time.time()) # start timestamp for multiple()
result = multiple(34565432345678654323456787654323456765432,388383839393899999999999999999999999999999999999999)
end_time = (time.time()) # start timestamp for multiple()

time_taken = end_time - start_time

print(f"multiple() function, took {time_taken/1000000000} nano-seconds to execute")

print("Check Sleep Timer:")

import os
import sys

print(sys.platform)
