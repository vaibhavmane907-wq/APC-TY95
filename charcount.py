s = input("Enter string: ")
v = c = d = sp = sc = 0
for i in s:
    if i.lower() in "aeiou": v += 1
    elif i.isalpha(): c += 1
    elif i.isdigit(): d += 1
    elif i == " ": sp += 1
    else: sc += 1
print("Vowels:", v, "Consonants:", c, "Digits:", d, "Spaces:", sp, "Special:", sc)