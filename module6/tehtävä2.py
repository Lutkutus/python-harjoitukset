luvut = []

luku = input("Anna ensimmäinen luku tai lopeta painamalla enter: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna seuraava luku tai lopeta painamalla enter: ")

luvut.sort(reverse=True)

print(luvut[:5])
