import random

wlist = ["Fenster", "Buch", "Computer", "Tisch", "Stuhl", "Auto", "Haus", "Lampe", "Telefon", "Uhr", "Brot", "Milch",
         "Butter", "Käse", "Apfel", "Birne", "Banane", "Orange", "Zitrone", "Erdbeere"]
Angaben = set()
Worts = set()
default = "____________________"
lives = 10

def Wort():
    x = wlist[random.randrange(19)]
    print(x)
    for i in x:
        Worts.add(i)
    print(Worts)
    return x


wort = Wort()
b = default[0:len(wort)]


def Drucken(Eingabe, wort):
    global b
    index = wort.find(Eingabe)

    while index != -1:
        b = b[:index] + Eingabe + b[index + 1:]
        index = wort.find(Eingabe, index + 1)
        print(b)


def Eingabe(x):
    global lives
    if x.isnumeric():
        print("Falsche Eingabe! versuche es erneut.")
    elif not x:
        print("Falsche Eingabe! versuche es erneut.")
    elif x not in Worts:
        print("falsch")
        lives = lives - 1
        print(lives)
        if lives == 0:
            print("verkackt")
            exit()
    Angaben.add(x)
    return x


def checkwin():
    if b == wort:
        print("Du hasst gewonnen!")
        return False
    else:
        return True


print(b)

# print(Worts)

while True:
    x = input("Test: ")
    Eingabe(x)
    Drucken(x, wort)
    # print(Worts)
    # print(Angaben)
    if not checkwin():
        break
