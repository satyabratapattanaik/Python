# Defining Constructor

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 90)
print(s2.name, s2.marks)