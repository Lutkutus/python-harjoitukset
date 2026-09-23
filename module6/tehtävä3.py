jakaja = 2

luku = int(input("Anna lukusi: "))

while jakaja < luku and luku % jakaja != 0:
    jakaja += 1

if jakaja < luku:
    print("Luku", luku, "ei ole alkuluku.")

if jakaja == luku:
    print("Luku", luku, "on alkuluku.")
