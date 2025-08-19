# Function -> perfrom specific task , () is identifier , and makes code reusable
# Python have alot of built in function which used to perform specific tasks

# len() (a builtin function)
length = len("Tufail")
#print(length)

# def keyword is used for function and identation is necessary!
def greetings():
  print("Good Evening")

# calling (revoke) a function
#greetings()

# Maximum of Three Numbers
def max_num():
  list = [20 , 22 , 30]
  for max in list:
      num = 0
      if max > num:
         num = max
  return max

print("The Maximum number in list:", max_num())

# Sum All Numbers in a List
list = [8, 2, 3, 0, 7]
def sum_list(list):
    sum = 0
    for num in list:
       sum += num
    return sum

print("The sum of list:" , sum_list(list))
