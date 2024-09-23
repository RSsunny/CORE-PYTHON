# Python For Loops

'''
A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

sum = 0
for i in range(6): # range means 0 to under the value
    sum+=i
print(f"The sum of range {sum}")  # formating string

# break

for i in range(10):
    if i>5: break
    print(i)

 # continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": continue
  print(x)


#  nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)