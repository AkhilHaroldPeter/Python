from Higher_Lower_art import *
import pandas as pd
import random
from art import *
import sys

# population_file_path = ""  
df_pop = pd.read_csv("World_Population_2022.csv") #population_file_path)
df_pop = df_pop.iloc[:,[0,-1]]
df_pop.iloc[:,-1] = [int(str(x).replace('.0','')) if str(x) not in ['','nan','NaN'] else '' for x in df_pop.iloc[:,-1]]
Population_dict = dict(zip(df_pop['Country Name'], df_pop[df_pop.columns[-1]]))

def random_country_generator():
    return random.choice(list(Population_dict.keys()))
def country_population(country):
    return Population_dict[country]
def compare(pop_a,pop_b,random_country_a,random_country_b,choice):
    if pop_a>pop_b:
        max_pop = pop_a
        max_country = random_country_a
    else:
        max_pop = pop_b
        max_country = random_country_b      
    formatted_population = ','.join([str(max_pop)[i:i+3] for i in range(0, len(str(max_pop)), 3)])[::-1]
    if choice==max_country:
        return "{} has a population of {}\n{}".format(max_country, formatted_population, text2art("You're Correct!")),True  #','.join([str(max(pop_a,pop_b))[i:i+3] for i in range(0, len(str(max(pop_a,pop_b))), 3)])[::-1]
    else:
        return "{} has a population of {}\n{}".format(max_country, formatted_population, text2art("You're Wrong!")),False  
def Higher_Lower_Game():    
    Game_Continue = True
    print(game_logo)
    print('Guess which country has the higher population!')
    random_country_a=random_country_generator()
    random_country_b=random_country_generator()
    Score=0
    while Game_Continue:
        random_country_a=random_country_b
        random_country_b=random_country_generator()
        while random_country_a==random_country_b:
            random_country_b=random_country_generator
        print(f"A. Population of {random_country_a}")
        print(vs_art)
        print(f"B. Population of {random_country_b}")
        pop_a = country_population(random_country_a)    
        pop_b = country_population(random_country_b)
        choice = input("Which among the mentioned countries has a greater population? 'A' or 'B'")
        if choice.upper()=='A':
            choice=random_country_a
        elif choice.upper()=='B':
            choice=random_country_b
        else:
            sys.exit(f"Invalid entry! {choice} is not a valid option. Type 'A' or 'B' : ")
        print(compare(pop_a,pop_b,random_country_a,random_country_b,choice)[0])
        if compare(pop_a,pop_b,random_country_a,random_country_b,choice)[1]==True:
            Score+=1
            print(f"You're Score is {Score}")
            pass
        elif compare(pop_a,pop_b,random_country_a,random_country_b,choice)[1]==False:
            print(text2art("You've Lost!"))
            print(f"You're Final Score {Score}")
            print('-'*100)
            
            Game_Continue=False
        
Game_Over=False
while not Game_Over:
    Choice_to_play = input("Do you want to play Higher Lower Game? 'Y' or 'N' : ")
    if Choice_to_play.upper()=='Y':
        Higher_Lower_Game()
    elif Choice_to_play.upper()=='N':
        print(text2art('GOODBYE!'))
        Game_Over=True
    else:
        sys.exit(f"'{Choice_to_play}' is an invalid entry!")
        
        
