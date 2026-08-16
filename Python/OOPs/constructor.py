class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stud1 = Student("Alice",9.0)
stud2 = Student("Bob",8.5)

print(stud1.name)
print(stud2.name)
print(stud1.get_cgpa())
print(stud2.get_cgpa())


