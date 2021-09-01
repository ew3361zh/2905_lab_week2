"""Part 3: Student dataclass

Type in the dataclass code from the slides/video. You would have done this before class.

Add one more field: gpa, a float

Write a main function to create some example Student objects with some example names, college_id and GPA values. 

Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 

Add some comments in your code to compare the dataclass version to the "traditional" version"""

#this is part of the python library, not a pip3 import external library
from dataclasses import dataclass

@dataclass
class Student:
    # don't need init nor str methods to initialize object
    # change object variables to specify datatypes (new!)
    name: str
    college_id: str
    gpa: float 
    # the above on their own allow for representing the class objects as a string but it's a little clunky compared to the original version
    # so perhaps include this version which still works when using the dataclass version to make it a little cleaner
    
    # def __str__(self):
    #     return f'Name: {self.name}, GPA: {self.gpa}'

def main():
    freddo = Student('Freddo', 'rh7675kj', 3.66)
    print(freddo.name)
    print(freddo.college_id)
    print(freddo.gpa)
    #print out string representation of student object
    print(freddo)

    kiki = Student('Kiki', 'pj9878ah', 2.99)
    print(kiki)

main()