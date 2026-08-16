class Student:
    college_name = "ABC College"




    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

print(s1.name)  # Output: Alice
print(s1.age)   # Output: 20