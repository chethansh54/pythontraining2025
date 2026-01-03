# Collections
# List
# Set
# Dictionary
# String


data=[10,"data items",True,40, "maths", 20, 40, 20, 10, 40]

# data insert

data.append(1000)
data.append(2000)

list_count = data.count(20)

print(f"Data List = {data}")
print(f"Data Count = {list_count}")
print(f"Data List Size = {len(data)}")

# data update
data[1] = "item"
data[2] = False

print(f"Data List = {data}")

# data read

item_1=data[0]
item_2=data[1]
item_3=data[2]
item_4=data[3]
item_5=data[4]

print(f"Item 1 = {item_1}")
print(f"Item 2 = {item_2}")
print(f"Item 3 = {item_3}")
print(f"Item 4 = {item_4}")
print(f"Item 5 = {item_5}")

# read using for loop

for item in data:
    print(f"Item = {item}")

for index in range(0, len(data)):
    print(f"Item No. {index} = {data[index]}")

# removing data from list
# using pop()

data.pop() # removes items from rightmost end / removes last item / if index is given, removes from that index

print(f"List After Popping : {data}")

# using remove()
# removes given element 

data.remove(40) # removes element with value 1000

print(f"Data List After remove : {data}")

data.pop(5) # remove element at index 5

print(f"Data : {data}")

print(f" Size Of List Now : {len(data)}")


data.clear()

print(f"List Cleared, List Data Now : {data}")