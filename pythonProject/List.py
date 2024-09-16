# Python List
from Oop import MyClass

studentName=["Sunny","Hasib","Ashik","juwel"]
studentRoll=[15,25,36,45]
sumOfRoll=MyClass.handlesum(studentRoll)
print(sumOfRoll)
thislist = ["apple", "banana", "cherry", "apple"]

print(thislist[2:4]) # index number 2 theke 4 index er ag projonto
print(thislist[2:])
print(thislist[:2])
if "cherry" in thislist: print("cherry is present")
thislist.insert(2, "watermelon")


newarr=thislist.copy()
newarr.append("mango")
print(newarr)


# Join
arr1=["apple", "banana", "cherry", "apple"]
arr2=[1,5,6,2,5,3,4]
arr3=arr1+arr2
print(arr3)
#or
arr3x=arr1.copy()
for i in arr2: arr3x.append(i)
print(arr3x)
# or
arr1.extend(arr2)
print(arr1)
# ------------------------

# List Method

# sort
listArr=[12,54,65,25,3,58,52,65,48,25,85,23,65,12,41,25,23,12,58,562,58,565,25,412,425]
listArr.sort(reverse=True,)
print(listArr)
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
def handlebar(e):
    return e["year"]
cars.sort(reverse=True, key=handlebar)
print(cars)

