import random
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
         
def cal_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user,comp):
    if user==comp:
        return "Draw"
    elif comp==0:
        return "Lose, opponent has Blackjack"
    elif user==0:
        return "Win, with a Blackjack"
    elif user>21:
        return "You went over, You lose"     
    elif comp>21:
        return "Opponent went over, You win"
    elif user>comp:
        return "You win"
    else:
        return "You lose"
def play():
    user_card=[]
    comp_cards=[]
    comp=-1
    user=-1
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_cards())
        comp_cards.append(deal_cards())
    while not is_game_over:
        user=cal_score(user_card)
        comp=cal_score(comp_cards)
        print(f"Your cards: {user_card}, Current score: {user}")
        print(f"Computer's first card {comp_cards[0]}") 
        if user==0 or comp==0 or user>21:
            is_game_over=True
        else:
            another_card=input("Type 'y' to get another card, Type 'n' to pass: ")
            if another_card=='y':
                user_card.append(deal_cards())
            else:
                is_game_over=True

    while comp!=0 and comp<17:
        comp_cards.append(deal_cards())
        comp=cal_score(comp_cards)
    
    print(f"Your final hand: {user_card}, Your final score: {user}")
    print(f"Computer's fina hand: {comp_cards}, Computer's final score{comp}")
    print(compare(user,comp))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")=='y':
    print("\n"*20)
    play()
