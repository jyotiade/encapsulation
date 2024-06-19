class student:
    school="ips"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def details(self):
        print("name",self.__name)
        print("age",self.__age)
        print("school=",student.school )
    
class Marks(student):
    def marks(self,hindi,math):
        self.hindi=hindi
        self.math=math
    def complete_detail(self):
        print("name",self.name)
        print("Age",self.__age)
        print("school",student.school)
        print("hindi",self.hindi)
        print("hindi",self.math)

obj=Marks("viti",21)
obj.__name="jyoti"
obj.details()
obj.marks(34,45)
student.school="ideal public school"
obj.complete_detail()
