import random

tahkot = int(input("Nopan tahkojen lukumäärä: "))

def sat_nop(tahkot):
    return random.randint(1, tahkot)


noppa = 0

while noppa != tahkot:
    noppa = sat_nop(tahkot)
    print(noppa)
