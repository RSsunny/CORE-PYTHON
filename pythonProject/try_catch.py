# Python Try Except and raise
from sys import exception

try:
    print("x is define", x)
except NameError:
    print(f"x is not define")
# throw a new arrow
y=False
if y is True:
    print("y present")
else:
    raise TypeError("Y Is falsy value")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")