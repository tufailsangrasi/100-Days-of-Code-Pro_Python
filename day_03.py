# Control Statements (if , elif , else)
# Module
# Comparison operators

# Even or Odd Detector
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

# Password Checker
stored_password = "22SW071"
user_enter_pass = input("Enter your password")
if stored_password == user_enter_pass:
  print("Access granted")
else:
  print("Access Denied")

# Grade based on marks
subject = "Artifical Intelligence"
marks_scored = int(input(f"What is your marks in {subject}:"))
if marks_scored >= 90:
  print("Your Grade is A+")
elif marks_scored > 80 and marks_scored < 90:
  print("Your Grade is A")
elif marks_scored > 70 and marks_scored <= 80:
  print("Your Grade is B+")
elif marks_scored >= 65 and marks_scored <= 70:
  print("Your Grade is B")
else:
  print("Sorry you are Fail")

# Write a program which finds out whether a given name is present in a list or not.
student_list = ['Tufail' ,'Sunjay','Zaheer','Varoon','Muzammil' , 'Sajid' ]
check_name =input("Enter the student name:Format[T____]")
if check_name in student_list:
  print(f"{check_name} a student of SWE Dept")
else:
  print(f"{check_name} is not present in list")

# Write a program to find out whether a given post is talking about “tufail” or not.
post_info = input("Enter the post:")
if "tufail" in post_info.lower:
  print("The post is talking about Tufail")
else:
  print("The post is not talking about Tufail")




