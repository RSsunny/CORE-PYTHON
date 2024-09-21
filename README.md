
# Why Python?
Python is the most popular language at this time. Works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.

# Environment set up 

- Download Python your Desktop  [click here](https://www.python.org/downloads/)
- Download PyCharm for Python text editor [click here](https://www.jetbrains.com/pycharm/download/?section=windows)
- create new project

```python
print("Hello Python Programmer")
```

# Python Core concept 

- [Syntax](pythonProject/main.py)
- [Comment](pythonProject/main.py)
- [Variable](pythonProject/main.py)
- [Data Types](pythonProject/dataTypes.py)
- [Numbers](pythonProject/number.py)
- [Casting](pythonProject/modifyString.py)
- [String](pythonProject/StringMathod.py)
- [Booleans](pythonProject/dataTypes.py)
- [Operator](pythonProject/oprator.py)
- [Lists](pythonProject/List.py)
- [If-else](pythonProject/IfElse.py)
- [For loops](pythonProject/List.py)
- [Function](pythonProject/Function.py)
- [Lambda](pythonProject/Lamda.py)
- [Oop](pythonProject/Oop.py)
- [Polymorphism](pythonProject/Polymorphism.py)
- [Date and time](pythonProject/Dates.py)
- [Math](pythonProject/Math.py)

# problem solving 
```python
# show that 2024 is leap year 

year=2024
if year%100==0:
    if year%400==0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
elif year%4==0:
     print(f"{year} is leap year")
else :
     print(f"{year} is not leap year")
```


```python
# solve fibonacci series sum of 20 number =1,1,2,3,5,8,13,21..........N

arr=[1,1]
for num in range(3,20):
  x=  arr[num-3]+arr[num-2]
  arr.append(x)
for i in arr:
    sum+=i
print(arr)
print("sum of 20 numbers in seres: ",sum)
```
- [problem-1](pythonProject/Problem1.py) 
- [problem-2](pythonProject/Problem1.py)
- [problem-3](pythonProject/Problem1.py)
- [problem-4](pythonProject/Problem1.py)
- [problem-5](pythonProject/Problem1.py)


