# story_data = open("story.txt", "w")

# story_data.write("NEW NEW I am Writing New Content ....")
# story_data.write("\n")
# story_data.write("NEW NEW Hello I am Writing New Content ....")

# story_data.close()


story_data = open("story.txt", "a")

story_data.write("I AM APPENDING THESE LINES...")
story_data.write("\n")
story_data.write("This is new data, but joined along with existing data\n")
story_data.write("There was a king and blah blah...\n")

story_data.close()