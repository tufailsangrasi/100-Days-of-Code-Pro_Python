from turtle import Turtle , Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red" , "brown")

# Making an Square
for i in range(1,5):
  timmy.forward(40)
  timmy.left(90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Names" , ["Tufail" , "Muzammil" , "Zaheer" , "Sunjay"])
table.add_column("Roll_No" , ["22SW071", "22SW074" , "22SW077" , "22SW050"])
table.align = "l"
print(table)