import random

oikea_luku = random.randint(1, 10)

arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != oikea_luku:

    if arvaus > oikea_luku:
        print("Liian suuri arvaus")

    else:
        print("Liian pieni arvaus")

    arvaus = int(input("Arvaa uudestaan: "))

print("Oikein")