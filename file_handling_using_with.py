
# with open("story.txt", "r") as story_file:
#     for line in story_file:
#         print(f"No. Of Characters = {len(line)}") # CHARACTER / LETTER COUNT
#         print(f"Words in the Line = {len(line.split(' '))}") # WORD COUNT
# print("Thanks")

with open("story.txt", "r") as story_file:
    total_word_count = 0
    for line in story_file:
        line_word_count = len(line.split(' '))
        total_word_count = total_word_count + line_word_count

    print(f"TOTAL WORDS IN THE FILE : {total_word_count}")

print("Thanks")

with open("story.txt", "r") as story_file:
    total_char_count = 0
    for line in story_file:
        line_char_count = len(line)
        total_char_count = total_char_count + line_char_count

    print(f"TOTAL CHARACTERS IN THE FILE : {total_char_count}")

print("Thanks")