# fruits=["Apple" , "Banana" , "Peach"]
# for fruit in fruits:
#    print(fruit)
#    print(fruit + "Pie")
#print(fruits) Intentation is important this line will run after the whole for loop ends

fruits=["Apple" , "Banana" , "Peach" , "Tufail" , "Sanjay" , "Akasha"]
for i in range(3):
    print(fruits[i])

# sum of lists program
student_score = [185 , 165 , 147 , 100 , 84 , 178]
total_score = sum(student_score)
print(total_score)

# How the sum methods works it is depend on for loop
sum=0
for score in student_score:
    sum+=score

print(sum)

# write for max method which gives us maximum no in the list using for loop
max_score=0
student_score = [185 , 165 , 147 , 100 , 84 , 178]
for score in student_score:
    if score > max_score:
        max_score = score

print(max)

# Range function
for number in range(1, 10):
    print(number)

for number in range(1, 10 , 3):
    print(number)

# Sum of numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number

print(total)