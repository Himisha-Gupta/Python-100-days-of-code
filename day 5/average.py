# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height = 0
for heights in student_heights:
    height += heights

#print(height)

number_of_students = 0
for number in student_heights:
    number_of_students+= 1

#print(number_of_students)

average = height/number_of_students
print(round(average))


