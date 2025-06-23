"""A simple Student class with private fields and property decorators"""

class Student:
    def __init__(self, id, firstname, lastname):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname
    
    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname
    

# Testing:

# Create a Student object
student = Student(1, "Alice", "Smith")

# Access properties
print(student.id)         # Should print: 1
print(student.firstname)  # Should print: Alice
print(student.lastname)   # Should print: Smith

# Modify properties
student.id = 2
student.firstname = "Bob"
student.lastname = "Johnson"

# Check the updated values
print(student.id)         # Should print: 2
print(student.firstname)  # Should print: Bob
print(student.lastname)   # Should print: Johnson