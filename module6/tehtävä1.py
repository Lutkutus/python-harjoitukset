import random
nopat = int(input("Kuinka monta arpakuutiota: "))
summa = 0
for i in range(nopat):
    noppa = random.randint(1, 6)
    summa += noppa
    print(noppa)

print("Silmälukujen summa on:", summa)
