class Person:
  def __init__(self, name, age):
    self.name = name 
    self.age = age 
    
   def introduce(self):
          print(f"Hi, my name is {self.name}and I am {self.age} years old")
     
class Student(Person):
  def __init__(self, name, age, grade):
    super().__init__(name, age)
    self.grade = grade 
  def display_student(self):
  print(f"Name: {self.name} | Grade: {self.grade}")
student1 = Student("Alice", 20, 95)

student1.intorduce()
student1.display_student()
