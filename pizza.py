print("Welcome to Python Pizza Devliveries!!")
size=input("What size do you want? S, M, L:\n")
pepperoni=input("Do tou want pepperoni on your pizza? Y or N:\n")
extra_cheese=input("Do you want extra cheese? Y or N:\n")
bill=0
if size == "S":
    bill = 15
    print("Small size pizza costs $15.")
    if pepperoni == "Y":
        bill += 2
        print("Addition of pepperoni for Small size pizza costs $2.")
elif size == "M":
    bill = 20
    print("Medium size pizza costs $20.")
    if pepperoni == "Y":
        bill += 3
        print("Addition of pepperoni for Medium size pizza costs $3.")
elif size == "L":
    bill = 25
    print("Large size pizza costs $25")
    if pepperoni == "Y":
        bill += 3
        print("Addition of pepperoni for Large size pizza costs $3.")
final_bill= bill
if extra_cheese == "Y":
    final_bill += 1
    print("Extra cheese costs $1.")
    print(f"Your Final bill is {final_bill}")
else:
    print(f"Your final bill is {final_bill}")