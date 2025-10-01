# We call an attribute with class name . and for an instance we used object .
class Dog:
  species = "Canine"  # class attribute

  def __init__(self , name , age): # instance variable
    self.name = name
    self.age = age

doggy = Dog("Buddy",3)
doggy.species = "Fenine"
#print(doggy.name)
#print(doggy.age)
#print(doggy.species)
#print(Dog.species) # class attribute calling using class name

# Single Inheritance 
class Animal:
  def __init__(self , species):
    self.species = species

class dog(Animal):
  def __init__(self , name , age , species):
    super().__init__(species)
    self.name = name
    self.age = age

  def get_info(self):
    print(f"Species",({self.species}))
    print(f"Name :", {self.name})
    print(f"Age :", {self.age})

class cat(Animal):
  def __init__(self , name , color , species):
    super().__init__(species)
    self.name = name
    self.color = color
    self.species = species
  
  def get_info(self):
    print(f"Name :{self.name}")
    print(f"Color:{self.color}")
    print(f"Species:{self.species}")


doggy = dog("Buddy" , 3 , "Fenine")
#doggy.get_info()

catty = cat("Mow" , "White" , "Domestic")
#catty.get_info()

# Multilevel Inheritance
# LivingBeing > Animals > Dog
class livingBeing:
  def breath(self):
    print("Can Breath")

class Animal(livingBeing):
  def __init__(self , species):
    self.species = species

class Dog(Animal):
  def __init__(self , name , color , species):
    super().__init__(species)
    self.name = name
    self.color = color
    self.species = species

  def info(self):
    print(f"Name :{self.name} Color :{self.color} , Species :{self.species}")


livings = livingBeing()
animal = Animal("Domestic")
doggy = Dog("Buddy" , 3 , animal.species)
#doggy.info()

# Multiple Inheritance
# Father + Mother > child , concept of MRO

class father:
  def can_drive(self):
    print("Can drive a car")

class mother:
  def can_cook(self):
    print("Can cook food")

class child(father , mother):
  def __init__(self):
    print("Can have Both")

childs = child()
childs.can_cook()
childs.can_drive()