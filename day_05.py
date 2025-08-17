          # ------------------------------------------------------------
          #                   Loops in Python
          #-------------------------------------------------------------

student_list = ["Tufail" , "Ahmed" , "Muzammil"]
for name in student_list:
  print(name)

# Calculate the sum score using sum method then calculate it using for loop
stu_score = [90 ,91  ,82 , 65 , 78 ,]
total_score = sum(stu_score)
#print(total_score)

sum = 0
for score in stu_score:
  sum+= score
#print(sum)

# Max score from the list
max_score = 0
for score in stu_score:
  if score > max_score:
    max_score = score

#print(max_score)
#print(max(stu_score))

# Range function
for num in range(1,6):
    print(num)

for number in range(1, 10 , 4):  # (strat  , stop , step)
    print(number)