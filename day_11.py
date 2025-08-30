 # Lab_Task# 6
import math
import random
#1.	Write a Python program which accepts the radius of a circle from the user and compute the area
# radius = input("Enter the radius:")
# area_of_circle = 2 * math.pi * float(radius)
#print(round(area_of_circle, 2))


# 2.	Write a Python program to guess a number between 1 to 9. Hint(use radom method to randomly generate numbers).
# print(round(random.random() * 10));

#3.	Write a Python program that accepts a word from the user and reverse it.
# user_word = input("Enter the word:");
# print("".join(reversed(user_word)));

# 4.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.

# for i in range(0, 7): 
#   if(i % 3 == 0):
#     continue
#   else:
#     print(i)


# 5.	Write a Python program which iterates the integers from 1 to 50. For multiples of three print “Multiple of 3" instead of the number and for the multiples of five print “Multiple of 5". For numbers which are multiples of both three and five print “Multiple of both 3 & 5".

# for i in range(1, 51): 
#   if(i % 3 == 0):
#     print(f"{i} Multiple of 3")
#   if(i % 5 == 0):
#     print(f"{i} Multiple of 5")
#   if(i%3 == 0 and i % 5 == 0):
#     print(f"{i} Multiple of 3 & 5")

# 6.	Write a Python program to check whether an alphabet is a vowel or consonant.

# alphabet = input("Enter alphabet: ");
# vowels = ["a", "e", "i", "o", "u"];
# if(alphabet in vowels):
#   print(f"{alphabet} is vowel")
# else:
#   print(f"{alphabet} is constant")

# temp = float(input("Enter the temperature in Celcius:"))
# temp_in_farhen= (1.8 * temp ) + 32
# print(round(temp_in_farhen , 2))

# 1.	Write a marksheet and display marks obtained, percentage and grade
marks = int(input("Enter marks: "));
name = input("Enter name: ");
total = int(input("Enter total marks: "));
percentage = marks/total * 100;

grade = "A+"

if(percentage > 80 and percentage < 90): 
  grade = "A"
elif(percentage > 70 and percentage < 80): 
  grade = "B+"
elif(percentage > 60 and percentage < 70): 
  grade = "B"
else:
  grade = "C"



print(f"------------- MarkSheet of {name} ---------------")
print(f"|             percentage:     {percentage}%               |")
print(f"|             obtain:     {marks}                  |")
print(f"|             grade:     {grade}                    |")
print("------------------------------------------------")


# 2.	Write a program for table 
num = int(input("Enter number to print table: ")); 

for i in range(1, 11): 
  print(f"{num} * {i} = ", i * num)
  