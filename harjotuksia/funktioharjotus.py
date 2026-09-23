import random

heittojen_summa = 0

def heita_noppaa(kerrat, tahkot=6):

    summa = 0
    heittokerrat = 0

    for n in range(kerrat):
        summa += random.randint(1, tahkot)
        heittokerrat += 1
    return summa, heittokerrat

(heittojen_summa , heitot) = heita_noppaa(4, 21)

print(f"Heittojen summa on: {heittojen_summa}")

# def printtaa_hei():
#     print("Hei!")

# printtaa_hei()
