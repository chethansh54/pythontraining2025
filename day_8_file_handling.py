# handling files
# open, read, write, append

story_file = open("story.txt", "r") # open in read mode

data = story_file.read()

print(f"File Data = ")
print(data)

story_file.close() # file closed

##########################################################################3
# Read the file line by line

story_file = open("story.txt", "r") # open in read mode

total_lines = 0
for i in range(5):
    data = story_file.readline() # copy one line of the file at a time
    print(f"Line No. {i} : {data}")
    if data != "":
        total_lines = total_lines + 1

print(f" TOTAL LINES = {total_lines}")

story_file.close() # file closed