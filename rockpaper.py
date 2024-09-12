import random
user_choice=int(input("What do you choose? Typr 0 for Rock, 1 for Paper or 2 fro Scissors.\n"))
comp_choice=random.randint(0, 2)
print(f"Computer Choice: {comp_choice}")
if user_choice >= 3 or user_choice <0:
        print("You typed an invalid number. You lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif user_choice > comp_choice:
    print("You Win")    
elif user_choice == 2 and comp_choice == 0:
    print("You lose.")
elif comp_choice > user_choice:
    print("You Lose.")
elif comp_choice == user_choice: 
    print("It's a draw.")
