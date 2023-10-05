cislo = int(input("Zadaj číslo v dvojkovej sústave: "))
desiatkove_cislo = 0
exponent = 0

while cislo > 0:
    posledna_cifra = cislo % 10
    desiatkove_cislo += posledna_cifra * (2 ** exponent)
    cislo = cislo // 10
    exponent += 1

print("Číslo v desiatkovej sústave:", desiatkove_cislo)
