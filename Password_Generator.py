import random 

try:
    sifre_soru = int(input("Şifre oluşturmak istediğiniz karakter sayısını giriniz: "))
except ValueError:
    print("Lütfen geçerli bir sayı giriniz.")
    exit()

if sifre_soru <= 0:
    print("Lütfen 0'dan büyük bir sayı giriniz.")
    exit()

sifreler = [
    "+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

sifre = ""
for i in range(sifre_soru):
    sifre += random.choice(sifreler)

print("Oluşturulan şifre:", sifre)