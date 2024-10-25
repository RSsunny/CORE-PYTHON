# EMI rate calculator

amount= input("inter your amount = ")
rate= input("inter your rate = ")
month= input("inter your month = ")



def ratecalculate():
    total=int(amount)+(((int(rate)*int(amount))/100)*int(month))


    return total
result=ratecalculate()
print(result)

