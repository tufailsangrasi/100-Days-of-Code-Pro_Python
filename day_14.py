import random
# Higher lower game
higher_persons = ['Virat kohli' , 'Critinio Ronaldo' , 'Babar Azam']
lower_persons = ['Asif Ali','Zain Awan','Tufail']

user_input = input("Type A or B")

high_random = random.choice(higher_persons)
low_random = random.choice(lower_persons)

print(f"Which is richest persons {high_random} vs {low_random}")

score = 0
if user_input == 'A' and 