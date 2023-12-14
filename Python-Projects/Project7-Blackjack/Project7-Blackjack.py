import random
from blackjack_art import *
from All_Cards import *
import sys
from art import *
from Cards_Ascii_Art_Code import *
Game_Over=False
def random_card():
    """Returns a random card from the deck!"""
    return random.choice(cards_lst)
def score_generator(cards_lst):
    """Returns the total of the deck provided!"""
    score = 0
    for i in cards_lst:
        score+=cards_lst_points[(str(i).split()[1])]
    if score == 21 and len(cards_lst) == 2:
        return 0
    if 11 in cards_lst and score > 21:
        cards_lst.remove(11)
        cards_lst.append(1)
    return score
def Score_comparsion(Player_score, Dealer_score):
  if Player_score > 21 and Dealer_score > 21:
    return text2art('You Lost!')
  if Player_score == Dealer_score:
    return text2art("Draw")
  elif Dealer_score == 0:
    return text2art("You Lost!\nDealer has Blackjack!")
  elif Player_score == 0:
    return text2art('You won \n with a Blackjack!')
  elif Player_score > 21:
    return text2art('You Lost!')
  elif Dealer_score > 21:
    return text2art('You Won!')
  elif Player_score > Dealer_score:
    return text2art('You Won!')
  else:
    return text2art('You Lost!')
def Blackjack():
    print(blackjack_logo)
    Player_cards = []
    Dealer_cards = []
    Game_Over = False

    for _ in range(2):
        Player_cards.append(random_card())
        Dealer_cards.append(random_card())
    while not Game_Over:
        print('-'*25,'Players Hand','-'*25)
        Player_score = score_generator(Player_cards)
        Dealer_score = score_generator(Dealer_cards)
        for i in range(len(Player_cards)):
            print(ascii_version_of_card(Card(Player_cards[i].split(' ')[0],Player_cards[i].split(' ')[1])),sep='   ') 
        print(f"   Your cards: {Player_cards}, current score: {Player_score}")
        print('-'*25,'Dealers Hand','-'*25)
        print(ascii_version_of_hidden_card(Card('Diamonds','Ace'),Card(Dealer_cards[0].split(' ')[0],Dealer_cards[0].split(' ')[1])),sep='   ') #Card('Diamonds','Ace'),
        print(f"   Dealer's first card: {Dealer_cards[0]}")

        if Player_score == 0 or Dealer_score == 0 or Player_score > 21:
            Game_Over = True
        else:
            Choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if Choice.lower() == "y":
                Player_cards.append(random_card())
            elif Choice.lower()=="n":
                Game_Over = True
            else:
                sys.exit(f"Invalid Input '{Choice}'")
    while Dealer_score != 0 and Dealer_score < 17:
        Dealer_cards.append(random_card())
        Dealer_score = score_generator(Dealer_cards)
    print('-'*25,'Players Final Hand','-'*25)  
    for i in range(len(Player_cards)):
        print(ascii_version_of_card(Card(Player_cards[i].split(' ')[0],Player_cards[i].split(' ')[1])),sep='   ')
    print(f"   Your final hand: {Player_cards},\n Final score: {Player_score}")
    print('-'*25,'Dealers Final Hand','-'*25)
    for i in range(len(Dealer_cards)):
        print(ascii_version_of_card(Card(Dealer_cards[i].split(' ')[0],Dealer_cards[i].split(' ')[1])),sep='   ')          
    print(f"   Dealer's final hand: {Dealer_cards}, Final score: {Dealer_score}")
    print(Score_comparsion(Player_score, Dealer_score))
    print('-'*64)
while input("Do you want to play a game of Blackjack? Type 'y' for yes or any key to exit: ").lower()  =='y':
    Blackjack()
print(text2art('Goodbye!'))

