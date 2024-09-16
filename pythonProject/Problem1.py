from Oop import MyClass
'''
Problem -1
series= 1,3,5,7,9,11............99
sum of oded series
'''

sum=0
#
# for num in range(1,99):
#     if num%2==0:
#         continue
#     else:
#         sum+=num
# print(sum)

# for num in range(1,99):
#     if num%2!=0:
#         sum+=num
# print(sum)

# for num in range(1,99,2):
#         sum+=num
# print("sum of oded series : ",sum)
# -------------------------------------

'''
Problem -2
proved 2023 is not Leap Year!
'''
year=2023
if year%100==0:
    if year%400==0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
elif year%4==0:
     print(f"{year} is leap year")
else :
     print(f"{year} is not leap year")

# ----------------------------------------

'''
Problem -3
solve fibonacci series first 20 number =1,1,2,3,5,8,13,21..........N
'''

arr=[1,1]
for num in range(3,20):
  x=  arr[num-3]+arr[num-2]
  arr.append(x)
for i in arr:
    sum+=i
print(arr)
print("sum of 20 numbers in seres: ",sum)
# ------------------------------------------------
valueOfX= MyClass.x
print(valueOfX)
