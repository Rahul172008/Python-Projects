print("===== Student Grade Management System =====")

name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n----- Student Report -----")
print("Student Name :", name)
print("Marks        :", marks)
print("Grade        :", grade)