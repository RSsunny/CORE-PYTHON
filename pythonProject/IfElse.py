# If else
x=10
y=12
if x>y :
    x*=2
    print("x is a max number:",x)
elif x==y :
    print("x is equal to y")
else:
    y*=10
    print("Y is a max number:",y)
# -------------------------------------
# ternary operator
print("x is big number") if x>y else print("y is a big number")
z=0
if x : z=x+y
print(z)