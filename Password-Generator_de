import random

try:
    passwort_laenge = int(input("Geben Sie die Anzahl der Zeichen ein, aus denen das Passwort bestehen soll: "))
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein.")
    exit()

if passwort_laenge <= 0:
    print("Bitte geben Sie eine Zahl größer als 0 ein.")
    exit()

zeichen = [
    "+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

passwort = ""
for i in range(passwort_laenge):
    passwort += random.choice(zeichen)

print("Generiertes Passwort:", passwort)
