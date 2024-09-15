# Python Numbers
'''
There are three numeric types in Python:
1. integer
2. float
3. complex
'''

x=10
y=15.50
z=12j

# print(type(y))
# print(type(z))
# print(type(x))

# convert integer to float integer to complex , float to integer ,float to complex

floatX=float(x)
complexX=complex(x)
# print(floatX)
# print(complexX)


integerY=int(y)
complexY=complex(y)
# print(integerY)
# print(complexY)


# note: can't convert complex numbers into another number type.
'''
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
'''

import random
myRandomNum=random.randrange(1,6)
print(myRandomNum)

