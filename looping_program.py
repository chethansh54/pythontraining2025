n=10

# print pattern * 10 times 

while n>0:
    print("*",end="")
    n = n - 1
    # can also be written as n-=2 
    # # n = n - 1, means, shortcut operation to do minus 1 of variable n

print() # prints a blank new line


print("Now we will print pattern using for loop:")
# meaning, for i=0 ; i<10; i++
# but in python, we need to write like below

limit=5
for i in range(1,limit+1):
    print("*"*i)


print()

# Assignment:
'''
*
**
***
****
*****
'''