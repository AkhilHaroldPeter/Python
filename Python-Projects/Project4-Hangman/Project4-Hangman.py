import random
import pandas as pd
from art import *
from mal import Anime
import pycountry
from os import system, name
import os
import sys
from random_words import RandomWords
from hangman_ascii_art import *

df = pd.read_csv(os.getcwd()+"/anime_subset.csv") # The Data provided is from kaggle. Link :https://www.kaggle.com/datasets/marlesson/myanimelist-dataset-animes-profiles-reviews?select=animes.csv
#Note: The above data has been filtered for NSFW content.
title_list=[x for x in df['title']]

game_over = False
while not game_over:
    live_remaining = 6
    random_word=""
    print(logo)
    choice = input(f"Please select from the given choices:\n1.Select '1' for Random Word\n2.Select '2' for Anime names \n3.Select '3' for 'Country' ")
    if choice.isdigit() and int(choice)==1:
        rw = RandomWords()
        random_word = rw.random_word()
    elif choice.isdigit() and int(choice)==2:
        # anime = Anime(random.randint(1,1000))
        # random_word = str(anime.title).lower()
        random_word = str(random.choice(title_list).lower())
    elif choice.isdigit() and int(choice)==3:
        countries = list(pycountry.countries)
        country_names = [country.name for country in countries]
        random_word=str(random.choice(country_names)).lower()
    else:
        sys.exit(f'The provided input "{choice}" is invalid.Please type from the provided values!')
    
##    print(random_word)
    display = []
    for _ in random_word:
        display.append("_")
    guessed_list=[]
    while "_" in display and live_remaining!=0:
        guessed_letter = input("Guess a letter : ").lower()
        if guessed_letter in guessed_list:
            print(f"You've already guessed '{guessed_letter}'")
        for letter in range(len(random_word)):
            if guessed_letter == random_word[letter]:
                display[letter] = guessed_letter
                guessed_list.append(guessed_letter)
        if guessed_letter not in random_word and guessed_letter not in guessed_list:
            print(f"You've guessed '{guessed_letter}',that's not in the word.You lose a life!")
            live_remaining-=1
            print(stages[live_remaining])
            guessed_list.append(guessed_letter)

        print(' '.join(display))
        print(f"guessed letters : {(',').join(guessed_list)}")
        print(f"guesses left : {live_remaining}")
        print('-'*50)
        #clear_terminal()#uncomment this code to clear screen in jupyter notebook

    if '_' not in display:
        print(text2art("YOU WON!",font="small"))
    else:
        print(text2art("YOU LOST!",font='small'))
    choice = input('Do you want to continue: "y" for Yes and "n" for No :').lower()
    if choice=='y':
        pass
    elif choice=='n':
        game_over=True
        print(text2art("GAME OVER!",font='small'))
        # sys.exit()
    else:
        sys.exit(f'The provide value {choice} is not valid')
        

