"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "General"
    def __init__ (self, name, age):
        self.name = name
        self.age = age

        def display_info(self):
            return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    category = "Student"

    def __init__(self, name, age, major, grade):
        super() .__init__(name, age)
        self.major = major
        self.grade = grade

        def display_info(self):
            return (
                f"Name: {self.name}, Age: {self.age}, "
                f"Major: {self.major}, Grade: {self.grade}"
            )
        def study(self):
            return f"{self.name} is studying {self.major}."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Amari", 27, "Computer Science", "A")
    student2 = ChildClass("Amir", 1, "Early Learning", "N/A")

    print("Class category:", ChildClass.category)

    print("Student 1 category:", student1.category)

    student1.favorite_subject = "Programming"

    print("Student 1 namespace:", student1.__dict__)
    print("Student 2 namespace:", student2.__dict__)

    print("Class namespace:", ChildClass.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "name": "Amari",
        "courses": ["Python", "Data Structures"]

    }
    shallow = copy(original)

    deep = deepcopy(original)

    orinal["courses"].append("Cybersecurity")

    print("Original object:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent = ParentClass("Amari", 27)
    print("\nParent object:")
    print("Available methods:", dir(parent))
    print(parent.display_info())

    child = ChildClass("Amari", 27, "Computer Science", "A")
    print("\nChild object:")
    print(child.display_info())
    print(child.study())


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()