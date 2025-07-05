import random

try:
    moji_suu = int(input("パスワードに使用したい文字数を入力してください: "))
except ValueError:
    print("有効な数字を入力してください。")
    exit()

if moji_suu <= 0:
    print("0より大きい数字を入力してください。")
    exit()

moji_list = [
    "+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

password = ""
for i in range(moji_suu):
    password += random.choice(moji_list)

print("生成されたパスワード:", password)
