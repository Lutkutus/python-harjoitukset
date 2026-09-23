pienin = None
suurin = None

while True:
    syote = input("Anna luku: ")

    if syote == "":
        break

    luku = int(syote)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

print(f"Pienin luku on {pienin}")
print(f"Suurin luku on {suurin}")