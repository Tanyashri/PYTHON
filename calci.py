print("Welcome to the Tip Calculator")
a=float(input("What was the total bill?"))
b=int(input("How much tip  would you like to give? 10, 12 or 15? "))
c=int(input("How many people to split the bill? "))
d=(b/100*a+a)/c
print("Each person should pay:" + str(round(d,2)))  