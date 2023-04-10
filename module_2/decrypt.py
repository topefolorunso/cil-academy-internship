#Cryptography Challenge #1

import random, time

#A basic decryption algorithm...
def decrypt(ciphertext, key):
    print("...")
    time.sleep(1)
    
    print("Decrypting ciphertext...")
    plaintext = ciphertext[::key+1]
    time.sleep(1)
    
    print("...")
    time.sleep(1)

    return plaintext

    # current_index = 0
    # plaintext = ciphertext[current_index]
    # current_index = current_index + key + 1
    # while current_index < len(ciphertext):
    #   plaintext += ciphertext[current_index]
    #   current_index = current_index + key + 1
      
    # return plaintext

def get_input():
    ciphertext = input("Enter a message to decrypt (ciphertext): ")
    key = int(input("Input a key as a number between 1 and 10: "))
    while not (key>=1 and key<=10):
        print("Invalid key, try again!")
        key = int(input("Input a key as a number between 1 and 10: "))
        
    return ciphertext, key
 
#Main program starts here...
def run_program():
    #Input...
    ciphertext, key = get_input()
    #Process...
    plaintext = decrypt(ciphertext, key)
    #Output...
    print(f"Plaintext: {plaintext}")
    
    decrypt_more_ciphertext_or_exit()
    
def decrypt_more_ciphertext_or_exit():
    more_input = input("Do you have more ciphertext to decrypt? Yes/No (Y/N): ").lower()
    while more_input not in ("yes", "y", "no", "n"):
        print("Invalid response, try again!")
        more_input = input("Do you have more ciphertext to decrypt? Yes/No (Y/N): ").lower()
    if more_input in ("yes", "y"):
        run_program()
    elif more_input in ("no", "n"):
        print("Thank you for using Tope's decryption program!")
        exit()

run_program()
