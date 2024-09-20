class MyClass:
   x=20
   y=30

   def __init__(self, name, age):
       self.name = name
       self.age = age

   # Python Inheritance
   def instanceMathod(self,boy):
        print(f"this is a normal function {self.name} {boy}")


   def handlesum(arr):
       totalvalue = 0
       for i in arr:
          totalvalue +=i
       return totalvalue
   @classmethod
   def ClassMethod(cls,):
       print(f"this is class method {cls}")


