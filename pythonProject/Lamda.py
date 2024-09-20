'''
Python -Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''

# Lamda function
x=lambda a,b: a+b
print(x(10,20))


# pass argument lambda function
def myFunction(fun1,fun2):
    sum=fun1+fun2
    return sum
math1= lambda a,b: a+b
math2= lambda a,b: a-b
z=myFunction(math1(10,20),math2(20,5))
print(z)

# anonymous function inside another function

def function2(n):
    return lambda a,b: (a+b)*n
mydoubler = function2(10)
finalres= mydoubler(10,5)
print(finalres)


