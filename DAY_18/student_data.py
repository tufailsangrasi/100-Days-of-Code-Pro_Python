class Student():
    stu_id = ''
    stu_name = ''
    stu_dept = ''
    def __init__(self,stu_id , stu_name , stu_dept):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_dept = stu_dept

    def getter(self):
        print(self.stu_id, self.stu_name, self.stu_dept)


student_01 = Student("22SW071" , "Tufail" , "Software")
student_01.getter()
