# Rouissat abdelhakim

les_nombres = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10"
}

phrase_avant=input("donner une phrase : ")
# en transform tous les lettre en lower case
phrase = phrase_avant.lower()


# déviser la phrase a une liste des mots
mots = phrase.split()


# si en trouve un mot = mot dans le dictionaire en le remplace par son chiffre
for i in range(len(mots)):
    if mots[i] in les_nombres:
        mots[i] = les_nombres[mots[i]]


# apres en regroupe les mots
phrase=" ".join(mots)


#affichage
print("avant :")
print(phrase_avant)
print("\napres :")
print(phrase)