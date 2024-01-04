firstLetters = ""

name = input().split("-")
for word in name:
    firstLetters += word[0]

print(firstLetters.upper())