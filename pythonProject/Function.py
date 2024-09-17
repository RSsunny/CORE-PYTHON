# Python - Function
# normal function stacture
def myFunction():
        print("normal function")

myFunction()

#  return function

def function2():
    return "this is return function"
x=function2()
print(x)

# received parameter and pass argument

def argFunction(x,y):
    sum=x+y
    return sum
total=argFunction(10,20)
print(total)

# default parameter

def function3(name="sunny"):
    return f"my name is {name}"
myName= function3("Hasib")
print(myName)

# pass manny data like list items
list=[155,562,452,63,544,25,365,23,452,42]
def function4(data):
    sum=0
    for i in data: sum+=i
    return sum
totalAmount=function4(list)
print(totalAmount)

# optional
from Oop import MyClass
totallist= MyClass.handlesum(list)
print(totallist)
