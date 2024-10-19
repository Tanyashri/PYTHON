from random import randint
Easy_level_turns=10
Hard_level_turns=5
turn=0

def check_answer(user_guess,actual_answer,turn):
    if user_guess>actual_answer:
        print("Too high.")
        return turn-1
    elif user_guess<actual_answer:
        print("Too low")
        return turn-1
    else:
        print(f"You got it! The answer was {actual_answer}")
        
def game():       
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100")
    num=randint(1,100)

    def set_difficulty():
        level=input("Choose a difficulty. TYpe 'easy' or 'hard':")
        if level=='easy':
            return Easy_level_turns
        else:
            return Hard_level_turns
            
    turn=set_difficulty()

    guess=0
    while guess!=num:
        print(f"You have {turn} attempts remaining to guess the number")

        guess=int(input("Make a guess:"))
        turn=check_answer(guess,num,turn)
            
game()