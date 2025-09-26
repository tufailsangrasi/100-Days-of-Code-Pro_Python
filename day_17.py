class Student:
  # Attributes of class
  name = ""
  roll_no = ""
  dept = ""
  age = 0

# Constructor to set the values
  def __init__(self ,name , roll_no , dept , age):
    # No 'self', so these only affect class variables
    Student.name = name
    Student.roll_no = roll_no
    Student.dept = dept
    Student.age = age

# Methods to get values
  def get_details(self):
    print(Student.name , Student.roll_no , Student.dept , Student.age)

# Both objects ended up sharing the same values (last assigned) 
tufail = Student("Tufail" , "22SW071" , "Software" , 20)
zaheer = Student("Zaheer" , "22SW077" , "Software" , 21)
tufail.get_details()
zaheer.get_details()

class Student_self:
  # Attributes of class
  name = ""
  roll_no = ""
  dept = ""
  age = 0

# Constructor to set the values
  def __init__(self ,name , roll_no , dept , age):
    # with self keyword assign object values
    self.name = name
    self.roll_no = roll_no
    self.dept = dept
    self.age = age

# Methods to get values
  def get_details(self):
    print(self.name , self.roll_no , self.dept , self.age)

# Both objects ended up with their assign values 
tufail = Student_self("Tufail" , "22SW071" , "Software" , 20)
zaheer = Student_self("Zaheer" , "22SW077" , "Software" , 21)
tufail.get_details()
zaheer.get_details()




  






  


