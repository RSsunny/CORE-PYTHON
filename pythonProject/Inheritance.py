# Python Inheritance
''' 
Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class.
'''

# Create a Parent Class
class Person:
    def __init__(self,fName,lName):
        self.firstName= fName
        self.lastName= lName

    def printName(self):
        print(self.firstName,self.lastName)


x= Person("Sunny","Sharif")
x.printName()

# Create a Child Class
class Student(Person):
  pass