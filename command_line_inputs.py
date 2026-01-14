import sys
input_1 = sys.argv[1]

# using command line input, wish in different languages

input_2 = sys.argv[2]

if input_2 =="english":
    print(f"Hello, {input_1}")
elif input_2 =="hindi":
    print(f"Namaste, {input_1}")
elif input_2 =="japanese":
    print(f"Khonichiva Senpai, {input_1}")
elif input_2 =="gujrati":
    print(f"Kem Cho Mota Bhai, {input_1} ?")
else:
    print(f"No Language matched, so, just Hello {input_1}")