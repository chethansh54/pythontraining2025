# data handling using csv module

import csv

csv_file_name = "students.csv"

# CSV READING
with open(csv_file_name) as mycsvfile:
    print("Reading CSV File ....")
    students_csv = csv.reader(mycsvfile)

    for row in students_csv:
        print(row)

# CSV WRITING
with open(csv_file_name, "a") as mycsvfile:
    print("Writing To CSV File....")
    students_csv = csv.writer(mycsvfile)

    student_name = input("Enter Student Name : ")
    student_class = input("Enter Student Class : ")
    student_age = input("Enter Student Age : ")
    student_rank = input("Enter Student Rank : ")
    student_place = input("Enter Student Place : ")

    row_list = [student_name, student_class, student_age, student_rank, student_place]

    students_csv.writerow(row_list)

