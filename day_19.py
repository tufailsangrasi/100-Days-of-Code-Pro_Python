# Polymorphism 
# 1.Compile time polymorphism -> Overloading (same name , different parameters)
# 2.Runtime Polymorphism -> Overriden 
class university:

  def info(self , name):
    self.name = name
  
  def info(self , name , location):
    self.name = name
    self.location = location

  def details(self):
    print(self.name)
    print(self.location)

# Main methods
muet = university()
muet.info("Mehran1")
muet.info("Mehran" , "Jamshoro")
muet.details()
