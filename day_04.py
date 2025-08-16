# list -> collection of different datatypes
# Nested list
# Iterate list 
# Choosing a random number from list
# add another member in list using append method

fruits = ["Apple" , "Banana" , "Mango" , "Peach" , 1]
#print(fruits[0])
#print(fruits[1])
#print(fruits[2])
# Reverse iteration
#print(fruits[-1])
#print(1 in fruits)
#print("Apple" in fruits)
#print("Banana" in fruits)
#print("Peach" in fruits)

# Operation on list
fruits.append("Pineapple")
fruits.insert(1 , "Strawberry")
#print(fruits)
#fruits.sort()
#print(len(fruits))

stu_names = ["Tufail" , "Muzammil" , "Zaheer" , "Sunjay" , "Sajid"]
stu_roll_num = ["22SW071" , "22SW074" , "22SW077" , "22SW050" , "22SW053"]
stu_data = int(input("Enter the index of student:"))
print(stu_names[stu_data] , stu_roll_num[stu_data])

# Concatenation using +
numbers = [1 , 2 , 3]
alphabets = ["A" , "B" , "C"]
combine = numbers + alphabets
print(combine)





