student_score = {
    "Zaheer": 83 ,
    "Tufail": 91 ,
    "Varoon": 78 ,
    "Sunjay": 54 ,
    "Draco": 74
}

#TODO-1 Create an empty dictionary for student_grades
student_grades = {}

# TODO-2 write your code below to add the grades to student
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)