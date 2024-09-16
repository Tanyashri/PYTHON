import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7','8','9']
symbols = ['!', '#', '$', '%', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
no_letters = int(input("How manys letters would you like in your passowrd!\n"))
no_numbers = int(input("How many numbers would you like?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
password = ""
for char in range(1, no_letters+1):
    password += random.choice(letters)
for char in range (1, no_symbols + 1):
    password += random.choice(symbols)
for char in range(1, no_numbers+1):
    password += random.choice(numbers)
print(password)