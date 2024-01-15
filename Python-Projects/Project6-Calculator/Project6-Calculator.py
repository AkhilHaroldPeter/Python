from Calculator_art import *
from art import *
import sys
# import shutup;shutup.please()

def add(num1,num2):
    return int(num1)+int(num2)
def sub(num1,num2):
    return int(num1)-int(num2)
def mult(num1,num2):
    return int(num1)*int(num2)
def div(num1,num2):
    return int(num1)/int(num2)
def mod(num1,num2):
    return int(num1)%int(num2)    
def power(num1,num2):
    return int(num1)**int(num2)
operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div,
  "%": mod,
  "**": power
}

def Calculator():        
    print(text2art("Calculator"))
    print(Calc_logo)
    num1 = input("Please enter the first number : ")
    if not str(num1).isdigit():
        sys.exit(f'Error! Please type a valid number! "{num1}" is not acceptable')
    for symbol in operations:
        print(symbol)
    exit_flag = True
    while exit_flag:
        operation_selected = input("Please pick an operation from the given operations: ")
        if operation_selected not in [x for x in operations]:
            sys.exit(f'"{operation_selected}" operation is not available!')
        num2 = input("Please enter the second number : ")
        if not str(num2).isdigit():
            sys.exit(f'Error! Please type a valid number! "{num2}" is not acceptable')        
        calculator_func = operations[operation_selected]#accessing the value using key(the operation selected by user)
        print(calculator_func)
        result = calculator_func(num1,num2)
        print('-'*50)
        print(f"{num1} {operation_selected} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type x to exit! ").lower()
        if  choice == 'y':
          num1 = result
        elif choice =='n':
          exit_flag = False
          Calculator()
        elif choice =='x':
            print(text2art("Goodbye!"))
            sys.exit()
        else:
            sys.exit(f"{choice} is invalid!")
Calculator()        