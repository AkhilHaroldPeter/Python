import string
from cipher_art import *
from vigenere import encrypt, decrypt, random_key 
import sys
from art import *
#Note : Have used inbuild packages to keep this project simple.(vigenere)
#To code the algorithm from scratch, you could refer here : https://www.geeksforgeeks.org/vigenere-cipher/

alphabet_list = list(string.ascii_lowercase)*2#list(string.ascii_letters)
exit_flag = False
while not exit_flag:
    def caesar():
        def caesar_cipher(choice,input_text,shift_value):
            if choice.lower() == 'encode' or choice.lower() == 'decode':
                cipher_text = ""
                if choice.lower() == 'decode':
                    shift_value*=-1
                for letter in input_text:
                    if letter in alphabet_list:
                        position = alphabet_list.index(letter)
                        encryted_letter = alphabet_list[position+shift_value]
                        cipher_text+=encryted_letter
                    else:
                        cipher_text+=letter
                print("-"*50)
                print(f"The {choice}d text is '{cipher_text}'")
                print("-"*50)
            else:
                print(f'The value provided "{choice}" is incorrect!')
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if choice not in ['encode','decode']:
            sys.exit(f'The value provided "{choice}" is incorrect!')
        else:
            text_to_encode_or_decode = input("Type your message:\n").lower()
            shift_amount = int(input("Type the shift number:\n"))  
            shift_amount=shift_amount%26
            caesar_cipher(choice,text_to_encode_or_decode,shift_amount)
    def vigenere():
        def vigenere_cipher_key():
            cipher_key:str = random_key() # one can even use user-defined key such as `qwerty`
            return cipher_key
        def vigenere_encrypt(value):
            cipher_key = vigenere_cipher_key()
            return f'Encrypted Value : "{encrypt(value, cipher_key)}"\nCipher Key : "{cipher_key}"'    
        def vigenere_decrypt(cipher,cipher_key):
            try:
                return f'Decrypted Value : "{decrypt(cipher, cipher_key)}"'
            except:
                return f'Unable to decode!. Invalid value "{cipher}" or "{cipher_key}" provided!'
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if choice.lower()=='encode':
            text_to_encode = input("Type your message : ")
            print('-'*50)
            print(vigenere_encrypt(text_to_encode))
            print('Note:Please keep the key provided if you want to decode the message!')        
            print('-'*50)
        elif choice.lower()=='decode':
            text_to_decode = input("Please enter the message you want to decode :")
            cipher_key = input("Please enter the cipher key : ")
            print('-'*50)
            print(vigenere_decrypt(text_to_decode,cipher_key))
            print('-'*50)
        else:
            print(f"The Provided Value '{choice}' is invalid!")
    print(cipher_logo)
    algo_choice = input('Welcome, Please Select an algorithm to encrpyt or decrypt your message\n1."caesar" for Caesar Cipher \n2."vigenere" for Vigenere Cipher \n')
    if algo_choice.lower() == 'caesar':
        print(caesar_cipher_logo)
        caesar()
    elif algo_choice.lower() == 'vigenere':
        print(vigenere_cipher_logo)
        vigenere()
    else:
        sys.exit(f"The provided value '{algo_choice}' is not available.Please select from the algorithms provided!" )
    choice_to_continue = input('Do you want to continue. Type "y" for Yes and "n" for No :').lower()
    if choice_to_continue=='y':
        exit_flag=False
    elif choice_to_continue=='n':
        exit_flag=True
        print(text2art("Adios Amigo!"))
    else:
        sys.exit(f"The given input {choice_to_continue} is invalid!")
    
