student_heights = input("enter").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_student = 0
for student in student_heights:
  number_of_student += 1
print(f"number of students = {number_of_student}")

avarage_hight = round(total_height/number_of_student)
print(f"average height = {avarage_hight}")
  