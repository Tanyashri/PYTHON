import random
import hangamnwords
lives = 6
choices = random.choice(hangamnwords)
placeholder = ""
word_lenght = len(choices)
for position in range(word_lenght):
    placeholder += "_ "
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display =""

    for letter in choice:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
            
        else:
            display += "_"
    print(display)
    if guess not in choices:
        lives -= 1
        print(f"Your lives {lives}")
        if lives == 0:
            game_over = True
            print("YOU LOSE")
    if "_" not in display:
        game_over = True
        print("You win")

