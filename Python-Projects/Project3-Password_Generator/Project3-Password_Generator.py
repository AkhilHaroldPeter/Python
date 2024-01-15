import random
import string
from art import *
import sys

letters = list(string.ascii_lowercase)+list(string.ascii_uppercase) #here we use string.ascii_lower for all lowercase alphabets from a-z and same for string.ascii_uppercase
all_symbols = [c for c in string.printable if c not in string.ascii_letters and c not in string.digits]
symbols = all_symbols[:-6] # have removed the last 6 symbols(' ', '\t', '\n', '\r', '\x0b', '\x0c')

# print("Password Generator!")
print(text2art("Password  Generator!"))
nr_letters= input("How many letters would you like in your password?\n")
if not nr_letters.isdigit():
    sys.exit(f'The provided input "{nr_letters}" is not a valid type.')
else:
    nr_letter=int(nr_letters)
nr_symbols = input(f"How many symbols would you like?\n")
if not nr_symbols.isdigit():
    sys.exit(f'The provided input "{nr_symbols}" is not a valid type.')
else:
    nr_symbols=int(nr_symbols)
nr_numbers = input(f"How many numbers would you like?\n")
if not nr_numbers.isdigit():
    sys.exit(f'The provided input "{nr_symbols}" is not a valid type.')
else:
    nr_numbers=int(nr_numbers)
password = ""
password_list = []
for i in range(1,int(nr_letters)+1):
  password_list += random.choice(letters)
for i in range(1,int(nr_numbers)+1):
  password_list += str(random.randint(0,9))#Here we randomly take a value between 0 and 9 using randint
for i in range(1,int(nr_symbols)+1):
  password_list += random.choice(symbols)
random.shuffle(password_list)
password = ""
for chr in password_list:
  password+=chr
print(f"Your password is: {password}")
