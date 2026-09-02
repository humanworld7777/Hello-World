</> Python
class Student:
  def __init__(self, name, grade):
    self.name = name 
    self.grade = grade

  def display_info(self):
    print(f"Student Name: {self.name} | Grade: {self.grade}")

student1 = Student("Alice", 9)
student2 = Student("Bob", 8)


student1.display_info()
student2.display_info()
