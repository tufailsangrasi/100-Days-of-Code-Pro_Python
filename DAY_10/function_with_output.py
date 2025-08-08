# Function with Output

def my_function():
    result = 3 * 2
    return result

output = my_function()
print(output)

def table(num):
    multiple=1
    while multiple<=10:
        print(num, "x" , multiple, "=", num*multiple)
        multiple+=1

table(5)

# Positional Arguments
def my_function_position(a,b,c):
    print(a)

my_function_position(1,2,3)

#keyword positioning
def my_function_keywords(a,b,c):
    print(a,b,c)

my_function_keywords(a=1,c=2,b=4)

def char_letters(name):
    for name1 in name:
        print(name1)
print(char_letters("tufail"))

#
def character_letters(name):
    for name in range(3):
        print(name)
print(character_letters("tufail"))

# if you want to print 3 letters
def character_letter3(name):
    for i in range(3):
        print(name[i])


print(character_letter3("tufail"))


# love_Calculator
def love_calculator(name1 , name2):
    combined = (name1 + name2).lower()
    word1="true"
    word2="love"
    total1 = 0
    for letter in word1:
        count = combined.count(letter)
        print(letter.upper(), "occurs" , count , "times")
        total1 += count
    print(total1)

    total2 = 0
    for letter in word2:
        count = combined.count(letter)
        print(letter.upper(), "occurs" , count , "times")
        total2 += count
    print("Total" , total2)




love_calculator('Tufail' , "Dua")