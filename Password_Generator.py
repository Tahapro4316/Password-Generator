import random 

try:
    password_question = int(input("Enter the number of characters you want to create a password: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if password_question <= 0:
    print("Please enter a number greater than 0.")
    exit()

passwords = [
    "+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

password = ""
for i in range(password_question):
    password += random.choice(passwords)

print("Generated password:", password)
