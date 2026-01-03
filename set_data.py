students={"ankur", "daya", "gaurav", "daya"}

students.add("Arjun")

print(f"Students = {students}")
print(f"Students Count = {len(students)}")

fruits=set()

fruits.add("Mango")
fruits.add("Mango")
fruits.add("Mango")
fruits.add("Mango")
fruits.add("Mango")
fruits.add("Mango")
fruits.add("Guava")
fruits.add("Guava")
fruits.add("Orange")
fruits.add("Orange")
fruits.add("Orange")
fruits.add("Kiwi")
fruits.add("Kiwi")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")
fruits.add("Avocado")

print(f"Types Of Fruits in fruits Bag : {fruits}")

football_team={"daya","gaurav","bhargav","arjun","bhishm","bheem"}

badminton_team={"arjun","indra","abhimanyu","gaurav"}

# all sports students

print(f"All Sports Students : {football_team.union(badminton_team)}")

# all students who play football and badminton

print(f"All Rounders Are : {football_team.intersection(badminton_team)}")

# all students who play badmiton but not football

print(f"Pure Badminton Players Are : {badminton_team.difference(football_team)}")
print(f"Pure Football Players Are : {football_team.difference(badminton_team)}")


data_list=["mango","guava","guava","kiwi","kiwi","kiwi"]

print(f"All Fruits Type : {set(data_list)}")
