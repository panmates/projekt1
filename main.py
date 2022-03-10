TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of , more , than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

oddelovac = 80 * "-"
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

ciste_slova = []
velke_pismena = []
zaciatocne_pismena = []
male_pismena = []
pocet_cisel = []
suma = 0

username = input("username:").lower()
password = input("password:").lower()

print(oddelovac)

if users.get(username) == password:
    print(f"Welcome to the app {username}." "We have 3 texts to be analyzed.", sep="\n")
else:
    print("Unregistered user, terminating the program.")
    exit()

print(oddelovac)

cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
if cislo_textu.isnumeric() and (1 <= int(cislo_textu) <= 3):
    print(oddelovac)
else:
    print("Zadané cislo alebo tvar neexistuje")
    exit()
print(oddelovac)

TEXT = TEXTS[int(cislo_textu) - 1]
slova_textu = TEXT.split()

pocetnost_slov = {}

for slovo in slova_textu:
    ciste_slovo = slovo.strip(".,-,")

    if ciste_slovo != "":
        ciste_slova.append(ciste_slovo)
    if ciste_slovo.istitle():
        zaciatocne_pismena.append(slovo)
    if ciste_slovo.isupper():
        velke_pismena.append(slovo)
    if ciste_slovo.islower():
        male_pismena.append(slovo)
    if ciste_slovo.isnumeric():
        pocet_cisel.append(slovo)
        suma += int(slovo)

    pocetnost_slov[len(slovo)] = pocetnost_slov.get(len(slovo), 0) + 1

print(
    f"There are {len(ciste_slova)} words in the selected text.",
    f"There are {len(zaciatocne_pismena)} titlecase words.",
    f"There are {len(velke_pismena)} uppercase words.",
    f"There are {len(male_pismena)} lowercase words.",
    f"There are {len(pocet_cisel)} numeric strings.",
    f"The sum of all the numbers {suma}.",
    sep="\n"
    )

print(oddelovac)

slovnik_vyskytov = {}
for slovo in ciste_slova:
    if slovo in slovnik_vyskytov:
        continue
    slovnik_vyskytov[slovo] = ciste_slova.count(slovo)

print("{:>4}|{:<18}| {}".format("LEN","OCCURENCES", "NR."))

pocetnost_slov_zoradene = dict(sorted(pocetnost_slov.items())) 

for k in pocetnost_slov_zoradene:
  print("{:>4}|{:<18}| {}".format(k, "*" * pocetnost_slov_zoradene[k], pocetnost_slov_zoradene[k]))
  
print(oddelovac)
exit()
