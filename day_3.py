print("Hello World")
print("Welcome to Python")

distance=100
time=0.5
speed=0

print("Our Variables:")
print(f"Distance = {distance}")
print(f"Time = {time}")
print(f"Speed = {speed}")

speed=distance/time

print(f"Updated Value of Speed = {speed}")

print("=====================================")
print("Speed Limit Checker Camera")
print("=====================================")

minimum_speed=80.0

if speed <= minimum_speed:
    print(f"Your Speed was {speed} KM/H and it is safe.")
elif speed > minimum_speed:
    print(f"Speed Limit Violation Detected ! Your Speed is {speed} KM/H, Please go slow.")
    print(f"Drive Safely!!")

    if speed > 140:
        print(f"Your Speed is very high, {speed} KM/H !!")
        print(f"Please slow down, or else you will be arrested")









