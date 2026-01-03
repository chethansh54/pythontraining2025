name="Daya"

print(f"Name = {name}")

print(f"First letter of name : {name[0]}")
print(f"Last letter of name : {name[-1]}")

text_data = "The quick brown fox jumped over a lazy dog"

print(f"Sentence = {text_data}")

words_list = text_data.split()

reversed_sentence = words_list[::-1]

reversed_sentence = " ".join(reversed_sentence)

print(f"Reveresed Sentence = {reversed_sentence}")

print(text_data.upper())
print(text_data.lower())
print(text_data.capitalize())
print(text_data.endswith("dog"))
