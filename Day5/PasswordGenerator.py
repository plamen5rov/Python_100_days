#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for i in range(1, num_letters + 1):
    n = random.randint(0, len(letters)-1)
    password += letters[n]
for i in range(1, num_symbols + 1):
    n = random.randint(0, len(symbols)-1)
    password += symbols[n]
for i in range(1, num_numbers + 1):
    n = random.randint(0, len(numbers)-1)
    password += numbers[n]
print(f"Your password is: {password}\n\n")

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
strong_password = password[:]

def fisher_yates_shuffle(sequence):
    """Fisher-Yates shuffle algorithm."""
    for i in range(len(sequence) - 1, 0, -1):
        j = random.randint(0, i)
        sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

# Assuming strong_password is a list of characters
shuffled_password = fisher_yates_shuffle(list(strong_password))

# Convert the list back to a string
strong_password = ''.join(shuffled_password)

print(f"Your strong password is: {strong_password}")

