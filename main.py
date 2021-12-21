# Blackjack Game 
'''Assumptions:
1. Infinite deck
2. Ace denoted by 1 or 11
3. If you and computer both go more than 21 then only you loose
'''
import random
import os

def allot_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def score(cards):
    val=sum(cards)
    if val==21 and len(cards)==2 :
        return 0
    if val>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player,comp):
    if player>21 and comp>21:
        print('You loose as you went over 21 !!!')
    elif player==comp:
        print('Draw score')
    elif comp==0:
        print('You loose as computer has a blackjack !!!')
    elif player==0:
        print('You have got a blackjack, you win !!!')
    elif player>21:
        print('You loose as you went over 21')
    elif comp>21:
        print('You win as computer went over 21')
    elif player>comp:
        print('You have higher score, you win !!!')
    else:
        print('Computer has higher score, you loose !!!')

def begin_game():
    player=[]
    comp=[]
    player_score=0
    comp_score=0
    cond=True
    while cond:
        os.system("cls")
        print('Welcome to the Blackjack / 21 Game')
        for _ in range(2):
            player.append(allot_cards())
            comp.append(allot_cards())
        player_score=score(player)
        comp_score=score(comp)
        print("Your score is",player_score)
        print("Your cards are",player)
        print("The computer's first card is",comp[0])
        if comp_score==0 or player_score==0 or player_score>21 or comp_score>21:
            cond=False
        print("""If you want to get another card, enter "yes" else enter "no" to pass""")
        choice=input()
        if choice=="yes":
            player.append(allot_cards())
            player_score=score(player)
        else:
            cond=False
        while comp_score!=0 and comp_score<17:
            comp.append(allot_cards())
            comp_score=score(comp)
        
        if player_score==0:
            player_score=21
        if comp_score==0:
            comp_score=21
        


        print(f"""Your final score is {player_score}
Your final cards are {player}
Computer's final score is {comp_score}
Computer's final cards are {comp}""")
        compare(player_score,comp_score)
        return
    

begin_game()
while True:
    print("""Do you want to play the game again?
Enter "yes" for yes and "no" for no""")
    choice=input()
    if choice=="yes":
        begin_game()
    else:
        print('The game ends')
        break
    





    
















